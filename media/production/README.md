# Medios de producción

Este directorio conserva los medios asociados a productos en el entorno de producción de Productos Jumbo.

## Alcance actual

La extracción del 23 de julio de 2026 incluye únicamente imágenes:

- imágenes destacadas;
- imágenes de galería;
- imágenes adjuntas al producto;
- imágenes referenciadas dentro del contenido.

Los archivos PDF y ZIP fueron inventariados, pero no se descargaron en esta fase.

## Estado validado

- productos analizados: 542;
- productos con medios: 539;
- productos sin medios: 3;
- imágenes descargadas: 880;
- objetos Git LFS únicos: 872;
- relaciones únicas producto-imagen: 960;
- tamaño total validado: 204.73 MB;
- imágenes faltantes: 0;
- errores de punteros Git LFS: 0.

El inventario general también registra:

- 185 PDF;
- 175 ZIP;
- 1 referencia sin tipo reconocido;
- 6 referencias no gráficas sin archivo físico.

## Organización

- `uploads/`: copia de las imágenes conservando su ruta relativa original en WordPress.
- `inventory/`: relaciones entre productos, SKU, adjuntos, funciones de imagen y checksums.
- `reports/`: métricas, archivos faltantes y resultados de validación.

## Inventarios principales

### Consulta por producto

    inventory/product-image-map.tsv
    inventory/product-image-summary.tsv

### Relaciones originales

    inventory/image-product-relations.tsv
    inventory/product-media-relations.tsv

### Archivos únicos e integridad

    inventory/image-media.tsv
    inventory/unique-media.tsv
    inventory/image-files.txt
    inventory/image-checksums.tsv

### Productos sin medios

    inventory/products-without-media.tsv

## Reportes principales

    reports/media-summary.json
    reports/image-size-analysis.json
    reports/download-summary.json
    reports/lfs-validation.json
    reports/missing-media.tsv
    reports/non-image-media.tsv
    reports/suspicious-media-rows.tsv

## Almacenamiento

Los archivos de `uploads/` se administran mediante Git LFS.

Después de clonar el repositorio debe ejecutarse:

    git lfs install
    git lfs pull

Cada imagen tiene un hash SHA-256 registrado en:

    inventory/image-checksums.tsv

Git LFS almacena 872 objetos binarios únicos para las 880 rutas existentes. Ocho grupos de contenido duplicado abarcan 16 rutas, por lo que un mismo objeto puede ser reutilizado sin eliminar ninguna ruta original de WordPress.

## Convenciones

- Los archivos conservan su ruta relativa `año/mes/nombre.ext`.
- No se duplica una imagen física por cada producto que la utiliza.
- Las asociaciones producto-imagen se mantienen en TSV.
- `data/current` sigue siendo la fuente canónica de productos y categorías.
- Esta carpeta funciona como capa complementaria de evidencia y activos.
- Los snapshots y reportes no deben modificarse manualmente para ocultar anomalías.

## Actualizaciones futuras

Una actualización de medios debe:

1. generar un inventario nuevo desde producción en modo solo lectura;
2. comparar rutas, tamaños y hashes contra el inventario vigente;
3. descargar solo imágenes nuevas o modificadas;
4. conservar las rutas originales;
5. regenerar mapas, resúmenes y checksums;
6. validar los punteros Git LFS;
7. revisar archivos faltantes y productos sin medios;
8. actualizar la documentación mediante un pull request separado.

La documentación completa de la extracción inicial se encuentra en:

    ../../docs/product-media-production-2026-07-23.md

No se modificó WordPress, WooCommerce ni el contenido de producción durante la extracción.

## Documentos técnicos descargados

Los PDF y ZIP vinculados con productos se encuentran en:

    media/production/documents/uploads/

Inventarios y relaciones:

    media/production/documents/inventory/

Reportes de faltantes y contenido repetido:

    media/production/documents/reports/

No se eliminaron archivos repetidos.
