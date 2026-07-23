# Conciliación del catálogo — 2026-07-22

## Objetivo

Auditar el repositorio `productosjumbo-data`, producción, staging y la fuente comercial `Secciones por categoría.xlsx` para establecer una versión canónica verificable del catálogo.

La auditoría se realizó sin modificar WordPress, WooCommerce, producción ni staging.

## Fuentes revisadas

### Repositorio

Snapshot anterior:

    data/snapshots/2026-07-15/

Estado inicial:

- 540 productos;
- 484 publicados;
- 21 borradores;
- 35 privados;
- 74 categorías;
- 626 relaciones producto-categoría;
- 5 productos sin categoría.

### Producción

Entorno:

    https://www.productosjumbo.com

Snapshot:

    data/snapshots/2026-07-22/production/

Estado:

- 542 productos;
- 489 publicados;
- 18 borradores;
- 35 privados;
- 74 categorías;
- 627 relaciones producto-categoría;
- 5 productos sin categoría.

### Staging

Entorno:

    https://staging.productosjumbo.com

Snapshot:

    data/snapshots/2026-07-22/staging/

Estado:

- 537 productos;
- 479 publicados;
- 23 borradores;
- 35 privados;
- 86 categorías;
- 626 relaciones producto-categoría;
- 0 productos sin categoría.

### Fuente comercial

Archivo original:

    data/sources/2026-07-22/secciones-por-categoria.xlsx

Versión normalizada:

    data/sources/2026-07-22/secciones-por-categoria-normalizado.tsv

Contenido:

- 345 filas de productos;
- 345 SKU únicos;
- 12 sectores;
- 0 SKU duplicados;
- 1 modelo vacío.

## Decisiones de diseño

### Fuente canónica

`data/current` se establece como la fuente canónica auditada del catálogo.

Producción permanece como sistema operativo, pero sus cambios deberán extraerse, compararse y aprobarse antes de actualizar la versión canónica.

### Llave de comparación

El SKU se utiliza como llave comercial primaria.

El ID de WordPress se conserva como identificador técnico específico de cada entorno.

### Sectores comerciales

Los sectores del Excel se almacenan como una capa independiente.

No se convierten automáticamente en categorías de WooCommerce.

### Alias de SKU

Los SKU históricos o alternativos se relacionan con un SKU canónico y no se utilizan para crear productos duplicados.

## Cambios detectados en producción

Entre el 15 y el 22 de julio de 2026 se detectaron:

- 3 IDs nuevos;
- 1 ID eliminado;
- incremento neto de 2 productos;
- 5 SKU nuevos;
- 3 SKU retirados;
- 2 reemplazos de SKU sobre el mismo ID;
- 3 productos que cambiaron de borrador a publicado;
- 83 cambios de nombre;
- 0 cambios de slug;
- 0 categorías agregadas;
- 0 categorías eliminadas.

### Productos agregados

- `32713` — `EVA-PR-02-00` — Juego Atraction Basic;
- `32728` — `EOS-CR-01-00` — Juego Barcelona;
- `32733` — `TDF-00-01-00` — Juego Vizcaya.

### Producto eliminado

- `6868` — `TEM-PR-06-01` — Módulo Imperio.

### Reemplazos de SKU

- producto `6082`:
  - anterior: `EOS-PR-01-00`;
  - actual: `EOS-PR-01-02`;
  - estado: borrador a publicado.

- producto `6836`:
  - anterior: `EOS-PR-15-00`;
  - actual: `EOS-PR-15-03`;
  - estado: borrador a publicado.

### Cambio terminológico

Se detectaron 83 cambios de nombre, principalmente la sustitución de la palabra `Módulo` por `Juego`.

No se modificaron los slugs, por lo que las URLs conservaron su estructura.

## Diferencias entre staging y producción

Los IDs de WordPress no coinciden en numerosos productos, aun cuando comparten SKU.

Esto confirma que los IDs no deben utilizarse como llave universal.

Staging contiene 12 categorías raíz numéricas y vacías:

- `72`;
- `74`;
- `75`;
- `76`;
- `78`;
- `79`;
- `84`;
- `92`;
- `107`;
- `108`;
- `338`;
- `340`.

Estas categorías no se incorporaron a la fuente canónica.

## Conciliación comercial

Resultado:

- 345 filas analizadas;
- 311 resueltas mediante SKU directo;
- 32 resueltas mediante alias;
- 343 productos canónicos comerciales;
- 343 relaciones producto-sector;
- 2 registros pendientes;
- 0 colisiones de productos canónicos.

Archivos:

    data/commercial/current/resolved-commercial-products.tsv
    data/commercial/current/product-commercial-sectors.tsv
    data/commercial/current/sku-aliases.tsv
    data/commercial/current/unresolved-commercial-products.tsv
    data/commercial/current/commercial-reconciliation-summary.json

## Evidencia para alias

Los alias se clasificaron utilizando:

- coincidencia única de nombre normalizado;
- títulos de productos publicados;
- nombres de imágenes activas;
- archivos adjuntos;
- metadatos de WordPress;
- estado del producto;
- categoría;
- inspección manual de casos ambiguos.

Los archivos multimedia permitieron asociar claves comerciales nuevas con los productos publicados correspondientes.

Ejemplos:

- `IOS-PR-01-04` → `MEV-CR-01-00`;
- `TDF-00-02-02` → `MEL-CR-03-00`;
- `EOS-PR-08-02` → `MER-PR-03-00`;
- `EOS-PR-19-02` → `MEV-CR-02-00`;
- `TEM-PR-07-01` → `TEM-PR-07-20`;
- `EOS-IN-05-02` → `MEC-CR-08-00`.

La relación completa se encuentra en:

    data/commercial/current/sku-aliases.tsv

## Registros comerciales pendientes

### BAN-00-15-00 — Banca Tubular

Clasificación:

    missing_from_woocommerce

No se encontró evidencia en:

- productos;
- títulos;
- descripciones;
- metadatos;
- adjuntos;
- nombres de archivos.

Debe confirmarse si es un producto nuevo, retirado o pendiente de carga.

### SVC-NEG — Home Top-It

Clasificación:

    requires_commercial_validation

Existe un producto llamado `TOP-IT-TOPE DE CONTENSION`, SKU `LEPDM-AMA`, pero la similitud textual no es suficiente para confirmar que ambos registros sean equivalentes.

No se creó un alias automático.

## Anomalías activas de producción

### SKU duplicado

El SKU `EJE-EST-10-00` está asignado a dos productos publicados:

- ID `32320`;
- ID `32423`.

Ambos se llaman `EJERCITADOR BARRAS DE ESTIRAMIENTO`.

### Productos sin SKU

- ID `28389`: borrador sin nombre y sin SKU;
- ID `29376`: Banco Cubo, privado y sin SKU.

### Productos sin categoría

Cinco productos privados de velarias permanecen sin relación de categoría:

- ID `6674`;
- ID `6691`;
- ID `6693`;
- ID `6697`;
- ID `6699`.

## Actualización de la fuente canónica

`data/current` se actualizó con el snapshot de producción del 22 de julio de 2026.

La actualización fue validada mediante:

- checksums SHA-256;
- comparación binaria de los archivos de datos;
- unicidad de IDs;
- consistencia de estados;
- integridad de relaciones;
- existencia de categorías;
- comparación del resumen declarado con los conteos calculados.

Resultado:

    CURRENT_VALIDATION_OK

## Acciones no realizadas

Durante esta auditoría no se realizaron:

- modificaciones en WordPress;
- cambios en productos;
- eliminación de registros;
- corrección del SKU duplicado;
- creación de productos;
- creación o eliminación de categorías;
- cambios de slug;
- despliegues;
- modificaciones en producción;
- modificaciones en staging.

## Próximas acciones

1. revisar y resolver el SKU duplicado `EJE-EST-10-00`;
2. determinar el destino del borrador vacío `28389`;
3. validar el producto Banco Cubo;
4. revisar las cinco velarias sin categoría;
5. confirmar `BAN-00-15-00`;
6. confirmar `SVC-NEG`;
7. definir el proceso de cambios desde el repositorio hacia staging;
8. automatizar las exportaciones y validaciones;
9. crear pruebas de consistencia para pull requests;
10. revisar y fusionar la rama de conciliación.
