from ..conexion import Conexion

#Consultas para Clientes

#Clase Cliente
class Clientes():
    def __init__(self, nombre):

        self.Nombre = nombre

    def __str__(self):
        return f"clientes['{self.Nombre}']"

#Ingresar un nuevo cliente
def crearCliente(Cliente):
    con = Conexion()

    sql = f'''
            INSERT INTO cliente(nombre)
            VALUES('{Cliente.Nombre}')
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Cliente'
        texto = 'No se pudo crear el cliente'
        print(titulo,texto)

#Mostrar la informacion de los clientes
def mostrarClientes():
    con = Conexion()
    lista = []

    sql = f'''
            SELECT * 
            FROM cliente
    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Cliente'
        texto = 'No se encontraron clientes'
        print(titulo,texto)

#Actualizar la informacion de un cliente
def actualizarCliente(Clientes, cedula):
    con = Conexion()

    sql = f'''
            UPDATE cliente
            SET nombre = '{Clientes.Nombre}'
            WHERE cedula = {cedula}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Cliente'
        texto = 'No se ha podido actualizar el cliente'
        print(titulo,texto)

#Eliminar un cliente
def eliminarClieten(cedula):
    con = Conexion()

    sql = f'''
            DELETE FROM cliente
            WHERE cedula = {cedula}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Cliente'
        texto = 'No se pudo eliminar el cliente'
        print(titulo,texto)
