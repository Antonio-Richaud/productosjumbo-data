# Documentos técnicos de productos

Fuente: producción  
Fecha: 2026-07-23  
Ruta original: `/wp-content/uploads/`

## Estado validado

- documentos descargados: 355;
- PDF: 183;
- ZIP: 172;
- productos relacionados: 248;
- relaciones producto-documento: 358;
- tamaño validado: 157.30 MB;
- referencias faltantes: 5;
- grupos con contenido repetido: 1;
- rutas en grupos duplicados: 2;
- archivos eliminados por duplicidad: 0;
- rutas originales preservadas: sí.

## Clasificación

- `technical_sheet`: 121 fichas técnicas;
- `drawing_2d`: 22 dibujos 2D en PDF;
- `drawing_2d_package`: 172 paquetes ZIP identificados como dibujo o archivo 2D;
- `technical_pdf`: 40 PDF técnicos sin etiqueta explícita.

## Organización

    documents/
    ├── uploads/
    ├── inventory/
    ├── manifests/
    ├── reports/
    ├── README.md
    └── SHA256SUMS

### Binarios

    uploads/

Los archivos conservan su ruta original `año/mes/nombre.ext` y se administran mediante Git LFS.

### Inventarios

    inventory/document-files.tsv
    inventory/document-product-relations.tsv
    inventory/product-document-summary.tsv
    inventory/document-checksums.tsv

### Manifiestos

    manifests/document-source-paths.txt
    manifests/document-repository-paths.txt
    manifests/source-document-summary.json

### Reportes

    reports/download-summary.json
    reports/duplicate-document-content.tsv
    reports/missing-documents.tsv

## Referencias faltantes

Las cinco referencias sin archivo físico afectan cuatro SKU:

- `REH-00-02-00`;
- `RES-00-02-00`;
- `REH-00-03-00`;
- `CIR-00-02-00`.

El detalle exacto se conserva en:

    reports/missing-documents.tsv

No se generaron archivos sustitutos.

## Duplicados

Dos rutas de `AED-004-FORTE-PECHO.pdf` comparten el mismo contenido SHA-256. Ambas se conservaron porque representan rutas originales distintas de WordPress.

Git LFS puede reutilizar el mismo objeto binario sin eliminar ninguna ruta.

## Git LFS

Después de clonar el repositorio:

    git lfs install
    git lfs pull

No debe reemplazarse un puntero LFS por contenido binario directo.

## Integridad

- `SHA256SUMS` cubre inventarios, manifiestos, reportes y documentos;
- cada archivo tiene tamaño y SHA-256 registrado;
- los punteros LFS fueron validados contra el inventario;
- los documentos se enlazan mediante ID de producto, SKU y tipo de relación;
- no existen archivos adicionales fuera del manifiesto.

## Actualizaciones futuras

1. generar un inventario nuevo desde producción en modo solo lectura;
2. comparar rutas, tamaños y hashes;
3. descargar solo documentos nuevos o modificados;
4. conservar las rutas originales;
5. regenerar relaciones, manifiestos y checksums;
6. validar Git LFS;
7. documentar faltantes y duplicados;
8. actualizar la documentación mediante pull request.

## Documentación completa

    ../../../docs/product-documents-production-2026-07-23.md

No se modificó WordPress, WooCommerce, staging ni producción.
