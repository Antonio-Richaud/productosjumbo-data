# Medios de productos en producción — 2026-07-23

## Objetivo

Inventariar, descargar, validar y versionar los medios asociados a los productos del catálogo de producción de Productos Jumbo, sin modificar WordPress, WooCommerce ni el contenido servido por el sitio.

## Fuente

Entorno revisado:

    https://www.productosjumbo.com

Ruta de medios en el servidor:

    /home/dh_yiamy4/productosjumbo.com/wp-content/uploads

Fecha de extracción:

    2026-07-23

## Alcance del inventario

Se analizaron 542 productos de WooCommerce y sus relaciones con medios mediante:

- imagen destacada (`_thumbnail_id`);
- galería de WooCommerce (`_product_image_gallery`);
- adjuntos cuyo `post_parent` corresponde al producto;
- URLs de `wp-content/uploads` dentro del contenido y extracto;
- metadatos que referencian fichas técnicas y dibujos 2D;
- variaciones y adjuntos relacionados cuando aplicó.

## Resultado general

- productos analizados: 542;
- productos con algún medio: 539;
- productos sin medios: 3;
- relaciones producto-medio detectadas: 1,913;
- medios únicos detectados: 1,241;
- archivos únicos existentes: 1,235;
- referencias a archivos faltantes: 6;
- tamaño total de archivos existentes inventariados: 362.03 MB.

Distribución por tipo:

- 199 AVIF;
- 329 JPEG;
- 335 PNG;
- 17 WebP;
- 185 PDF;
- 175 ZIP;
- 1 referencia sin tipo reconocido.

## Imágenes versionadas

En esta fase se descargaron únicamente imágenes.

Resultado:

- 880 rutas de imagen;
- 880 imágenes existentes;
- 0 imágenes faltantes;
- 204.73 MB validados;
- 872 objetos binarios únicos en Git LFS;
- 8 grupos de contenido duplicado;
- 16 rutas incluidas en grupos duplicados;
- 539 productos con imágenes;
- 960 relaciones únicas producto-imagen;
- 0 errores de punteros Git LFS.

Las imágenes conservan su ruta relativa original de WordPress bajo:

    media/production/uploads/

## Almacenamiento con Git LFS

Los binarios se administran mediante la regla:

    media/production/uploads/** filter=lfs diff=lfs merge=lfs -text

Después de clonar el repositorio es necesario ejecutar:

    git lfs install
    git lfs pull

Git LFS reutiliza el mismo objeto cuando varias rutas contienen exactamente el mismo contenido. Por esa razón existen 880 rutas, pero 872 objetos binarios únicos.

## Inventarios generados

### `image-files.txt`

Lista ordenada de las 880 rutas relativas descargadas.

### `image-media.tsv`

Registro único por imagen, incluyendo MIME, ruta, existencia y tamaño.

### `image-product-relations.tsv`

Relaciones originales detectadas entre productos y archivos de imagen.

### `product-image-map.tsv`

Mapa normalizado producto-imagen con:

- ID de producto;
- SKU;
- nombre;
- estado;
- ruta relativa;
- ruta dentro del repositorio;
- MIME;
- IDs de adjunto;
- funciones o roles de la imagen.

### `product-image-summary.tsv`

Resumen por producto con cantidad de imágenes únicas y conteos por función.

### `image-checksums.tsv`

Hash SHA-256, tamaño y MIME de cada archivo descargado.

### `product-media-relations.tsv`

Inventario completo de relaciones, incluyendo imágenes, PDF, ZIP y referencias no descargadas.

### `unique-media.tsv`

Inventario consolidado de los 1,241 medios únicos detectados.

## Reportes generados

- `media-summary.json`: resumen del inventario completo;
- `image-size-analysis.json`: tamaños, MIME y archivos de imagen más grandes;
- `download-summary.json`: resultado de la descarga y comparación contra el manifiesto;
- `lfs-validation.json`: validación de punteros y objetos Git LFS;
- `missing-media.tsv`: seis referencias sin archivo físico;
- `non-image-media.tsv`: PDF, ZIP y referencia sin tipo;
- `suspicious-media-rows.tsv`: filas sospechosas detectadas durante la validación.

## Validaciones realizadas

### Integridad estructural

Se comprobó el número esperado de columnas en todos los TSV y no se detectaron filas malformadas.

Resultado:

    TSV_STRUCTURE_OK

### Descarga

Se compararon las rutas esperadas con los archivos descargados.

Resultado:

- 880 archivos esperados;
- 880 archivos descargados;
- 0 faltantes;
- 0 adicionales;
- 0 diferencias de tamaño.

Marcador:

    DOWNLOAD_VALIDATION_OK

### Checksums

Cada imagen fue leída y validada mediante SHA-256. Los resultados se conservan en:

    media/production/inventory/image-checksums.tsv

### Git LFS

Se comprobó para cada imagen:

- puntero LFS válido;
- tamaño declarado igual al archivo físico;
- OID SHA-256 igual al contenido real;
- atributo `filter=lfs` activo.

Marcador:

    LFS_POINTER_VALIDATION_OK

## Productos sin medios

Se detectaron tres productos sin relaciones de medios:

- ID `7307`, SKU `PPR1-2-1`, Jumbo Rubber Sport Tipo Tartan A 13 mm, privado;
- ID `28389`, borrador sin nombre y sin SKU;
- ID `29376`, Banco Cubo, privado y sin SKU.

Estos casos deben revisarse mediante tareas separadas.

## Referencias faltantes

Las seis referencias faltantes no corresponden a imágenes descargadas:

- PDF de `REH-00-02-00`;
- ZIP de `RES-00-02-00`;
- ZIP de `REH-00-03-00`;
- PDF de `REH-00-03-00`;
- ZIP de `CIR-00-02-00`;
- una ruta sin extensión asociada a `COL-AB-03-00`.

El detalle exacto se encuentra en:

    media/production/reports/missing-media.tsv

## Decisiones de diseño

### Una sola copia física

No se crea una copia de la imagen por cada producto. Cada ruta original se conserva una sola vez y las asociaciones se documentan en archivos TSV.

### Conservación de rutas

Las imágenes mantienen la estructura `año/mes/nombre.ext` para conservar trazabilidad con WordPress y simplificar futuras comparaciones.

### Separación entre datos y medios

`data/current` sigue siendo la fuente canónica de productos y taxonomías. `media/production` es una capa complementaria de evidencia y activos.

### Documentos no descargados

Los PDF y ZIP fueron inventariados, pero quedaron fuera de esta fase para evitar mezclar imágenes comerciales con documentos técnicos sin una clasificación previa.

## Flujo recomendado para futuras actualizaciones

1. actualizar `main` y crear una rama específica;
2. extraer un inventario nuevo desde producción en modo solo lectura;
3. comparar el inventario nuevo contra `unique-media.tsv` e `image-checksums.tsv`;
4. identificar altas, bajas, cambios de tamaño y cambios de hash;
5. descargar únicamente imágenes nuevas o modificadas;
6. conservar las rutas originales;
7. regenerar relaciones, resúmenes y checksums;
8. validar punteros Git LFS;
9. revisar productos sin medios y referencias rotas;
10. actualizar la fecha y métricas de la documentación;
11. abrir un pull request independiente;
12. fusionar mediante squash después de validar.

## Acciones no realizadas

Durante este proceso no se realizaron:

- modificaciones en WordPress;
- cambios en productos o categorías;
- reemplazos de imágenes en producción;
- eliminación de adjuntos;
- corrección de referencias faltantes;
- descarga de PDF o ZIP;
- despliegues a staging o producción.

## Commit de incorporación inicial

La incorporación inicial de imágenes se realizó mediante el PR `#2` y quedó fusionada en `main` con el commit:

    39ccb3f71c942bb193a4bc6fa2058f3543825b66
