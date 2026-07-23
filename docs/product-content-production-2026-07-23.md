# Contenido de productos de producción — 2026-07-23

## Objetivo

Extraer, conservar y normalizar las descripciones y especificaciones asociadas con los productos del catálogo de producción.

La extracción se realizó en modo de solo lectura.

## Fuente

- entorno: producción;
- sitio: https://www.productosjumbo.com/;
- fecha: 2026-07-23;
- referencia del catálogo: snapshot 2026-07-22;
- productos: 542.

## Campos de origen

- descripción larga: `wp_posts.post_content`;
- extracto: `wp_posts.post_excerpt`;
- especificaciones: texto clasificado desde `post_excerpt` o desde secciones explícitas de `post_content`.

Las dimensiones y atributos nativos estructurados de WooCommerce estaban vacíos en los 542 productos analizados.

## Distribución original de campos

- contenido y extracto: 130;
- solo contenido: 45;
- solo extracto: 308;
- sin contenido ni extracto: 59;
- productos con shortcodes: 101.

## Resultado final consolidado

La normalización final, correspondiente al esquema `1.1.1`, produjo:

- productos totales: 542;
- productos con descripción normalizada: 178;
- productos sin descripción: 364;
- productos con especificaciones estructuradas: 443;
- productos sin especificaciones estructuradas: 99;
- filas de especificaciones: 1,910;
- productos completos: 139;
- productos sin descripción: 304 dentro del análisis de completitud;
- productos sin especificaciones: 39 dentro del análisis de completitud;
- productos sin ambos tipos de contenido: 60;
- productos que requieren revisión manual: 32;
- productos con brechas de contenido: 403;
- fragmentos sin interpretar: 0;
- claves de especificación duplicadas detectadas: 2;
- incidencias conservadas de los datos fuente: 7;
- productos con campos eléctricos separados: 6.

Los conteos de completitud son categorías mutuamente excluyentes del estado final y no deben sumarse directamente a los conteos generales de presencia de campos.

## Archivos canónicos

    data/current/product-content.tsv
    data/current/product-content-summary.json
    data/current/product-specifications.tsv
    data/current/specification-dictionary.tsv

`product-content.tsv` contiene una fila por producto.

`product-specifications.tsv` contiene una fila por propiedad técnica y se enlaza mediante `product_id` y `product_sku`.

## Snapshot original

    data/snapshots/2026-07-23/production/content/

El JSONL conserva el HTML, shortcodes, metadatos, versiones normalizadas y hashes SHA-256 de los campos originales.

No debe editarse para corregir o esconder anomalías.

## Reportes

    data/reports/2026-07-23/product-content-summary.json
    data/reports/2026-07-23/content-standardization-summary.json
    data/reports/2026-07-23/products-without-description.tsv
    data/reports/2026-07-23/products-without-specifications.tsv
    data/reports/2026-07-23/products-without-text.tsv
    data/reports/2026-07-23/products-with-content-gaps.tsv
    data/reports/2026-07-23/products-needing-content-review.tsv
    data/reports/2026-07-23/ambiguous-specifications.tsv
    data/reports/2026-07-23/medium-confidence-specifications.tsv
    data/reports/2026-07-23/content-split-specifications.tsv
    data/reports/2026-07-23/duplicate-specification-keys.tsv
    data/reports/2026-07-23/source-data-issues.tsv
    data/reports/2026-07-23/unparsed-specification-fragments.tsv

## Reglas de normalización

- espacios y puntuación normalizados;
- encabezados redundantes retirados;
- etiquetas técnicas convertidas a claves canónicas;
- dimensiones expresadas con el símbolo `×`;
- unidades escritas de forma uniforme;
- singular y plural corregidos;
- ausencia de contenido separada de los casos de revisión;
- información faltante no inventada;
- contenido original preservado;
- prosa no forzada dentro de especificaciones;
- inconsistencias de la fuente reportadas sin corregirse automáticamente.

## Patrones resueltos

Se resolvieron, entre otros:

- fuentes de piso;
- pisos PG1;
- características de piso tipo tartán;
- bancas con alimentación eléctrica;
- letras con base;
- pistas con SKU incrustado;
- productos de concreto;
- encabezados `Medidas`;
- etiquetas `SKU` dentro de especificaciones;
- textos reclasificados correctamente como descripción.

## Propiedades eléctricas

En seis productos, voltaje o consumo estaban mezclados dentro del campo de materiales. Se separaron en:

- `materials`;
- `voltage`;
- `power_consumption`.

También se reparó un efecto de normalización que había sustituido la letra `x` dentro de palabras como `extruido` e `inoxidable`. La corrección se apoyó en `raw_value`, que conserva el valor original.

## Casos de revisión manual

Los 32 productos pendientes se explican por:

- múltiples valores posibles de longitud: 1;
- múltiples valores posibles de área mínima: 1;
- posible inconsistencia de unidad: 7;
- contenido técnico sin límite claro: 23.

Estos casos deben revisarse sin alterar el snapshot original.

## Integridad

Se validó que:

- los 542 IDs coinciden con el catálogo;
- los SKU coinciden con el catálogo;
- los estados coinciden con el catálogo;
- existen 542 registros originales y 542 registros normalizados;
- los valores ausentes no fueron inventados;
- las unidades y etiquetas utilizan convenciones canónicas.

## Limitaciones

La normalización no confirma que cada valor técnico publicado en WordPress sea correcto desde el punto de vista de ingeniería. Las siete posibles incidencias de fuente permanecen documentadas para revisión.

No se modificó WordPress, WooCommerce, staging ni producción.
