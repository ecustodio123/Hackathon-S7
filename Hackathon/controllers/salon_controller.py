from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta, input_fecha
from classes.salon import Salon

class Salon_controller():
    def __init__(self):
        self.salon = Salon()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Salones
                ===============
                ''')
                menu = ['Listar Salones', 'Buscar Salon', 'Nuevo Salon', 'Salir']
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_salones()
                elif respuesta == 2:
                    self.buscar_salon()
                elif respuesta == 3:
                    self.insertar_salon()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_salones(self):
        print('''
        ========================
            Lista de Salones
        ========================
        ''')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['ID', 'Nombre del Salón']))
        input("\nPresione una tecla para continuar...")

    def buscar_salon(self):
        print('''
        =====================
            Buscar Salon
        =====================
        ''')
        try:
            id_salon = input_data("Ingrese el ID del Salon >> ", "int")
            salon = self.salon.obtener_salon({'id_salon': id_salon})
            print(print_table(salon, ['ID', 'Nombre del Salón']))
            if salon:
                if pregunta("¿Deseas dar mantenimiento al salón?"):
                    opciones = ['Editar salón', 'Eliminar salón', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_salon(id_salon)
                    elif respuesta == 2:
                        self.eliminar_salon(id_salon)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_salon(self):
        nombre = input_data("Ingrese el nombre del Salón >> ")

        self.salon.guardar_salon({
            'nombre_salon': nombre
        })
        print('''
        ==============================
            Nuevo Salón agregado !
        ==============================
        ''')
        self.listar_salones()

    def editar_salon(self, id_salon):
        nombre = input_data("Ingrese el nuevo nombre del salón >> ")
        self.salon.modificar_salon({
            'id_salon': id_salon
        }, {
            'nombre_salon': nombre
        })
        print('''
        ========================
            Salón Editado !
        ========================
        ''')

    def eliminar_salon(self, id_salon):
        self.salon.eliminar_salon({
            'id_salon': id_salon
        })
        print('''
        ========================
            Salón Eliminado !
        ========================
        ''')
