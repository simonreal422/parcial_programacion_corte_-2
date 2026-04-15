from limpieza import limpiar_datos
from database import crear_conexion, crear_tablas
import pandas as pd

# 1. LIMPIAR
df_productos, df_clientes, df_proveedores = limpiar_datos()

# 2. EXPORTAR CSV LIMPIOS
df_productos.to_csv("parcial_2_productos_limpios.csv", index=False)
df_clientes.to_csv("parcial_2_clientes_limpios.csv", index=False)
df_proveedores.to_csv("parcial_2_proveedores_limpios.csv", index=False)

# 3. BASE DE DATOS
conn = crear_conexion()
crear_tablas(conn)

# 4. INSERTAR
df_productos.to_sql("productos", conn, if_exists="append", index=False)
df_clientes.to_sql("clientes", conn, if_exists="append", index=False)
df_proveedores.to_sql("proveedores", conn, if_exists="append", index=False)

# 5. VENTAS
cursor = conn.cursor()

cursor.executemany("""
INSERT INTO ventas (id_cliente, id_producto, id_proveedor, cantidad)
VALUES (?, ?, ?, ?)
""", [
    (1,1,1,2),
    (2,2,2,1),
    (3,3,3,4)
])

conn.commit()

# 6. JOIN
query = """
SELECT c.nombre_cliente, p.nombre_producto, pr.nombre_empresa, v.cantidad
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON v.id_producto = p.id_producto
JOIN proveedores pr ON v.id_proveedor = pr.id_proveedor
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()