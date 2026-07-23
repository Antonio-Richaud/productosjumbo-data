# Medios de producción

Este directorio conserva los medios asociados a productos en el entorno de producción de Productos Jumbo.

## Alcance actual

La extracción del 23 de julio de 2026 incluye únicamente imágenes:

- imágenes destacadas;
- imágenes de galería;
- imágenes adjuntas al producto;
- imágenes referenciadas dentro del contenido.

Los archivos PDF y ZIP fueron inventariados, pero no se descargaron en esta fase.

## Organización

- `uploads/`: copia de las imágenes conservando su ruta relativa original en WordPress.
- `inventory/`: relaciones entre productos, SKU, adjuntos e imágenes.
- `reports/`: métricas, archivos faltantes y resultados de validación.

## Almacenamiento

Los archivos de `uploads/` se administran mediante Git LFS.

Cada imagen tiene un hash SHA-256 registrado en:

    inventory/image-checksums.tsv

No se modificó WordPress, WooCommerce ni el contenido de producción durante la extracción.
