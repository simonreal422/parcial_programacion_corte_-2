import pandas as pd

def limpiar_datos():
    df_productos = pd.read_csv("parcial_2_productos_sucios.csv")
    df_clientes = pd.read_csv("parcial_2_clientes_sucios.csv")
    df_proveedores = pd.read_csv("parcial_2_proveedores_sucios.csv")

    # PRODUCTOS
    df_productos[["nombre_producto", "categoria"]] = df_productos["producto_categoria"].str.split(" - ", expand=True)
    df_productos["precio"] = df_productos["precio"].str.replace(r"[\$,]", "", regex=True)
    df_productos["precio"] = pd.to_numeric(df_productos["precio"])

    df_productos = df_productos.drop(columns=["producto_categoria"])
    df_productos["id_producto"] = range(1, len(df_productos) + 1)

    # CLIENTES
    df_clientes[["nombre_cliente", "tipo_cliente"]] = df_clientes["cliente_tipo"].str.split(" - ", expand=True)
    df_clientes["nombre_cliente"] = df_clientes["nombre_cliente"].str.title()
    df_clientes["telefono"] = df_clientes["telefono"].fillna("Sin telefono")

    df_clientes = df_clientes.drop(columns=["cliente_tipo"])
    df_clientes["id_cliente"] = range(1, len(df_clientes) + 1)

    # PROVEEDORES
    df_proveedores[["nombre_empresa", "ciudad"]] = df_proveedores["empresa_ciudad"].str.split(" - ", expand=True)
    df_proveedores = df_proveedores.drop(columns=["empresa_ciudad"])
    df_proveedores["id_proveedor"] = range(1, len(df_proveedores) + 1)

    return df_productos, df_clientes, df_proveedores