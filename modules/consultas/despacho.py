from ..conexion import Conexion


#Consultas para Inventario

#Clase Despacho
class Despachos():
    def __init__(self, cantidad, fecha, referenciaProducto, cedulaCliente):
        
        self.Cantidad = cantidad
        self.Fecha = fecha
        self.ReferenciaProducto = referenciaProducto
        self.CedulaCliente = cedulaCliente

    def __str__(self):
        return f"despachos[{self.Cantidad},'{self.Fecha}',{self.ReferenciaProducto},{self.CedulaCliente}]"

#Ingresar una nueva Reserva
def crearDespachos(Despachos):
    con = Conexion()

    sql = f'''
            INSERT INTO despacho(Cantidad, fecha, referenciaProducto, cedulaCliente)
            VALUES({Despachos.Cantidad},'{Despachos.Fecha}',{Despachos.ReferenciaProducto},{Despachos.CedulaCliente})
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo='Despachos'
        texto='No se ha podido crear un nuevo despacho'
        print(titulo,texto) 

#Mostrar la informacion de los despachos
def mostrarDespachos():
    con = Conexion()
    lista = []

    sql = '''
        SELECT D.codigo, C.nombre, I.producto, D.Cantidad, D.Fecha
        FROM despacho D
        INNER JOIN cliente C
        ON D.cedulaCliente = C.cedula
        INNER JOIN inventario I
        ON D.referenciaProducto = I.referencia
    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Despachos'
        texto = 'No se encontraron despachos'
        print(titulo,texto)

#Actualizar la informacion de un despacho
def actualizarDespachos(Despachos, codigo):
    con = Conexion()

    sql = f'''
            UPDATE despacho
            SET Cantidad = {Despachos.Cantidad},'{Despachos.Fecha}',{Despachos.ReferenciaProducto},{Despachos.CedulaCliente}
            WHERE Codigo = {codigo}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Despachos'
        texto = 'No se ha podido actualizar el despacho'
        print(titulo,texto)

#Eliminar una reserva
def eliminarDespachos(codigo):
    con = Conexion()

    sql = f'''
            DELETE FROM despacho
            WHERE Codigo = {codigo}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Despachos'
        texto = 'No se ha podido eliminar el despacho'
        print(titulo,texto)