import sqlite3

def crear_conexion():
    return sqlite3.connect("parcial_2_cafeteria.db")


def crear_tablas(conn):
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DROP TABLE IF EXISTS ventas")
    cursor.execute("DROP TABLE IF EXISTS clientes")
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute("DROP TABLE IF EXISTS proveedores")

    cursor.execute("""
    CREATE TABLE productos (
        id_producto INTEGER PRIMARY KEY,
        nombre_producto TEXT,
        categoria TEXT,
        precio REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE clientes (
        id_cliente INTEGER PRIMARY KEY,
        nombre_cliente TEXT,
        tipo_cliente TEXT,
        telefono TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE proveedores (
        id_proveedor INTEGER PRIMARY KEY,
        nombre_empresa TEXT,
        ciudad TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_producto INTEGER,
        id_proveedor INTEGER,
        cantidad INTEGER
    )
    """)

    conn.commit()