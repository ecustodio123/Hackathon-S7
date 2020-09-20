from connection.conn import Conexion

class Nota_final:
    def __init__(self):
        self.model = Conexion('notas_final')

    def guardar_nota_final(self, nota_final):
        return self.model.insert(nota_final)

    def obtener_nota_final(self, id_nota_final):
        return self.model.get_by_id(id_nota_final)

    def obtener_notas_final(self, order):
        return self.model.get_all(order)

    def buscar_notas_final(self, data_nota_final):
        return self.model.get_by_column(data_nota_final)

    def modificar_nota(self, id_nota_final, data_nota_final):
        return self.model.update(id_nota_final, data_nota_final)

    def eliminar_nota(self, id_nota_final):
        return self.model.delete(id_nota_final)
