# Medios de productos en producción — 2026-07-23

## Objetivo

Inventariar, descargar, validar y versionar los medios asociados con los productos del catálogo de producción, sin modificar WordPress, WooCommerce ni el contenido servido por el sitio.

## Fuente

- entorno: producción;
- sitio: https://www.productosjumbo.com;
- ruta de medios: `/home/dh_yiamy4/productosjumbo.com/wp-content/uploads`;
- fecha de inventario: 2026-07-23;
- productos analizados: 542.

## Alcance del inventario general

Las relaciones se obtuvieron mediante:

- imagen destacada (`_thumbnail_id`);
- galería de WooCommerce (`_product_image_gallery`);
- adjuntos cuyo `post_parent` corresponde al producto;
- URLs de `wp-content/uploads` dentro del contenido y extracto;
- metadatos de fichas técnicas y dibujos 2D;
- variaciones y adjuntos relacionados cuando aplicó.

Resultado del inventario original:

- relaciones producto-medio detectadas: 1,913;
- medios únicos detectados: 1,241;
- archivos únicos existentes: 1,235;
- referencias a archivos faltantes: 6;
- tamaño total inventariado: 362.03 MB.

Distribución:

- 199 AVIF;
- 329 JPEG;
- 335 PNG;
- 17 WebP;
- 185 PDF;
- 175 ZIP;
- 1 referencia sin tipo reconocido.

## Fase 1: imágenes versionadas

La primera fase descargó únicamente imágenes y se integró mediante el PR `#2`.

Resultado:

- rutas de imagen: 880;
- imágenes existentes: 880;
- imágenes faltantes: 0;
- tamaño validado: 204.73 MB;
- objetos binarios únicos en Git LFS: 872;
- grupos de contenido duplicado: 8;
- rutas en grupos duplicados: 16;
- productos con imágenes: 539;
- relaciones únicas producto-imagen: 960;
- errores de punteros Git LFS: 0.

Ubicación:

    media/production/uploads/

Inventarios:

    media/production/inventory/image-files.txt
    media/production/inventory/image-media.tsv
    media/production/inventory/image-product-relations.tsv
    media/production/inventory/product-image-map.tsv
    media/production/inventory/product-image-summary.tsv
    media/production/inventory/image-checksums.tsv
    media/production/inventory/product-media-relations.tsv
    media/production/inventory/unique-media.tsv

Reportes:

    media/production/reports/media-summary.json
    media/production/reports/image-size-analysis.json
    media/production/reports/download-summary.json
    media/production/reports/lfs-validation.json
    media/production/reports/missing-media.tsv
    media/production/reports/non-image-media.tsv
    media/production/reports/suspicious-media-rows.tsv

## Fase 2: documentos técnicos versionados

Posteriormente, los PDF y ZIP asociados con productos se clasificaron, descargaron y validaron en una colección independiente. Esta fase se integró mediante el PR `#5`.

Resultado:

- documentos descargados: 355;
- PDF: 183;
- ZIP: 172;
- productos relacionados: 248;
- relaciones producto-documento: 358;
- tamaño validado: 157.30 MB;
- referencias documentales faltantes: 5;
- grupo de contenido duplicado: 1;
- rutas dentro del grupo duplicado: 2;
- duplicados eliminados: 0.

Ubicación:

    media/production/documents/uploads/

Inventarios y reportes:

    media/production/documents/inventory/
    media/production/documents/manifests/
    media/production/documents/reports/

Documentación específica:

    docs/product-documents-production-2026-07-23.md

## Diferencia entre inventario y colección documental

El inventario general identificó 185 PDF y 175 ZIP. La colección descargada contiene 183 PDF y 172 ZIP porque cinco referencias documentales no tienen archivo físico en producción:

- un PDF de `REH-00-02-00`;
- un ZIP de `RES-00-02-00`;
- un ZIP y un PDF de `REH-00-03-00`;
- un ZIP de `CIR-00-02-00`.

La sexta referencia faltante del inventario general es una ruta sin extensión asociada con `COL-AB-03-00`; no se clasificó como PDF o ZIP.

## Git LFS

Reglas principales:

    media/production/uploads/** filter=lfs diff=lfs merge=lfs -text
    media/production/documents/uploads/** filter=lfs diff=lfs merge=lfs -text

Después de clonar:

    git lfs install
    git lfs pull

Git LFS reutiliza objetos cuando varias rutas contienen el mismo contenido. Las rutas originales se conservan aunque compartan OID SHA-256.

## Validaciones realizadas

### Imágenes

- estructura de TSV;
- manifiesto contra archivos físicos;
- tamaños;
- SHA-256;
- atributos Git LFS;
- punteros, OID y tamaños declarados;
- ausencia de imágenes faltantes.

### Documentos

- conteos de PDF y ZIP;
- comparación contra el inventario de producción;
- tamaños físicos;
- SHA-256;
- punteros Git LFS;
- OID y tamaño de cada puntero;
- estructura de TSV;
- referencias válidas a productos;
- conservación de duplicados y rutas originales.

## Productos sin medios

El inventario general detectó tres productos sin relaciones de medios:

- ID `7307`, SKU `PPR1-2-1`, Jumbo Rubber Sport Tipo Tartan A 13 mm, privado;
- ID `28389`, borrador sin nombre ni SKU;
- ID `29376`, Banco Cubo, privado y sin SKU.

Estos casos deben tratarse mediante tareas separadas.

## Decisiones de diseño

- Una ruta física se conserva una sola vez y puede relacionarse con varios productos.
- Las rutas `año/mes/nombre.ext` se preservan para mantener trazabilidad con WordPress.
- `data/current` sigue siendo la fuente canónica del catálogo.
- Los medios y documentos funcionan como evidencia y activos complementarios.
- Los duplicados no se eliminan automáticamente.
- Las referencias faltantes no se sustituyen ni se inventan.

## Flujo recomendado

1. actualizar `main` y crear una rama específica;
2. extraer un inventario nuevo en modo solo lectura;
3. comparar rutas, tamaños y hashes;
4. identificar altas, bajas y cambios;
5. descargar únicamente archivos nuevos o modificados;
6. conservar las rutas originales;
7. regenerar relaciones, resúmenes y checksums;
8. validar Git LFS;
9. revisar faltantes, duplicados y productos sin medios;
10. actualizar la documentación;
11. abrir un pull request independiente;
12. fusionar mediante squash después de validar.

## Acciones no realizadas

- modificaciones en WordPress o WooCommerce;
- cambios de productos o categorías;
- reemplazos o eliminación de adjuntos;
- corrección automática de referencias faltantes;
- despliegues a staging o producción.
