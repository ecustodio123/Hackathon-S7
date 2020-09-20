from connection.conn import Conexion

class Profesor_final:
    def __init__(self):
        self.model = Conexion('profesor_final')

    def guardar_profesor_final(self, profesor_final):
        return self.model.insert(profesor_final)

    def obtener_profesor_final(self, id_profesor_final):
        return self.model.get_by_id(id_profesor_final)

    def obtener_profesores_final(self, order):
        return self.model.get_all(order)

    def buscar_profesores_final(self, data_profesor_final):
        return self.model.get_by_column(data_profesor_final)

    def modificar_profesor(self, id_profesor_final, data_profesor_final):
        return self.model.update(id_profesor_final, data_profesor_final)

    def eliminar_profesor(self, id_profesor_final):
        return self.model.delete(id_profesor_final)
