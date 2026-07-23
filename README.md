# Productos Jumbo Data

Repositorio canónico para organizar, auditar y mantener la información estructurada, comercial, editorial y multimedia del catálogo de Productos Jumbo.

## Objetivo

Este repositorio centraliza información pública y técnica de los productos administrados en WordPress y WooCommerce para:

- conservar una versión verificable del catálogo;
- mantener nombres, SKU, estados, categorías y relaciones;
- documentar alias históricos y sectores comerciales;
- versionar descripciones y especificaciones normalizadas;
- conservar imágenes y documentos técnicos con trazabilidad;
- detectar anomalías, faltantes y duplicados;
- comparar producción y staging;
- preparar cambios antes de aplicarlos en WordPress;
- mantener historial mediante Git y Git LFS.

## Fuentes de verdad

La fuente canónica de datos estructurados es:

    data/current/

Producción continúa siendo el sistema operativo que sirve el catálogo público. Sus cambios deben extraerse, conciliarse y validarse antes de actualizar la versión canónica.

Los activos extraídos de producción se conservan en:

    media/production/

Esta capa complementa a `data/current`; no sustituye los datos canónicos de productos, estados, SKU ni categorías.

## Estado consolidado

### Catálogo canónico

Fuente: producción  
Snapshot: 2026-07-22

- productos totales: 542;
- publicados: 489;
- borradores: 18;
- privados: 35;
- pendientes: 0;
- categorías: 74;
- categorías raíz: 8;
- relaciones producto-categoría: 627;
- productos sin categoría: 5.

Resumen:

    data/current/catalog-summary.json

### Contenido y especificaciones

Extracción y normalización: 2026-07-23

- productos con descripción normalizada: 178;
- productos sin descripción: 364;
- productos con especificaciones estructuradas: 443;
- productos sin especificaciones estructuradas: 99;
- filas de especificaciones: 1,910;
- productos que requieren revisión manual: 32;
- productos con brechas de contenido: 403;
- fragmentos sin interpretar: 0;
- incidencias conservadas de los datos fuente: 7.

Archivos canónicos:

    data/current/product-content.tsv
    data/current/product-content-summary.json
    data/current/product-specifications.tsv
    data/current/specification-dictionary.tsv

El contenido original de WordPress permanece en:

    data/snapshots/2026-07-23/production/content/

### Imágenes de producción

Extracción: 2026-07-23

- productos analizados: 542;
- productos con medios: 539;
- productos sin medios: 3;
- imágenes descargadas: 880;
- objetos binarios únicos en Git LFS: 872;
- relaciones únicas producto-imagen: 960;
- tamaño validado: 204.73 MB;
- imágenes faltantes: 0;
- errores de punteros Git LFS: 0.

Ubicación:

    media/production/uploads/

Inventarios principales:

    media/production/inventory/product-image-map.tsv
    media/production/inventory/product-image-summary.tsv
    media/production/inventory/image-product-relations.tsv
    media/production/inventory/image-checksums.tsv

### Documentos técnicos

Extracción y descarga: 2026-07-23

- documentos descargados: 355;
- PDF: 183;
- ZIP: 172;
- productos relacionados: 248;
- relaciones producto-documento: 358;
- tamaño validado: 157.30 MB;
- referencias faltantes: 5;
- grupos de contenido duplicado: 1;
- rutas dentro de grupos duplicados: 2;
- archivos eliminados por duplicidad: 0.

Clasificación:

- fichas técnicas: 121;
- dibujos 2D en PDF: 22;
- paquetes de dibujo o archivo 2D: 172;
- PDF técnicos sin clasificación explícita: 40.

Ubicación:

    media/production/documents/uploads/

Inventarios y reportes:

    media/production/documents/inventory/
    media/production/documents/reports/

El inventario general original registró 185 referencias PDF y 175 ZIP. La colección descargada contiene 183 PDF y 172 ZIP porque cinco referencias no tienen archivo físico en producción; la sexta referencia faltante del inventario general es una ruta sin extensión y no forma parte de la colección documental clasificada.

## Estructura del repositorio

    productosjumbo-data/
    ├── data/
    │   ├── current/
    │   ├── commercial/current/
    │   ├── reports/
    │   ├── snapshots/
    │   └── sources/
    ├── docs/
    ├── media/
    │   └── production/
    │       ├── uploads/
    │       ├── inventory/
    │       ├── reports/
    │       └── documents/
    │           ├── uploads/
    │           ├── inventory/
    │           ├── manifests/
    │           └── reports/
    ├── scripts/
    └── taxonomy/

## Directorios principales

### `data/current`

Versión canónica consolidada del catálogo, contenido y especificaciones.

### `data/snapshots`

Exportaciones fechadas e inmutables. Los snapshots no deben editarse después de su incorporación.

### `data/commercial/current`

Capa comercial reconciliada: sectores, alias de SKU, productos resueltos y casos pendientes.

### `data/sources`

Fuentes externas originales y normalizadas utilizadas como evidencia.

### `data/reports`

Reportes de auditoría, integridad, diferencias, contenido y calidad.

### `media/production`

Copia auditada de imágenes asociadas con productos, conservando las rutas relativas originales de WordPress.

### `media/production/documents`

PDF y ZIP técnicos asociados con productos, con inventarios, relaciones, manifiestos y checksums independientes.

### `docs`

Documentación técnica y operativa de extracciones, conciliaciones y decisiones.

### `scripts`

Herramientas reproducibles para extracción, generación de índices, normalización y validación.

## Identificadores y relaciones

### SKU

El SKU es la llave comercial principal. Los SKU históricos o alternativos se documentan en:

    data/commercial/current/sku-aliases.tsv

### ID de WordPress

Es un identificador técnico específico de una base de datos. No debe utilizarse como llave universal entre producción y staging.

### Ruta de medios

La ruta relativa dentro de `wp-content/uploads` conserva la ubicación original. El SHA-256 identifica el contenido y permite detectar duplicados aunque existan en rutas diferentes.

### Relaciones de medios

Entre otras, se registran:

- `featured_image`;
- `gallery_image`;
- `parented_attachment`;
- `content_url`;
- ficha técnica;
- dibujo o archivo 2D.

## Git LFS

Las imágenes y documentos binarios se administran mediante Git LFS.

Después de clonar:

    git lfs install
    git lfs pull

No debe sustituirse un puntero LFS por contenido binario directo ni retirarse una ruta duplicada sin revisar sus relaciones.

## Flujo de actualización

1. actualizar `main` y crear una rama específica;
2. extraer snapshots o inventarios en modo solo lectura;
3. comparar IDs técnicos y SKU comerciales;
4. validar conteos, esquemas y checksums;
5. revisar altas, bajas, duplicados, faltantes y cambios;
6. conservar las fuentes originales;
7. actualizar tablas canónicas e inventarios derivados;
8. descargar únicamente activos nuevos o modificados;
9. conservar rutas originales y relaciones;
10. validar Git LFS, tamaños, OID y SHA-256;
11. actualizar la documentación;
12. revisar el diff y escanear información sensible;
13. abrir un pull request;
14. fusionar mediante squash después de validar.

## Reglas de conciliación

- No asumir equivalencia solo por nombre.
- No asumir diferencia solo por ID.
- No reemplazar SKU sin conservar trazabilidad.
- No convertir sectores comerciales en categorías de WooCommerce.
- No eliminar productos por no aparecer en una fuente externa.
- No inventar descripciones, especificaciones ni documentos faltantes.
- No duplicar un archivo físico por cada producto relacionado.
- No eliminar una ruta únicamente por compartir contenido con otra.
- Los casos ambiguos deben conservarse para revisión manual.
- Los binarios deben conservar ruta, tamaño y SHA-256.

## Anomalías conocidas

- SKU duplicado `EJE-EST-10-00` en los productos 32320 y 32423;
- producto 28389 sin nombre ni SKU, en borrador;
- producto 29376, Banco Cubo, sin SKU y privado;
- cinco productos privados de velarias sin categoría;
- producto `PPR1-2-1` sin medios asociados;
- cinco referencias documentales sin archivo físico;
- una referencia adicional sin extensión en el inventario general de medios;
- dos registros comerciales pendientes:
  - `BAN-00-15-00`, Banca Tubular;
  - `SVC-NEG`, Home Top-It.

Estas anomalías deben resolverse mediante tareas separadas, sin modificar snapshots ni ocultar registros.

## Seguridad

Este repositorio no debe contener:

- datos personales de clientes;
- usuarios, sesiones, pedidos o cotizaciones;
- prospectos de CRM;
- contraseñas, tokens o claves privadas;
- archivos `wp-config.php`;
- respaldos completos de producción;
- bases de datos SQL sin sanear;
- activos ajenos al catálogo.

## Documentación

    docs/catalog-reconciliation-2026-07-22.md
    docs/product-content-production-2026-07-23.md
    docs/product-media-production-2026-07-23.md
    docs/product-documents-production-2026-07-23.md
    media/production/README.md
    media/production/documents/README.md
