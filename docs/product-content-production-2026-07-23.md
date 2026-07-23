# Contenido de productos de producción — 2026-07-23

## Objetivo

Extraer y versionar las descripciones y especificaciones asociadas a
los productos del catálogo de producción.

La extracción se realizó en modo de solo lectura.

## Fuente

- entorno: producción;
- sitio: https://www.productosjumbo.com/;
- fecha: 2026-07-23;
- productos: 542.

## Campos de origen

- descripción larga: `wp_posts.post_content`;
- extracto: `wp_posts.post_excerpt`;
- especificaciones: texto identificado dentro del extracto o dentro
  de una sección explícita de `post_content`.

Las dimensiones y atributos estructurados de WooCommerce están vacíos
en los 542 productos analizados.

## Distribución de campos

- contenido y extracto: 130;
- solo contenido: 45;
- solo extracto: 308;
- sin contenido ni extracto: 59.

## Resultado

- productos con descripción: 175;
- productos sin descripción: 367;
- productos con especificaciones: 446;
- productos sin especificaciones: 96;
- especificaciones de confianza alta: 421;
- especificaciones de confianza media: 25;
- casos ambiguos: 23;
- productos con shortcodes: 101.

## Archivos canónicos

    data/current/product-content.tsv
    data/current/product-content-summary.json

La tabla utiliza `product_id` y `product_sku` para relacionar cada
registro con el catálogo y con el inventario de imágenes.

## Snapshot original

    data/snapshots/2026-07-23/production/content/

El archivo JSONL conserva el contenido HTML y los shortcodes originales,
además de versiones normalizadas y hashes SHA-256 por campo.

## Reportes

    data/reports/2026-07-23/product-content-summary.json
    data/reports/2026-07-23/products-without-description.tsv
    data/reports/2026-07-23/products-without-specifications.tsv
    data/reports/2026-07-23/products-without-text.tsv
    data/reports/2026-07-23/ambiguous-specifications.tsv
    data/reports/2026-07-23/medium-confidence-specifications.tsv
    data/reports/2026-07-23/content-split-specifications.tsv

## Limitaciones

La clasificación de especificaciones no modifica el contenido original.
Los casos de confianza media y los casos ambiguos deben conservarse
como pendientes hasta una revisión manual.

No se inventaron descripciones ni especificaciones para productos que
no cuentan con esos campos en producción.

## Estandarización del contenido

El contenido se organiza mediante dos tablas canónicas:

    data/current/product-content.tsv
    data/current/product-specifications.tsv

`product-content.tsv` contiene una fila por producto.

`product-specifications.tsv` contiene una fila por propiedad técnica,
utilizando claves, etiquetas, valores y unidades normalizadas.

Reglas aplicadas:

- espacios y puntuación normalizados;
- encabezados redundantes retirados;
- etiquetas técnicas convertidas a claves canónicas;
- dimensiones expresadas con el símbolo `×`;
- unidades escritas de forma uniforme;
- singular y plural corregidos;
- conteo de especificaciones calculado desde la tabla técnica;
- ausencia de contenido separada de los casos de revisión;
- información faltante no inventada;
- contenido original preservado en el snapshot.

Resultado:

- productos: 542;
- especificaciones individuales: 1831;
- productos completamente estructurados: 420;
- productos parcialmente estructurados: 9;
- productos no estructurados: 17;
- productos sin especificaciones: 96;
- productos que requieren revisión manual: 72;
- productos con brechas de contenido: 403.

Los productos con información faltante se encuentran en:

    data/reports/2026-07-23/products-with-content-gaps.tsv

Los casos que requieren revisar la interpretación se encuentran en:

    data/reports/2026-07-23/products-needing-content-review.tsv

La ausencia de una descripción o especificación no se clasifica por sí
sola como error de normalización.
## Normalización final de formatos

Se resolvieron automáticamente los patrones restantes de producción:

- fuentes de piso;
- pisos PG1;
- características de piso tipo tartán;
- bancas con alimentación eléctrica;
- letras con base;
- pistas con SKU incrustado;
- productos de concreto;
- encabezados `Medidas`;
- etiquetas `SKU` dentro de especificaciones;
- textos que correspondían realmente a una descripción.

Resultado:

- productos: 542;
- productos con especificaciones estructuradas: 443;
- especificaciones individuales: 1900;
- fragmentos no interpretados: 0;
- casos de revisión manual: 32;
- incidencias detectadas en los datos fuente: 7.

El diccionario canónico se encuentra en:

    data/current/specification-dictionary.tsv

Las posibles inconsistencias de unidades se encuentran en:

    data/reports/2026-07-23/source-data-issues.tsv

No se corrigieron automáticamente valores que podrían representar
errores en el contenido original.

## Separación de propiedades eléctricas

Se detectaron 6 productos cuyo campo de materiales
incluía también voltaje o consumo energético.

Estos datos se separaron en las claves canónicas:

- `materials`;
- `voltage`;
- `power_consumption`.

También se corrigió un efecto de normalización que había sustituido la
letra `x` dentro de palabras como `extruido` e `inoxidable`.

La corrección se realizó utilizando `raw_value`, que conserva el valor
original extraído de producción.
