# Productos Jumbo Data

Repositorio canónico para organizar, auditar y mantener la información estructurada y los medios asociados al catálogo de Productos Jumbo.

## Objetivo

Este repositorio centraliza la información pública, comercial y técnica de los productos administrados en WordPress y WooCommerce.

Sus objetivos principales son:

- conservar una versión verificable del catálogo;
- conocer el número exacto de productos y sus estados;
- mantener nombres, SKU, categorías y relaciones;
- registrar cambios históricos mediante snapshots;
- comparar producción y staging;
- detectar productos duplicados o incompletos;
- documentar equivalencias entre SKU históricos y vigentes;
- relacionar productos con segmentos comerciales;
- conservar las imágenes asociadas a los productos con trazabilidad;
- preparar modificaciones antes de aplicarlas en WordPress;
- mantener trazabilidad mediante Git y Git LFS.

## Fuente de verdad

La fuente canónica de datos estructurados es:

    data/current/

Producción continúa siendo el sistema operativo que sirve el catálogo público, pero sus cambios no deben incorporarse automáticamente como verdad canónica sin una extracción, revisión y validación.

Los medios extraídos de producción se conservan en:

    media/production/

Esta capa documenta los archivos asociados al catálogo, pero no sustituye la fuente canónica de productos, categorías ni relaciones almacenada en `data/current`.

El flujo objetivo es:

1. proponer o registrar el cambio en este repositorio;
2. revisar el impacto en datos, SKU, categorías y medios;
3. aplicar y validar el cambio en staging;
4. desplegarlo de forma controlada en producción;
5. generar una nueva extracción de producción;
6. comprobar que producción y `data/current` sean consistentes;
7. actualizar el inventario de medios cuando corresponda;
8. conservar el estado anterior como snapshot inmutable.

Durante la transición al modelo gobernado por datos, las modificaciones que ya existan en producción deberán extraerse y conciliarse antes de actualizar `data/current`.

## Estado actual

### Catálogo canónico

Última actualización canónica:

- fecha del snapshot: 2026-07-22;
- entorno de origen: producción;
- URL: https://www.productosjumbo.com;
- productos totales: 542;
- productos publicados: 489;
- productos borrador: 18;
- productos privados: 35;
- productos pendientes: 0;
- categorías: 74;
- categorías raíz: 8;
- relaciones producto-categoría: 627;
- productos sin categoría: 5.

El resumen completo se encuentra en:

    data/current/catalog-summary.json

### Medios de producción

Última extracción de medios:

- fecha: 2026-07-23;
- entorno de origen: producción;
- productos analizados: 542;
- productos con medios: 539;
- productos sin medios: 3;
- imágenes descargadas: 880;
- objetos binarios únicos en Git LFS: 872;
- relaciones únicas producto-imagen: 960;
- tamaño validado de imágenes: 204.73 MB;
- imágenes faltantes: 0;
- errores de punteros Git LFS: 0.

El inventario completo identificó también 185 PDF, 175 ZIP y una referencia sin tipo reconocido. Estos archivos fueron documentados, pero no descargados en esta fase.

Los resúmenes principales se encuentran en:

    media/production/reports/media-summary.json
    media/production/reports/lfs-validation.json
    media/production/reports/download-summary.json

## Identificadores

### SKU

El SKU es la llave comercial principal para comparar productos entre fuentes y entornos.

Puede existir un SKU histórico o comercial diferente del SKU actualmente almacenado en WooCommerce. Estas equivalencias se documentan en:

    data/commercial/current/sku-aliases.tsv

### ID de WordPress

El ID de WordPress identifica técnicamente un registro dentro de una base de datos concreta.

Los IDs no deben utilizarse como llave universal entre producción y staging, porque un mismo producto puede tener IDs distintos en cada entorno.

### Nombre y slug

El nombre es un atributo descriptivo y puede cambiar.

El slug forma parte de la URL y debe modificarse únicamente mediante un proceso controlado, debido al riesgo de romper enlaces o posicionamiento.

### Ruta de medios

La ruta relativa dentro de `wp-content/uploads` identifica la ubicación original de cada archivo en WordPress.

Las relaciones entre producto, SKU, adjunto, función del medio y ruta se documentan mediante inventarios TSV. El hash SHA-256 identifica el contenido binario y permite detectar archivos duplicados aunque tengan rutas diferentes.

## Estructura del repositorio

    productosjumbo-data/
    ├── README.md
    ├── data/
    │   ├── current/
    │   ├── commercial/
    │   │   └── current/
    │   ├── reports/
    │   ├── snapshots/
    │   └── sources/
    ├── docs/
    ├── media/
    │   └── production/
    │       ├── uploads/
    │       ├── inventory/
    │       ├── reports/
    │       └── README.md
    └── taxonomy/

## Directorios

### `data/current`

Versión canónica consolidada del catálogo.

Contiene:

- resumen del catálogo;
- productos;
- estados;
- categorías;
- categorías raíz;
- relaciones producto-categoría;
- términos de visibilidad;
- productos sin categoría;
- checksums de integridad.

### `data/snapshots`

Exportaciones fechadas e inmutables.

Cada entorno se conserva por separado, por ejemplo:

    data/snapshots/2026-07-22/production/
    data/snapshots/2026-07-22/staging/

Los snapshots no deben editarse después de su incorporación.

### `data/commercial/current`

Capa comercial reconciliada con el catálogo canónico.

Contiene:

- relaciones producto-sector;
- SKU históricos o alternativos;
- productos comerciales resueltos;
- productos pendientes de validación;
- resumen de conciliación.

Los sectores comerciales no sustituyen las categorías de WooCommerce. Son dimensiones independientes.

### `data/sources`

Archivos externos utilizados como evidencia.

Cada fuente debe conservar:

- archivo original;
- versión normalizada;
- fecha;
- checksums;
- reporte de conciliación.

### `data/reports`

Reportes de auditoría, integridad, diferencias y calidad.

Los reportes fechados explican cómo se obtuvo una versión de `data/current`.

### `media/production`

Copia auditada de los medios asociados a productos en producción.

Contiene:

- `uploads/`: imágenes conservando la ruta relativa original de WordPress;
- `inventory/`: relaciones producto-imagen, rutas, adjuntos, funciones y checksums;
- `reports/`: métricas de extracción, archivos faltantes y validaciones;
- `README.md`: guía operativa de la capa de medios.

Los archivos dentro de `uploads/` se administran mediante Git LFS. Para obtener los binarios después de clonar el repositorio:

    git lfs install
    git lfs pull

Los archivos principales para consultar la relación entre productos e imágenes son:

    media/production/inventory/product-image-map.tsv
    media/production/inventory/product-image-summary.tsv
    media/production/inventory/image-product-relations.tsv
    media/production/inventory/image-checksums.tsv

### `docs`

Documentación técnica y operativa de auditorías, conciliaciones, decisiones y procesos de actualización.

### `taxonomy`

Información de taxonomías de producción y propuestas de organización curada.

## Información por producto

El modelo permite relacionar cada producto con:

- SKU canónico;
- SKU históricos o alternativos;
- ID de producción;
- ID de staging;
- nombre;
- slug;
- estado;
- categorías;
- sectores comerciales;
- URL pública;
- descripción principal;
- descripción corta;
- especificaciones;
- imagen principal;
- galería;
- adjuntos;
- ficha técnica;
- plano o dibujo 2D;
- documentos adicionales;
- fecha de creación;
- fecha de modificación;
- fecha de verificación.

La capa de medios distingue, entre otras, las siguientes relaciones:

- `featured_image`;
- `gallery_image`;
- `parented_attachment`;
- `content_url`;
- referencias de ficha técnica y dibujo 2D.

## Flujo de actualización

Toda actualización debe seguir estas fases:

1. crear una rama específica;
2. obtener snapshots de producción y staging;
3. generar el inventario de medios cuando el alcance lo requiera;
4. validar checksums;
5. comparar por SKU;
6. revisar altas, bajas, duplicados y cambios;
7. revisar imágenes, adjuntos y referencias rotas;
8. incorporar fuentes externas sin sobrescribir datos automáticamente;
9. documentar alias y decisiones;
10. actualizar `data/current`;
11. actualizar la capa de medios sin duplicar archivos por producto;
12. ejecutar validaciones estructurales y de Git LFS;
13. revisar el diff;
14. crear commits temáticos;
15. abrir un pull request;
16. validar antes de fusionar.

## Reglas de conciliación

- No asumir que dos productos son iguales solo porque comparten nombre.
- No asumir que dos productos son distintos solo porque tienen IDs diferentes.
- No reemplazar SKU sin conservar trazabilidad.
- No convertir sectores comerciales en categorías de WooCommerce.
- No eliminar productos por no aparecer en una fuente externa.
- No crear productos automáticamente a partir de una hoja de cálculo.
- No duplicar una imagen física por cada producto que la utiliza.
- No eliminar un medio únicamente porque su `post_parent` no corresponda al producto actual.
- Toda equivalencia debe tener evidencia y nivel de confianza.
- Los casos ambiguos deben permanecer pendientes hasta su validación.
- Los medios descargados deben conservar su ruta relativa, tamaño y hash SHA-256.

## Anomalías conocidas

Actualmente se conservan las siguientes anomalías de producción:

- SKU duplicado `EJE-EST-10-00` en los productos 32320 y 32423;
- producto 28389 sin nombre ni SKU, en borrador;
- producto 29376, Banco Cubo, sin SKU y en estado privado;
- cinco productos privados de velarias sin categoría;
- producto `PPR1-2-1`, Jumbo Rubber Sport Tipo Tartan A 13 mm, sin medios asociados;
- seis referencias no gráficas faltantes: PDF, ZIP o ruta sin extensión;
- dos registros de la fuente comercial pendientes:
  - `BAN-00-15-00`, Banca Tubular, sin evidencia en WooCommerce;
  - `SVC-NEG`, Home Top-It, sin equivalencia confirmada.

Los detalles de medios faltantes se encuentran en:

    media/production/reports/missing-media.tsv

Estas anomalías deben documentarse y corregirse mediante tareas separadas. No deben resolverse modificando directamente los snapshots ni ocultando registros del inventario.

## Seguridad

Este repositorio no debe contener:

- datos personales de clientes;
- usuarios de WordPress;
- pedidos;
- cotizaciones;
- prospectos de CRM;
- sesiones;
- contraseñas;
- tokens;
- claves privadas;
- archivos `wp-config.php`;
- respaldos completos de producción;
- bases de datos SQL sin sanear;
- archivos multimedia ajenos al catálogo de productos.

Antes de incorporar medios debe comprobarse que sean materiales públicos o técnicos del catálogo y que no incluyan información personal, confidencial o credenciales.

## Documentación

La auditoría y conciliación del catálogo del 22 de julio de 2026 se encuentra en:

    docs/catalog-reconciliation-2026-07-22.md

La extracción, asociación y validación de medios de producción del 23 de julio de 2026 se encuentra en:

    docs/product-media-production-2026-07-23.md

La guía específica de la capa de medios se encuentra en:

    media/production/README.md
