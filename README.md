# Productos Jumbo Data

Repositorio centralizado para organizar, revisar y mantener actualizada la información del catálogo de Productos Jumbo.

## Objetivo

El objetivo de este repositorio es conservar una copia organizada, verificable y actualizada de la información pública y técnica de los productos disponibles en el sitio web de Productos Jumbo.

Este repositorio permitirá:

- conocer el número exacto de productos activos;
- registrar productos publicados, borradores y productos desactivados;
- conservar nombres, claves, categorías y URLs;
- actualizar imágenes y galerías;
- actualizar descripciones y especificaciones;
- organizar fichas técnicas;
- organizar planos y dibujos 2D;
- detectar productos con información incompleta;
- comparar cambios entre diferentes fechas;
- mantener trazabilidad mediante Git.

## Fuente de verdad

La fuente principal será el sitio de producción de Productos Jumbo y su instalación de WordPress y WooCommerce.

Cada extracción deberá registrar:

- fecha de extracción;
- entorno de origen;
- cantidad total de productos;
- cantidad de productos publicados;
- cantidad de productos borrador;
- cantidad de productos privados;
- cantidad de productos sin imagen principal;
- cantidad de productos sin descripción;
- cantidad de productos sin ficha técnica;
- cantidad de productos sin plano 2D.

## Información por producto

Cada producto deberá incluir o relacionarse con:

- ID de WordPress;
- nombre;
- slug;
- estado;
- clave o SKU;
- categoría;
- URL pública;
- descripción principal;
- descripción corta;
- especificaciones técnicas;
- imagen principal;
- galería de imágenes;
- ficha técnica;
- plano o dibujo 2D;
- documentos adicionales;
- fecha de creación;
- fecha de última modificación;
- fecha de última extracción.

## Estructura propuesta

    productosjumbo-data/
    ├── README.md
    ├── .gitignore
    ├── data/
    │   ├── current/
    │   ├── snapshots/
    │   └── reports/
    ├── products/
    ├── media/
    │   ├── images/
    │   ├── technical-sheets/
    │   ├── drawings-2d/
    │   └── documents/
    ├── scripts/
    ├── docs/
    └── backups/

## Directorios

### data/current

Contendrá la versión consolidada más reciente del catálogo.

### data/snapshots

Contendrá exportaciones fechadas para comparar cambios históricos.

### data/reports

Contendrá métricas, conteos y reportes de calidad del catálogo.

### products

Contendrá la información individual y organizada de cada producto.

### media/images

Contendrá imágenes principales y galerías de productos.

### media/technical-sheets

Contendrá fichas técnicas.

### media/drawings-2d

Contendrá planos, dibujos y vistas 2D.

### media/documents

Contendrá manuales, certificados y documentos adicionales.

### scripts

Contendrá herramientas de extracción, validación, limpieza y actualización.

### backups

Contendrá respaldos privados. Esta carpeta no debe subirse a Git.

## Principios de organización

1. Producción será la fuente principal del catálogo vigente.
2. No se modificarán directamente los archivos originales descargados.
3. Se conservarán los IDs originales de WordPress y WooCommerce.
4. Cada extracción tendrá una fecha y un origen identificables.
5. Los nombres de archivos deberán ser consistentes.
6. Las imágenes y documentos deberán estar relacionados con productos concretos.
7. Se evitarán archivos duplicados.
8. Los cambios deberán quedar registrados mediante Git.
9. No se almacenarán datos personales o comerciales de clientes.
10. No se almacenarán secretos ni respaldos completos dentro del historial de Git.

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
- archivos wp-config.php;
- respaldos completos de producción;
- bases de datos SQL sin sanear.

## Estado inicial

El repositorio se encuentra en fase de preparación.

Los siguientes pasos serán:

1. crear la estructura base de directorios;
2. obtener un inventario de productos desde producción;
3. determinar el número exacto de productos activos;
4. exportar los metadatos del catálogo;
5. identificar imágenes y documentos asociados;
6. descargar archivos multimedia;
7. generar reportes de información faltante;
8. definir un proceso periódico de actualización.

## Alcance inicial

La primera versión del repositorio se enfocará en:

- productos publicados;
- categorías;
- claves y SKU;
- descripciones;
- especificaciones;
- imágenes;
- fichas técnicas;
- planos 2D;
- documentos relacionados.

Los datos de clientes, pedidos, cotizaciones y CRM quedan fuera del alcance.
