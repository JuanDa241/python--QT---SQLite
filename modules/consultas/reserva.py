from ..conexion import Conexion

#Consultas para Inventario

#Clase Reservas
class Reservas():
    def __init__(self, cantidad, estado, referenciaProducto):
        self.Cantidad = cantidad
        self.Estado = estado
        self.ReferenciaProducto = referenciaProducto

    def __str__(self):
        return f"reservas[{self.Cantidad},'{self.Estado}',{self.ReferenciaProducto}]"

#Ingresar una nueva Reserva
def crearReserva(Reservas):
    con = Conexion()

    sql = f'''
            INSERT INTO reserva(cantidad, estado, referenciaProducto)
            VALUES({Reservas.Cantidad},'{Reservas.Estado}',{Reservas.ReferenciaProducto})
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo='Reservas'
        texto='No se ha podido crear una nueva reserva'
        print(titulo,texto)

#Mostrar la informacion de las reservas
def mostrarReservas():
    con = Conexion()
    lista = []

    sql = '''
        SELECT R.idReserva, I.producto, R.cantidad, R.estado
        FROM reserva R
        INNER JOIN inventario I
        ON R.referenciaProducto = I.referencia

    '''
    try:
        lista = con.conexion.execute(sql)
        datos = lista.fetchall()
        con.CloseConexion()
        return datos
    except:
        titulo = 'Reservas'
        texto = 'No se encontraron reservas'
        print(titulo,texto)

#Actualizar la informacion de una reserva
def actualizarReserva(Reservas, idReserva):
    con = Conexion()

    sql = f'''
            UPDATE reserva
            SET cantidad = {Reservas.Cantidad}, estado = '{Reservas.Estado}', referenciaProducto = {Reservas.ReferenciaProducto}
            WHERE idReserva = {idReserva}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Reservas'
        texto = 'No se ha podido actualizar la reserva'
        print(titulo,texto)

#Eliminar una reserva
def eliminarReservas(idReserva):
    con = Conexion()

    sql = f'''
            DELETE FROM reserva
            WHERE reserva = {idReserva}
    '''
    try:
        con.conexion.execute(sql)
        con.CloseConexion()
    except:
        titulo = 'Reservas'
        texto = 'No se ha podido eliminar la reserva'
        print(titulo,texto)