# Documentos técnicos de productos en producción — 2026-07-23

## Objetivo

Descargar, clasificar, validar y versionar los PDF y ZIP asociados con los productos del catálogo de producción, conservando todas las rutas originales y sus relaciones.

## Fuente

- entorno: producción;
- sitio: https://www.productosjumbo.com/;
- ruta de origen: `/home/dh_yiamy4/productosjumbo.com/wp-content/uploads`;
- fecha: 2026-07-23;
- productos analizados: 542.

La extracción fue de solo lectura.

## Resultado consolidado

- documentos descargados: 355;
- PDF: 183;
- ZIP: 172;
- productos relacionados: 248;
- relaciones producto-documento: 358;
- tamaño total: 164,937,502 bytes;
- tamaño total aproximado: 157.30 MB;
- referencias faltantes: 5;
- grupos con contenido duplicado: 1;
- rutas dentro de grupos duplicados: 2;
- documentos eliminados por duplicidad: 0;
- rutas originales preservadas: sí.

## Clasificación

- `technical_sheet`: 121 fichas técnicas;
- `drawing_2d`: 22 dibujos 2D en PDF;
- `drawing_2d_package`: 172 paquetes ZIP de dibujo o archivo 2D;
- `technical_pdf`: 40 PDF técnicos sin clasificación explícita.

## Ubicación

Los binarios se almacenan mediante Git LFS bajo:

    media/production/documents/uploads/

Los documentos conservan su ruta relativa original `año/mes/nombre.ext`.

## Inventarios

    media/production/documents/inventory/document-files.tsv
    media/production/documents/inventory/document-product-relations.tsv
    media/production/documents/inventory/product-document-summary.tsv
    media/production/documents/inventory/document-checksums.tsv

Cada relación puede incluir:

- ID de producto;
- SKU;
- nombre;
- estado;
- tipo documental;
- ruta original;
- ruta en el repositorio;
- ID de adjunto;
- tipos de relación;
- URL original;
- tamaño;
- SHA-256.

## Manifiestos

    media/production/documents/manifests/document-source-paths.txt
    media/production/documents/manifests/document-repository-paths.txt
    media/production/documents/manifests/source-document-summary.json

Los manifiestos permiten comparar las rutas esperadas de producción con los archivos versionados.

## Reportes

    media/production/documents/reports/download-summary.json
    media/production/documents/reports/duplicate-document-content.tsv
    media/production/documents/reports/missing-documents.tsv

## Referencias faltantes

Cinco referencias no tienen archivo físico en producción:

1. `2021/01/AEM-217A-RE-RAMPA.pdf` — SKU `REH-00-02-00`;
2. `2021/11/RPL-117-Plano-de-Excavacion-REV0.zip` — SKU `RES-00-02-00`;
3. `2022/06/AEM-217B-RE-Archivo-2D-Rev.0.zip` — SKU `REH-00-03-00`;
4. `2022/06/AEM-217B-RE-Ficha-Tecnica-REV.0.pdf` — SKU `REH-00-03-00`;
5. `2023/06/CIR-00-02-00-CONJUNTO-CALISTENIA-Plano-de-excavacion.zip` — SKU `CIR-00-02-00`.

No se generaron sustitutos ni se inventaron contenidos.

## Contenido duplicado

Se detectó un grupo con el mismo SHA-256 en dos rutas:

- `2020/12/AED-004-FORTE-PECHO.pdf`;
- `2021/01/AED-004-FORTE-PECHO.pdf`.

Ambas rutas pertenecen al SKU `EJE-FO-11-00` y fueron conservadas. Git LFS reutiliza el mismo objeto binario sin perder las rutas originales.

## Diferencia frente al inventario general de medios

El inventario inicial registró 185 referencias PDF y 175 ZIP. Esta colección contiene 183 PDF y 172 ZIP porque las cinco referencias anteriores no existen físicamente.

La sexta referencia faltante del inventario general es una ruta sin extensión asociada con `COL-AB-03-00`; no se clasificó como PDF o ZIP y no forma parte de esta colección.

## Git LFS

Regla:

    media/production/documents/uploads/** filter=lfs diff=lfs merge=lfs -text

Después de clonar:

    git lfs install
    git lfs pull

## Validaciones realizadas

- 355 rutas esperadas y 355 archivos descargados;
- 183 PDF y 172 ZIP;
- tamaños físicos iguales al inventario fuente;
- SHA-256 generado para cada archivo;
- `SHA256SUMS` validado;
- atributos Git LFS correctos;
- 355 punteros LFS válidos;
- OID y tamaño de cada puntero iguales al inventario;
- estructura regular de todos los TSV;
- 358 relaciones válidas con productos;
- cinco faltantes documentados;
- duplicados conservados;
- cero archivos adicionales;
- cero eliminaciones automáticas.

## Política de conservación

- No eliminar documentos por compartir nombre, tamaño o hash.
- No renombrar rutas originales sin una migración documentada.
- No sustituir referencias faltantes con archivos similares.
- No editar snapshots o inventarios para esconder anomalías.
- Toda actualización debe regenerar relaciones, checksums y reportes.

## Seguridad

No se modificó WordPress, WooCommerce, staging ni producción. La colección no incluye pedidos, clientes, cotizaciones, credenciales ni respaldos de bases de datos.
