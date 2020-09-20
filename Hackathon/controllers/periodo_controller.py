from helpers.menu import Menu
from helpers.helper import input_data, print_table, pregunta, input_fecha
from classes.periodo import Periodo

class Periodo_controller:
    def __init__(self):
        self.periodo = Periodo()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Periodo
                ===============
                ''')
                menu = ['Listar Periodos', 'Buscar Periodo', 'Nuevo Periodo', 'Salir']
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_periodos()
                elif respuesta == 2:
                    self.buscar_periodo()
                elif respuesta == 3:
                    self.insertar_periodo()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')


    def listar_periodos(self):
        print('''
        ========================
            Lista de Periodos
        ========================
        ''')
        periodos = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodos, ['ID', 'Periodo', 'F. Inicio Periodo', 'F. Fin Periodo']))
        input("\nPresione una tecla para continuar...")

    def buscar_periodo(self):
        print('''
        =====================
            Buscar Periodo
        =====================
        ''')
        try:
            id_periodo = input_data("Ingrese el ID del Periodo >> ", "int")
            periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
            print(print_table(periodo, ['ID', 'Periodo', 'F. Inicio Periodo', 'F. Fin Periodo']))
            if periodo:
                if pregunta("¿Deseas dar mantenimiento al periodo?"):
                    opciones = ['Editar Periodo', 'Eliminar Periodo', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_periodo(id_periodo)
                    elif respuesta == 2:
                        self.eliminar_periodo(id_periodo)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_periodo(self):
        nombre = input_data("Ingrese el nombre del periodo >> ")
        print("\nIngrese los datos sobre la fecha de inicio del periodo que está registrando\n")
        fecha_inicio = input_fecha()
        print("\nIngrese los datos sobre la fecha de fin del periodo que está registrando\n")
        fecha_fin = input_fecha()

        self.periodo.guardar_periodo({
            'nombre_periodo': nombre,
            'fecha_desde': fecha_inicio,
            'fecha_hasta': fecha_fin
        })
        print('''
        ==============================
            Nuevo Periodo agregado !
        ==============================
        ''')
        self.listar_periodos()

    def editar_periodo(self, id_periodo):
        nombre = input_data("Ingrese el nuevo nombre del periodo >> ")
        print("\nIngrese los datos sobre la fecha de inicio del periodo que está registrando\n")
        fecha_inicio = input_fecha()
        print("\nIngrese los datos sobre la fecha de fin del periodo que está registrando\n")
        fecha_fin = input_fecha()
        self.periodo.modificar_periodo({
            'id_periodo': id_periodo
        }, {
            'nombre_periodo': nombre,
            'fecha_desde': fecha_inicio,
            'fecha_hasta': fecha_fin
        })
        print('''
        ========================
            Periodo Editado !
        ========================
        ''')

    def eliminar_periodo(self, id_periodo):
        self.periodo.eliminar_periodo({
            'id_periodo': id_periodo
        })
        print('''
        ========================
            Periodo Eliminado !
        ========================
        ''')