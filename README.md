# Productos Jumbo Data

Repositorio canónico para organizar, auditar y mantener la información estructurada del catálogo de Productos Jumbo.

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
- preparar modificaciones antes de aplicarlas en WordPress;
- mantener trazabilidad mediante Git.

## Fuente de verdad

La fuente canónica de datos estructurados es:

    data/current/

Producción continúa siendo el sistema operativo que sirve el catálogo público, pero sus cambios no deben incorporarse automáticamente como verdad canónica sin una extracción, revisión y validación.

El flujo objetivo es:

1. proponer o registrar el cambio en este repositorio;
2. revisar el impacto en datos, SKU, categorías y medios;
3. aplicar y validar el cambio en staging;
4. desplegarlo de forma controlada en producción;
5. generar una nueva extracción de producción;
6. comprobar que producción y `data/current` sean consistentes;
7. conservar el estado anterior como snapshot inmutable.

Durante la transición al modelo gobernado por datos, las modificaciones que ya existan en producción deberán extraerse y conciliarse antes de actualizar `data/current`.

## Estado actual

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

### `taxonomy`

Información de taxonomías de producción y propuestas de organización curada.

## Información por producto

La evolución del modelo deberá permitir relacionar cada producto con:

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
- ficha técnica;
- plano o dibujo 2D;
- documentos adicionales;
- fecha de creación;
- fecha de modificación;
- fecha de verificación.

## Flujo de actualización

Toda actualización debe seguir estas fases:

1. crear una rama específica;
2. obtener snapshots de producción y staging;
3. validar checksums;
4. comparar por SKU;
5. revisar altas, bajas, duplicados y cambios;
6. incorporar fuentes externas sin sobrescribir datos automáticamente;
7. documentar alias y decisiones;
8. actualizar `data/current`;
9. ejecutar validaciones estructurales;
10. revisar el diff;
11. crear commits temáticos;
12. abrir un pull request;
13. validar antes de fusionar.

## Reglas de conciliación

- No asumir que dos productos son iguales solo porque comparten nombre.
- No asumir que dos productos son distintos solo porque tienen IDs diferentes.
- No reemplazar SKU sin conservar trazabilidad.
- No convertir sectores comerciales en categorías de WooCommerce.
- No eliminar productos por no aparecer en una fuente externa.
- No crear productos automáticamente a partir de una hoja de cálculo.
- Toda equivalencia debe tener evidencia y nivel de confianza.
- Los casos ambiguos deben permanecer pendientes hasta su validación.

## Anomalías conocidas

Actualmente se conservan las siguientes anomalías de producción:

- SKU duplicado `EJE-EST-10-00` en los productos 32320 y 32423;
- producto 28389 sin nombre ni SKU, en borrador;
- producto 29376, Banco Cubo, sin SKU y en estado privado;
- cinco productos privados de velarias sin categoría;
- dos registros de la fuente comercial pendientes:
  - `BAN-00-15-00`, Banca Tubular, sin evidencia en WooCommerce;
  - `SVC-NEG`, Home Top-It, sin equivalencia confirmada.

Estas anomalías deben documentarse y corregirse mediante tareas separadas. No deben resolverse modificando directamente los snapshots.

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
- bases de datos SQL sin sanear.

## Documentación

La auditoría y conciliación del 22 de julio de 2026 se encuentra en:

    docs/catalog-reconciliation-2026-07-22.md
