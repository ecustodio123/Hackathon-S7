from connection.conn import Conexion

class Alumno_final:
    def __init__(self):
        self.model = Conexion('alumnos_final')

    def guardar_alumno_final(self, alumno_final):
        return self.model.insert(alumno_final)

    def obtener_alumno_final(self, id_alumno_final):
        return self.model.get_by_id(id_alumno_final)

    def obtener_alumnos_final(self, order):
        return self.model.get_all(order)

    def buscar_alumnos_final(self, data_alumno_final):
        return self.model.get_by_column(data_alumno_final)

    def modificar_alumno(self, id_alumno_final, data_alumno_final):
        return self.model.update(id_alumno_final, data_alumno_final)

    def eliminar_alumno(self, id_alumno_final):
        return self.model.delete(id_alumno_final)
