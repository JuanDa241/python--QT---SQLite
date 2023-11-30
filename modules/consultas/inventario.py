from ..conexion import Conexion

#Consultas para Inventario

#Clase Productos
class Productos:
    def __init__(self, producto, precio, categoria, stock, proveedor):
        self.Producto = producto
        self.Precio = precio
        self.Categoria = categoria
        self.Stock = stock
        self.Proveedor = proveedor

    def __str__(self):
        return f"productos['{self.Producto}',{self.Precio},'{self.Categoria}',{self.Stock},{self.Proveedor}]"

#Ingresar un producto al inventario
def crearProducto(Productos):
    con = Conexion()

    sql = f'''
            INSERT INTO inventario(producto, precio, categoria, stock, idProveedor)
            VALUES('{Productos.Producto}',{Productos.Precio},'{Productos.Categoria}',{Productos.Stock},{Productos.Proveedor})
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Inventario'
        texto = 'No se puede ingresar el producto al inventario'
        print(titulo,texto)

#Mostrar la informacion del inventario
def mostrarInventario():
    con = Conexion()
    lista = []

    sql = '''
        SELECT I.referencia, I.producto, I.precio, I.categoria, I.stock, P.nombre
        FROM inventario I
        INNER JOIN proveedor P
        ON I.idProveedor = P.idProveedor
    '''

    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Inventario'
        texto = 'No se encontro elementos en el inventario'
        print(titulo,texto)

#Actualizar un producto del inventario
def actualizarProdcuto(Productos, referencia):
    con = Conexion()

    sql = f'''
            UPDATE inventario
            SET producto = '{Productos.Producto}', precio = '{Productos.Precio}', categoria = '{Productos.Categoria}', stock = {Productos.Stock}, idProveedor = {Productos.Proveedor}
            WHERE referencia = {referencia}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Inventario'
        texto = 'No se ha podido actualizar el prodcuto'
        print(titulo,texto)

#Eliminar un producto del inventario
def eliminarProducto(referencia):
    con = Conexion()

    sql = f'''
            DELETE FROM inventario
            WHERE referencia = {referencia}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Inventario'
        texto = 'No se ha podido eliminar el prodcuto del inventario'
        print(titulo,texto)

    #Mostrar referencia y nombre del producto
def mostrarIdNombre():
    con = Conexion()
    lista = []

    sql = '''
        SELECT referencia, producto
        FROM inventario 
    '''

    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Inventario'
        texto = 'No se encontro elementos en el inventario'

#editar Stock cuando se hace un despacho:

def editarStock(cantidad, nombre):
    con = Conexion()

    sql = f''' 
            UPDATE inventario
            SET stock = stock - {cantidad}
            WHERE referencia = {nombre}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Inventario'
        texto = 'No se ha podido editar el stock'
        print(titulo,texto)
    
#Mostrar stock disponible

def mostrarStock(Referencia):
    con = Conexion()

    lista = []

    sql = f'''
    SELECT stock 
    FROM inventario 
    WHERE referencia = {Referencia}
    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchone()
        con.CloseConexion()
        return datos[0]
    except:
        titulo = 'Inventario'
        texto = 'No se encontro stock'
   

    