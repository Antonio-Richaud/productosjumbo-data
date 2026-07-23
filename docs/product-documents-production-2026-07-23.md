# Documentos técnicos de productos en producción — 2026-07-23

## Objetivo

Descargar y versionar los PDF y ZIP asociados con los productos del catálogo
de producción, conservando todas las rutas originales y sus relaciones.

## Alcance

Se incluyen:

- fichas técnicas;
- dibujos 2D en PDF;
- paquetes ZIP de dibujos o archivos técnicos;
- PDF técnicos sin clasificación explícita;
- paquetes ZIP técnicos sin clasificación explícita.

## Política de duplicados

No se eliminó ningún archivo por nombre, ruta, tamaño o hash.

Cuando dos o más rutas contienen exactamente el mismo contenido, todas se
conservan y se registran en:

    media/production/documents/reports/duplicate-document-content.tsv

## Relaciones con productos

Las relaciones normalizadas se encuentran en:

    media/production/documents/inventory/document-product-relations.tsv

Cada fila vincula un producto con un documento mediante:

- ID de producto;
- SKU;
- nombre;
- estado;
- tipo de documento;
- ruta original;
- ruta en el repositorio;
- adjunto de WordPress;
- tipos de relación;
- URL original;
- SHA-256.

## Archivos faltantes

Las referencias que no tienen un archivo físico en producción se conservan en:

    media/production/documents/reports/missing-documents.tsv

No se generaron archivos sustitutos ni se inventaron contenidos.

## Almacenamiento

Los binarios se almacenan mediante Git LFS bajo:

    media/production/documents/uploads/

Después de clonar el repositorio se requiere:

    git lfs install
    git lfs pull

## Seguridad

La extracción fue de solo lectura. No se modificó WordPress, WooCommerce,
staging ni producción.
