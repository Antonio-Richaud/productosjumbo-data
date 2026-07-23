# Medios de producción

Este directorio conserva los medios asociados con productos en el entorno de producción de Productos Jumbo.

## Alcance actual

La capa de medios del 23 de julio de 2026 incluye dos colecciones versionadas mediante Git LFS:

- imágenes comerciales y de producto en `uploads/`;
- PDF y ZIP técnicos en `documents/uploads/`.

También conserva inventarios generales que registran relaciones con medios faltantes o no clasificados.

## Estado consolidado

### Imágenes

- productos analizados: 542;
- productos con medios: 539;
- productos sin medios: 3;
- imágenes descargadas: 880;
- objetos Git LFS únicos: 872;
- relaciones únicas producto-imagen: 960;
- tamaño validado: 204.73 MB;
- imágenes faltantes: 0;
- errores de punteros Git LFS: 0.

### Documentos técnicos

- documentos descargados: 355;
- PDF: 183;
- ZIP: 172;
- productos relacionados: 248;
- relaciones producto-documento: 358;
- tamaño validado: 157.30 MB;
- referencias faltantes: 5;
- grupos de contenido duplicado: 1;
- archivos eliminados por duplicidad: 0.

### Inventario general original

El inventario completo de relaciones de WordPress registró:

- 880 imágenes;
- 185 referencias PDF;
- 175 referencias ZIP;
- 1 referencia sin tipo reconocido;
- 6 referencias sin archivo físico.

La colección técnica descargada contiene 183 PDF y 172 ZIP porque cinco referencias documentales no existen físicamente en producción. La sexta referencia faltante es una ruta sin extensión y permanece documentada únicamente en el inventario general.

## Organización

    media/production/
    ├── uploads/
    ├── inventory/
    ├── reports/
    ├── README.md
    └── documents/
        ├── uploads/
        ├── inventory/
        ├── manifests/
        ├── reports/
        ├── README.md
        └── SHA256SUMS

### Imágenes

- `uploads/`: archivos conservando su ruta relativa original de WordPress;
- `inventory/`: relaciones producto-imagen, funciones, adjuntos y checksums;
- `reports/`: métricas, faltantes y validaciones.

Inventarios principales:

    inventory/product-image-map.tsv
    inventory/product-image-summary.tsv
    inventory/image-product-relations.tsv
    inventory/product-media-relations.tsv
    inventory/image-media.tsv
    inventory/unique-media.tsv
    inventory/image-files.txt
    inventory/image-checksums.tsv
    inventory/products-without-media.tsv

Reportes principales:

    reports/media-summary.json
    reports/image-size-analysis.json
    reports/download-summary.json
    reports/lfs-validation.json
    reports/missing-media.tsv
    reports/non-image-media.tsv
    reports/suspicious-media-rows.tsv

### Documentos técnicos

- `documents/uploads/`: PDF y ZIP conservando sus rutas originales;
- `documents/inventory/`: documentos, relaciones, resúmenes y checksums;
- `documents/manifests/`: rutas esperadas y fuente de extracción;
- `documents/reports/`: resumen, duplicados y referencias faltantes.

Inventarios principales:

    documents/inventory/document-files.tsv
    documents/inventory/document-product-relations.tsv
    documents/inventory/product-document-summary.tsv
    documents/inventory/document-checksums.tsv

Reportes principales:

    documents/reports/download-summary.json
    documents/reports/duplicate-document-content.tsv
    documents/reports/missing-documents.tsv

## Git LFS e integridad

Las imágenes y documentos binarios se administran mediante Git LFS.

Después de clonar:

    git lfs install
    git lfs pull

Cada archivo descargado cuenta con tamaño y SHA-256 en sus inventarios. Los duplicados por contenido pueden reutilizar un mismo objeto LFS sin eliminar ninguna ruta original.

## Convenciones

- Los archivos conservan la estructura `año/mes/nombre.ext`.
- No se crea una copia por cada producto relacionado.
- Las asociaciones producto-medio se mantienen en TSV.
- `data/current` continúa siendo la fuente canónica del catálogo.
- Los snapshots e inventarios no deben editarse para ocultar anomalías.
- Las referencias faltantes se documentan; no se generan sustitutos.

## Actualizaciones futuras

1. generar un inventario nuevo desde producción en modo solo lectura;
2. comparar rutas, tamaños y hashes contra el estado vigente;
3. identificar altas, bajas y archivos modificados;
4. descargar solo archivos nuevos o modificados;
5. conservar las rutas originales;
6. regenerar inventarios, relaciones y checksums;
7. validar punteros, OID y tamaños de Git LFS;
8. revisar faltantes, duplicados y productos sin medios;
9. actualizar la documentación mediante un pull request separado.

## Documentación relacionada

    ../../docs/product-media-production-2026-07-23.md
    ../../docs/product-documents-production-2026-07-23.md
    documents/README.md

Las extracciones fueron de solo lectura. No se modificó WordPress, WooCommerce, staging ni producción.
