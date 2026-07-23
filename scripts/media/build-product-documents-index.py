#!/usr/bin/env python3

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]

SOURCE_NON_IMAGE = (
    ROOT /
    "media/production/reports/non-image-media.tsv"
)

SOURCE_RELATIONS = (
    ROOT /
    "media/production/inventory/"
    "product-media-relations.tsv"
)

PRODUCTS_CURRENT = (
    ROOT /
    "data/current/products-basic.tsv"
)

DOCUMENT_ROOT = (
    ROOT /
    "media/production/documents"
)

DOCUMENT_UPLOADS = DOCUMENT_ROOT / "uploads"
DOCUMENT_INVENTORY = DOCUMENT_ROOT / "inventory"
DOCUMENT_REPORTS = DOCUMENT_ROOT / "reports"
DOCUMENT_MANIFESTS = DOCUMENT_ROOT / "manifests"

MANIFEST_TXT = (
    DOCUMENT_MANIFESTS /
    "document-source-paths.txt"
)

ALLOWED_MIME = {
    "application/pdf",
    "application/zip",
}


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        reader = csv.DictReader(
            handle,
            delimiter="\t",
        )

        return (
            reader.fieldnames or [],
            list(reader),
        )


def write_tsv(
    path: Path,
    fieldnames: list[str],
    rows: Iterable[dict[str, object]],
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            lineterminator="\n",
            quoting=csv.QUOTE_MINIMAL,
            extrasaction="ignore",
        )

        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        while True:
            block = handle.read(
                1024 * 1024
            )

            if not block:
                break

            digest.update(block)

    return digest.hexdigest()


def folded(value: str) -> str:
    value = unicodedata.normalize(
        "NFKD",
        value or "",
    )

    value = "".join(
        character
        for character in value
        if not unicodedata.combining(
            character
        )
    )

    return value.casefold()


def split_values(value: str) -> list[str]:
    if not value:
        return []

    return [
        item.strip()
        for item in re.split(
            r"\s*(?:\||,)\s*",
            value,
        )
        if item.strip()
    ]


def natural_key(value: str) -> tuple[object, ...]:
    parts = re.split(
        r"(\d+)",
        value,
    )

    return tuple(
        int(part)
        if part.isdigit()
        else part.casefold()
        for part in parts
    )


def classify_document(
    relative_path: str,
    mime_type: str,
    relation_types: Iterable[str],
    attachment_titles: Iterable[str],
) -> str:
    relations = " ".join(
        relation_types
    )

    titles = " ".join(
        attachment_titles
    )

    text = folded(
        " ".join([
            relative_path,
            relations,
            titles,
        ])
    )

    explicit_drawing = (
        "_pj_dibujo_2d_url" in relations
        or bool(
            re.search(
                r"\b(?:"
                r"dibujo[\s_-]*2d|"
                r"archivo[\s_-]*2d|"
                r"plano[\s_-]*2d|"
                r"dwg|cad"
                r")\b",
                text,
            )
        )
    )

    explicit_sheet = (
        "_pj_ficha_tecnica_url" in relations
        or bool(
            re.search(
                r"\b(?:"
                r"ficha[\s_-]*tecnica|"
                r"fichatecnica|"
                r"technical[\s_-]*sheet"
                r")\b",
                text,
            )
        )
    )

    if mime_type == "application/zip":
        if explicit_drawing:
            return "drawing_2d_package"

        return "technical_package"

    if explicit_drawing:
        return "drawing_2d"

    if explicit_sheet:
        return "technical_sheet"

    return "technical_pdf"


def validate_relative_path(value: str) -> None:
    path = PurePosixPath(value)

    if not value:
        raise SystemExit(
            "ERROR: ruta vacía."
        )

    if path.is_absolute():
        raise SystemExit(
            f"ERROR: ruta absoluta: {value}"
        )

    if ".." in path.parts:
        raise SystemExit(
            f"ERROR: ruta insegura: {value}"
        )


def main() -> None:
    for directory in (
        DOCUMENT_UPLOADS,
        DOCUMENT_INVENTORY,
        DOCUMENT_REPORTS,
        DOCUMENT_MANIFESTS,
    ):
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    _, media_rows = read_tsv(
        SOURCE_NON_IMAGE
    )

    _, relation_rows = read_tsv(
        SOURCE_RELATIONS
    )

    _, product_rows = read_tsv(
        PRODUCTS_CURRENT
    )

    products_by_id = {
        row["product_id"]: row
        for row in product_rows
    }

    document_rows = [
        row
        for row in media_rows
        if row["mime_type"] in ALLOWED_MIME
    ]

    existing_rows = [
        row
        for row in document_rows
        if (
            row["file_exists"]
            .strip()
            .lower()
            == "yes"
        )
    ]

    missing_rows = [
        row
        for row in document_rows
        if (
            row["file_exists"]
            .strip()
            .lower()
            != "yes"
        )
    ]

    expected_by_path: dict[
        str,
        dict[str, str],
    ] = {}

    for row in existing_rows:
        relative_path = (
            row["relative_path"].strip()
        )

        validate_relative_path(
            relative_path
        )

        if relative_path in expected_by_path:
            raise SystemExit(
                "ERROR: ruta duplicada en inventario: "
                f"{relative_path}"
            )

        expected_by_path[
            relative_path
        ] = row

    expected_paths = set(
        expected_by_path
    )

    actual_paths = {
        path.relative_to(
            DOCUMENT_UPLOADS
        ).as_posix()
        for path in DOCUMENT_UPLOADS.rglob("*")
        if path.is_file()
    }

    missing_downloads = sorted(
        expected_paths - actual_paths,
        key=natural_key,
    )

    extra_downloads = sorted(
        actual_paths - expected_paths,
        key=natural_key,
    )

    if missing_downloads:
        raise SystemExit(
            "ERROR: faltan descargas:\n"
            + "\n".join(
                missing_downloads[:50]
            )
        )

    if extra_downloads:
        raise SystemExit(
            "ERROR: hay archivos adicionales:\n"
            + "\n".join(
                extra_downloads[:50]
            )
        )

    relation_source = [
        row
        for row in relation_rows
        if (
            row["mime_type"] in ALLOWED_MIME
            and row["relative_path"]
            in expected_paths
            and row["file_exists"]
            .strip()
            .lower()
            == "yes"
        )
    ]

    relation_details_by_path: dict[
        str,
        dict[str, set[str]],
    ] = defaultdict(
        lambda: {
            "relation_types": set(),
            "attachment_ids": set(),
            "attachment_titles": set(),
        }
    )

    normalized_relations: dict[
        tuple[str, str],
        dict[str, object],
    ] = {}

    for row in relation_source:
        relative_path = row[
            "relative_path"
        ]

        product_id = row[
            "product_id"
        ].strip()

        if product_id not in products_by_id:
            raise SystemExit(
                "ERROR: relación con producto "
                f"inexistente: {product_id}, "
                f"{relative_path}"
            )

        details = (
            relation_details_by_path[
                relative_path
            ]
        )

        relation_type = (
            row["relation_type"].strip()
        )

        attachment_id = (
            row["attachment_id"].strip()
        )

        attachment_title = (
            row["attachment_title"].strip()
        )

        if relation_type:
            details[
                "relation_types"
            ].add(relation_type)

        if attachment_id:
            details[
                "attachment_ids"
            ].add(attachment_id)

        if attachment_title:
            details[
                "attachment_titles"
            ].add(attachment_title)

        key = (
            product_id,
            relative_path,
        )

        target = normalized_relations.setdefault(
            key,
            {
                "product_id": product_id,
                "relative_path": relative_path,
                "attachment_ids": set(),
                "attachment_titles": set(),
                "relation_types": set(),
            },
        )

        if attachment_id:
            target[
                "attachment_ids"
            ].add(attachment_id)

        if attachment_title:
            target[
                "attachment_titles"
            ].add(attachment_title)

        if relation_type:
            target[
                "relation_types"
            ].add(relation_type)

    document_file_rows = []
    checksum_rows = []

    hashes_by_path: dict[str, str] = {}
    bytes_by_path: dict[str, int] = {}
    document_type_by_path: dict[
        str,
        str,
    ] = {}

    for relative_path in sorted(
        expected_paths,
        key=natural_key,
    ):
        source = expected_by_path[
            relative_path
        ]

        file_path = (
            DOCUMENT_UPLOADS /
            relative_path
        )

        actual_bytes = file_path.stat().st_size
        expected_bytes = int(
            source["bytes"] or 0
        )

        if actual_bytes != expected_bytes:
            raise SystemExit(
                "ERROR: tamaño diferente para "
                f"{relative_path}: "
                f"{actual_bytes} != "
                f"{expected_bytes}"
            )

        digest = sha256(file_path)

        details = (
            relation_details_by_path[
                relative_path
            ]
        )

        document_type = classify_document(
            relative_path,
            source["mime_type"],
            details["relation_types"],
            details["attachment_titles"],
        )

        repository_path = (
            "media/production/documents/"
            f"uploads/{relative_path}"
        )

        hashes_by_path[
            relative_path
        ] = digest

        bytes_by_path[
            relative_path
        ] = actual_bytes

        document_type_by_path[
            relative_path
        ] = document_type

        product_ids = sorted(
            set(
                split_values(
                    source["product_ids"]
                )
            ),
            key=natural_key,
        )

        product_skus = sorted(
            set(
                split_values(
                    source["product_skus"]
                )
            ),
            key=natural_key,
        )

        document_file_rows.append({
            "document_key": source[
                "media_key"
            ],
            "relative_path": relative_path,
            "repository_path": (
                repository_path
            ),
            "document_type": (
                document_type
            ),
            "mime_type": source[
                "mime_type"
            ],
            "extension": (
                Path(
                    relative_path
                ).suffix.lower()
            ),
            "bytes": actual_bytes,
            "sha256": digest,
            "canonical_url": source[
                "canonical_url"
            ],
            "attachment_ids": " | ".join(
                sorted(
                    details[
                        "attachment_ids"
                    ],
                    key=natural_key,
                )
            ),
            "product_ids": " | ".join(
                product_ids
            ),
            "product_skus": " | ".join(
                product_skus
            ),
            "relation_types": " | ".join(
                sorted(
                    details[
                        "relation_types"
                    ]
                )
            ),
        })

        checksum_rows.append({
            "relative_path": relative_path,
            "repository_path": (
                repository_path
            ),
            "mime_type": source[
                "mime_type"
            ],
            "bytes": actual_bytes,
            "sha256": digest,
        })

    product_relation_rows = []

    for (
        product_id,
        relative_path,
    ), relation in sorted(
        normalized_relations.items(),
        key=lambda item: (
            natural_key(item[0][0]),
            natural_key(item[0][1]),
        ),
    ):
        product = products_by_id[
            product_id
        ]

        source = expected_by_path[
            relative_path
        ]

        product_relation_rows.append({
            "product_id": product_id,
            "product_sku": product[
                "sku"
            ],
            "product_name": product[
                "product_name"
            ],
            "product_status": product[
                "post_status"
            ],
            "document_type": (
                document_type_by_path[
                    relative_path
                ]
            ),
            "document_key": source[
                "media_key"
            ],
            "relative_path": relative_path,
            "repository_path": (
                "media/production/documents/"
                f"uploads/{relative_path}"
            ),
            "mime_type": source[
                "mime_type"
            ],
            "bytes": bytes_by_path[
                relative_path
            ],
            "sha256": hashes_by_path[
                relative_path
            ],
            "attachment_ids": " | ".join(
                sorted(
                    relation[
                        "attachment_ids"
                    ],
                    key=natural_key,
                )
            ),
            "attachment_titles": (
                " | ".join(
                    sorted(
                        relation[
                            "attachment_titles"
                        ]
                    )
                )
            ),
            "relation_types": " | ".join(
                sorted(
                    relation[
                        "relation_types"
                    ]
                )
            ),
            "canonical_url": source[
                "canonical_url"
            ],
        })

    relations_by_product: dict[
        str,
        list[dict[str, object]],
    ] = defaultdict(list)

    for row in product_relation_rows:
        relations_by_product[
            str(row["product_id"])
        ].append(row)

    product_summary_rows = []

    for product_id in sorted(
        relations_by_product,
        key=natural_key,
    ):
        product = products_by_id[
            product_id
        ]

        relations = (
            relations_by_product[
                product_id
            ]
        )

        unique_documents = {
            str(row["relative_path"])
            for row in relations
        }

        type_counts = Counter(
            document_type_by_path[
                path
            ]
            for path in unique_documents
        )

        total_bytes = sum(
            bytes_by_path[path]
            for path in unique_documents
        )

        product_summary_rows.append({
            "product_id": product_id,
            "product_sku": product[
                "sku"
            ],
            "product_name": product[
                "product_name"
            ],
            "product_status": product[
                "post_status"
            ],
            "document_count": len(
                unique_documents
            ),
            "pdf_count": sum(
                expected_by_path[path][
                    "mime_type"
                ] == "application/pdf"
                for path in unique_documents
            ),
            "zip_count": sum(
                expected_by_path[path][
                    "mime_type"
                ] == "application/zip"
                for path in unique_documents
            ),
            "technical_sheet_count": (
                type_counts[
                    "technical_sheet"
                ]
            ),
            "drawing_2d_count": (
                type_counts[
                    "drawing_2d"
                ]
            ),
            "drawing_2d_package_count": (
                type_counts[
                    "drawing_2d_package"
                ]
            ),
            "technical_pdf_count": (
                type_counts[
                    "technical_pdf"
                ]
            ),
            "technical_package_count": (
                type_counts[
                    "technical_package"
                ]
            ),
            "total_bytes": total_bytes,
        })

    paths_by_hash: dict[
        str,
        list[str],
    ] = defaultdict(list)

    for path, digest in hashes_by_path.items():
        paths_by_hash[digest].append(path)

    products_by_document_path: dict[
        str,
        set[str],
    ] = defaultdict(set)

    for row in product_relation_rows:
        sku = str(
            row["product_sku"]
        ).strip()

        if sku:
            products_by_document_path[
                str(row["relative_path"])
            ].add(sku)

    duplicate_rows = []

    for digest, paths in sorted(
        paths_by_hash.items()
    ):
        if len(paths) < 2:
            continue

        sorted_paths = sorted(
            paths,
            key=natural_key,
        )

        product_skus = sorted(
            {
                sku
                for path in sorted_paths
                for sku in (
                    products_by_document_path[
                        path
                    ]
                )
            },
            key=natural_key,
        )

        duplicate_rows.append({
            "sha256": digest,
            "bytes": bytes_by_path[
                sorted_paths[0]
            ],
            "path_count": len(
                sorted_paths
            ),
            "paths": " | ".join(
                sorted_paths
            ),
            "product_skus": " | ".join(
                product_skus
            ),
            "action": "preserved",
        })

    missing_output_rows = []

    for source in sorted(
        missing_rows,
        key=lambda row: natural_key(
            row["relative_path"]
        ),
    ):
        missing_output_rows.append({
            "document_key": source[
                "media_key"
            ],
            "relative_path": source[
                "relative_path"
            ],
            "mime_type": source[
                "mime_type"
            ],
            "canonical_url": source[
                "canonical_url"
            ],
            "referenced_url": source[
                "referenced_url"
            ],
            "product_ids": source[
                "product_ids"
            ],
            "product_skus": source[
                "product_skus"
            ],
            "product_names": source[
                "product_names"
            ],
            "relation_types": source[
                "relation_types"
            ],
            "status": (
                "missing_in_production"
            ),
        })

    write_tsv(
        DOCUMENT_INVENTORY /
        "document-files.tsv",
        [
            "document_key",
            "relative_path",
            "repository_path",
            "document_type",
            "mime_type",
            "extension",
            "bytes",
            "sha256",
            "canonical_url",
            "attachment_ids",
            "product_ids",
            "product_skus",
            "relation_types",
        ],
        document_file_rows,
    )

    write_tsv(
        DOCUMENT_INVENTORY /
        "document-product-relations.tsv",
        [
            "product_id",
            "product_sku",
            "product_name",
            "product_status",
            "document_type",
            "document_key",
            "relative_path",
            "repository_path",
            "mime_type",
            "bytes",
            "sha256",
            "attachment_ids",
            "attachment_titles",
            "relation_types",
            "canonical_url",
        ],
        product_relation_rows,
    )

    write_tsv(
        DOCUMENT_INVENTORY /
        "product-document-summary.tsv",
        [
            "product_id",
            "product_sku",
            "product_name",
            "product_status",
            "document_count",
            "pdf_count",
            "zip_count",
            "technical_sheet_count",
            "drawing_2d_count",
            "drawing_2d_package_count",
            "technical_pdf_count",
            "technical_package_count",
            "total_bytes",
        ],
        product_summary_rows,
    )

    write_tsv(
        DOCUMENT_INVENTORY /
        "document-checksums.tsv",
        [
            "relative_path",
            "repository_path",
            "mime_type",
            "bytes",
            "sha256",
        ],
        checksum_rows,
    )

    write_tsv(
        DOCUMENT_REPORTS /
        "duplicate-document-content.tsv",
        [
            "sha256",
            "bytes",
            "path_count",
            "paths",
            "product_skus",
            "action",
        ],
        duplicate_rows,
    )

    write_tsv(
        DOCUMENT_REPORTS /
        "missing-documents.tsv",
        [
            "document_key",
            "relative_path",
            "mime_type",
            "canonical_url",
            "referenced_url",
            "product_ids",
            "product_skus",
            "product_names",
            "relation_types",
            "status",
        ],
        missing_output_rows,
    )

    document_type_counts = Counter(
        row["document_type"]
        for row in document_file_rows
    )

    mime_counts = Counter(
        row["mime_type"]
        for row in document_file_rows
    )

    total_bytes = sum(
        bytes_by_path.values()
    )

    duplicate_path_count = sum(
        int(row["path_count"])
        for row in duplicate_rows
    )

    summary = {
        "schema_version": "1.0.0",
        "source_environment": "production",
        "products_total": len(
            product_rows
        ),
        "products_with_documents": len(
            product_summary_rows
        ),
        "documents_downloaded": len(
            document_file_rows
        ),
        "document_relations": len(
            product_relation_rows
        ),
        "missing_document_references": len(
            missing_output_rows
        ),
        "mime_types": dict(
            sorted(mime_counts.items())
        ),
        "document_types": dict(
            sorted(
                document_type_counts.items()
            )
        ),
        "total_bytes": total_bytes,
        "total_megabytes": round(
            total_bytes / 1024 / 1024,
            2,
        ),
        "duplicate_content_groups": len(
            duplicate_rows
        ),
        "paths_in_duplicate_groups": (
            duplicate_path_count
        ),
        "duplicates_deleted": 0,
        "all_original_paths_preserved": True,
        "checks": {
            "all_expected_files_downloaded": True,
            "no_extra_files": True,
            "sizes_match_source_inventory": True,
            "checksums_generated": True,
            "product_references_valid": True,
        },
    }

    (
        DOCUMENT_REPORTS /
        "download-summary.json"
    ).write_text(
        json.dumps(
            summary,
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    repository_paths = [
        str(row["repository_path"])
        for row in document_file_rows
    ]

    (
        DOCUMENT_MANIFESTS /
        "document-repository-paths.txt"
    ).write_text(
        "".join(
            f"{path}\n"
            for path in repository_paths
        ),
        encoding="utf-8",
    )

    readme = f"""# Documentos técnicos de productos

Fuente: producción

Ruta original:

    /wp-content/uploads/

Archivos descargados:

- total: {len(document_file_rows)};
- PDF: {mime_counts['application/pdf']};
- ZIP: {mime_counts['application/zip']};
- productos relacionados: {len(product_summary_rows)};
- relaciones producto-documento: {len(product_relation_rows)};
- referencias faltantes: {len(missing_output_rows)};
- grupos con contenido repetido: {len(duplicate_rows)};
- archivos eliminados por duplicidad: 0.

Los documentos conservan su ruta original bajo:

    media/production/documents/uploads/

Inventarios:

    inventory/document-files.tsv
    inventory/document-product-relations.tsv
    inventory/product-document-summary.tsv
    inventory/document-checksums.tsv

Reportes:

    reports/download-summary.json
    reports/duplicate-document-content.tsv
    reports/missing-documents.tsv

Clasificación:

- `technical_sheet`: ficha técnica identificada explícitamente;
- `drawing_2d`: dibujo 2D en PDF;
- `drawing_2d_package`: paquete ZIP identificado como dibujo o archivo 2D;
- `technical_pdf`: PDF técnico sin etiqueta explícita;
- `technical_package`: paquete ZIP sin etiqueta explícita.

Los archivos repetidos por contenido se conservaron en todas sus rutas.
No se realizó ninguna eliminación automática.
"""

    (
        DOCUMENT_ROOT / "README.md"
    ).write_text(
        readme,
        encoding="utf-8",
    )

    checksums_path = (
        DOCUMENT_ROOT /
        "SHA256SUMS"
    )

    checksum_targets = sorted(
        (
            path
            for path in DOCUMENT_ROOT.rglob("*")
            if path.is_file()
            and path != checksums_path
            and path.name != (
                "document-source-paths.nul"
            )
        ),
        key=lambda path: natural_key(
            path.relative_to(
                DOCUMENT_ROOT
            ).as_posix()
        ),
    )

    with checksums_path.open(
        "w",
        encoding="utf-8",
    ) as handle:
        for path in checksum_targets:
            relative = path.relative_to(
                DOCUMENT_ROOT
            ).as_posix()

            handle.write(
                f"{sha256(path)}  {relative}\n"
            )

    print(
        f"DOCUMENTS_DOWNLOADED="
        f"{len(document_file_rows)}"
    )

    print(
        f"PRODUCTS_WITH_DOCUMENTS="
        f"{len(product_summary_rows)}"
    )

    print(
        f"DOCUMENT_RELATIONS="
        f"{len(product_relation_rows)}"
    )

    print(
        f"MISSING_DOCUMENT_REFERENCES="
        f"{len(missing_output_rows)}"
    )

    print(
        f"DUPLICATE_CONTENT_GROUPS="
        f"{len(duplicate_rows)}"
    )

    print(
        f"TOTAL_BYTES={total_bytes}"
    )

    print("DOCUMENT_INDEX_BUILD_OK")


if __name__ == "__main__":
    main()
