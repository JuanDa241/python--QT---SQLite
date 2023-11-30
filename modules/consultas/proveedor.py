from ..conexion import Conexion

#Consultas para Inventario

#Clase Proveedor
class Proveedores():
    def __init__(self, nombre, telefono, direccion, precio):
        self.Nombre = nombre
        self.Telefono = telefono
        self.Direccion = direccion
        self.Precio = precio

    def __str__(self):
        return f"proveedores[,'{self.Nombre}','{self.Telefono}','{self.Direccion}',{self.Precio}]"

#Ingresar un nuevo Proveedor
def crearProveedor(Proveedores):
    con = Conexion()

    sql = f'''
            INSERT INTO proveedor(nombre, telefono, direccion, precioProveedor)
            VALUES('{Proveedores.Nombre}','{Proveedores.Telefono}','{Proveedores.Direccion}',{Proveedores.Precio})
    '''

    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Proveedor'
        texto = 'No se pudo crear el proveedor'
        print(titulo,texto)

#Mostrar la informacion de los proveedores
def mostrarProveedores():
    con = Conexion()
    lista = []

    sql = '''
        SELECT *
        FROM proveedor
    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Proveedor'
        texto = 'No se encontraron proveedores'
        print(titulo,texto)
        

#Actualizar la informacion de un provedor
def actualizarProveedor(Proveedores, id):
    con = Conexion()

    sql = f'''
            UPDATE proveedor
            SET nombre = '{Proveedores.Nombre}',telefono = '{Proveedores.Telefono}',direccion = '{Proveedores.Direccion}',precioProveedor = {Proveedores.Precio}
            WHERE idProveedor = {id}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
         titulo = 'Proveedor'
         texto = 'No se ha podido actualizar el proveedor'
         print(titulo,texto)

#Eliminar un proveedor
def eliminarProveedor(codigo):
    con = Conexion()

    sql = f'''
            DELETE FROM proveedor
            WHERE idProveedor = {codigo}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Proveedor'
        texto = 'No se ha podido eliminar el proveedor'
        print(titulo,texto)

#cosulta para comboBox
def mostrarNombreProveedor():
    con = Conexion()
    lista = []

    sql = '''
        SELECT idProveedor , nombre
        FROM proveedor
     
    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Proveedor'
        texto = 'No se encontro elementos del proveedor'
        print(titulo,texto)