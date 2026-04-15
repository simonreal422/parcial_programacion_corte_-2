
# Parcial Final Corte 2 - Cafetería U. Sabana

 

### Mateo Perez, Diego Limas, Simon Restrepo

 

## Descripción

Este repositorio contiene la solución completa del parcial final del Corte 2. El proyecto toma tres datasets sucios de la cafetería, los limpia y normaliza con **Pandas**, los exporta como CSV limpios y luego los migra a una base de datos **SQLite** con una arquitectura relacional que incluye una tabla `ventas` con llaves foráneas activas.

 

## Archivos incluidos

- `parcial_final_corte_2.ipynb`: notebook documentado paso a paso.

- `parcial_2_productos_sucios.csv`

- `parcial_2_clientes_sucios.csv`

- `parcial_2_proveedores_sucios.csv`

- `parcial_2_productos_limpios.csv`

- `parcial_2_clientes_limpios.csv`

- `parcial_2_proveedores_limpios.csv`

- `parcial_2_cafeteria.db`

 

## Paso a paso realizado

1. Se generaron los **3 CSV sucios** a partir de los datos del enunciado.

2. Se cargaron los archivos en **3 DataFrames** distintos usando Pandas.

3. Se realizó limpieza de nulos, estandarización de texto y conversión de tipos de datos.

4. Se aplicó **1NF** separando columnas compuestas:

   - `producto_categoria` -> `nombre_producto`, `categoria`

   - `cliente_tipo` -> `nombre_cliente`, `tipo_cliente`

   - `empresa_ciudad` -> `nombre_empresa`, `ciudad`

5. Se aplicó **3NF** eliminando `edad` en clientes, ya que es un dato derivado de `fecha_nacimiento`.

6. Se exportaron los **3 CSV limpios**.

7. Se creó la base de datos `parcial_2_cafeteria.db`.

8. Se cargaron los DataFrames limpios a SQLite utilizando `df.to_sql()`.

9. Se creó la tabla `ventas` con:

   - `id_venta` como PK autoincremental

   - `id_cliente`, `id_producto`, `id_proveedor` como FK

10. Se ejecutaron operaciones CRUD:

    - **INSERT** de 5 ventas

    - **SELECT con INNER JOIN**

    - **UPDATE** de la venta `id_venta = 1`

    - **DELETE** de la venta `id_venta = 3`

 

## Resultado final

La base de datos queda con 4 tablas funcionales:

- `productos`

- `clientes`

- `proveedores`

- `ventas`

 

y lista para consumo en herramientas como Power BI.

