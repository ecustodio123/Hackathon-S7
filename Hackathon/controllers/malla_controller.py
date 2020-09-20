from classes.profesor import Profesor
from classes.curso import Curso
from classes.salon import Salon
from classes.periodo import Periodo
from classes.profesor_curso import Profesor_curso
from classes.malla import Malla
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta 


class Malla_controller:
    def __init__(self):
        self.profesor = Profesor()
        self.curso = Curso()
        self.salon = Salon()
        self.periodo = Periodo()
        self.profesor_curso = Profesor_curso()
        self.malla = Malla()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ========================
                    Malla Curricular
                ========================
                ''')
                menu = ['Listar Malla', 'Buscar Malla', "Nuevo Registro", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_mallas()
                elif respuesta == 2:
                    self.buscar_malla()
                elif respuesta == 3:
                    self.insertar_malla()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_mallas(self):
        print('''
        ==================================
            Lista de Malla Curricular
        ==================================
        ''')
        mallas = self.malla.obtener_mallas('id_malla')
        print(print_table(mallas, ['ID_Malla', 'ID_Periodo', 'ID_Salón', 'ID_Profesor Curso']))
        input("\nPresione una tecla para continuar...")

    def insertar_malla(self):
        print('''
        ===========================
            Profesor - Cursos
        ===========================
        ''')
        try:
            profesor_curso = self.profesor_curso.obtener_profesor_cursos('id_profesor_curso')
            print(print_table(profesor_curso, ['ID_Profesor_Curso', 'Profesor', 'Curso']))
            id_profesor_curso = input_data("Ingrese el ID del profesor-curso >> ", "int")
            print(f'\n Asignación de cursos para el profesor :')
            print('''
            ============================
                Periodos disponibles
            ============================
            ''')
            periodos = self.periodo.obtener_periodos('id_periodo')
            periodos_disponibles = []
            if periodos:
                for periodo in periodos:
                    id_periodo = periodo[0]
                    nombre_periodo = periodo[1]
                    periodos_profesor = self.malla.buscar_mallas({
                        'id_periodo' : id_periodo,
                        'id_profesor_curso' : id_profesor_curso
                    })
                    if not periodos_profesor:
                        periodos_disponibles.append({
                            'id' : id_periodo,
                            'Periodos disponibles' : nombre_periodo
                        })
                print(print_table(periodos_disponibles))
                periodo_seleccionado = input_data(f'\nSeleccione el ID del periodo a asignar al profesor: >> ', 'int')
                buscar_periodo = self.periodo.obtener_periodo({'id_periodo': periodo_seleccionado})
                if not buscar_periodo:
                    print('\nEste curso no existe !')
                    return
                periodos_profesor = self.malla.buscar_mallas({
                    'id_periodo' : periodo_seleccionado,
                    'id_profesor_curso' : id_profesor_curso
                    # 'id_periodo' : id_periodo,
                    # 'id_profesor_curso' : periodo_seleccionado
                })
                if periodos_profesor:
                    print('\nEste curso ya está asignado al profesor !')
                    return    

            print('''
            ============================
                Salones disponibles
            ============================
            ''')
            salones = self.salon.obtener_salones('id_salon')
            salones_disponibles = []

            if salones:
                for salon in salones:
                    id_salon = salon[0]
                    nombre_salon = salon[1]
                    salones_profesor = self.malla.buscar_mallas({
                        'id_salon' : id_salon,
                        'id_profesor_curso' : id_profesor_curso
                    })
                    if not salones_profesor:
                        salones_disponibles.append({
                            'id' : id_salon,
                            'Salones disponibles' : nombre_salon
                        })
                print(print_table(salones_disponibles))
                salon_seleccionado = input_data(f'\nSeleccione el ID del Salon a asignar al profesor: >> ', 'int')
                buscar_salon = self.salon.obtener_salon({'id_salon': salon_seleccionado})
                if not buscar_salon:
                    print('\nEste salón no existe !')
                    return
                salones_profesor = self.malla.buscar_mallas({
                    'id_salon' : salon_seleccionado,
                    'id_profesor_curso' : id_profesor_curso
                })
                if salones_profesor:
                    print('\nEste Salón ya está asignado al profesor !')
                    return    
                self.malla.guardar_malla({
                    'id_periodo' : periodo_seleccionado,
                    'id_salon' : salon_seleccionado,
                    'id_profesor_curso' : id_profesor_curso
                })

            print('''
            =================================
                Nuevo Profesor agregado !
            =================================
            ''')
            self.listar_mallas()
        finally:
            pass

    def buscar_malla(self):
        print('''
        ================================
            Buscar Malla Curricular
        ================================
        ''')
        try:
            id_malla = input_data("Ingrese el ID de la malla curricular que desea buscar >> ", "int")
            malla = self.malla.obtener_malla({'id_malla': id_malla})
            print(print_table(malla, ['ID', 'ID_Periodo', 'ID_Salon', 'ID_Profesor_Curso']))

            if malla:
                if pregunta("¿Deseas dar mantenimiento a la malla?"):
                    opciones = ['Editar malla', 'Eliminar malla', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_malla(id_malla)
                    elif respuesta == 2:
                        self.eliminar_malla(id_malla)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_malla(self, id_malla):
        id_periodo = input_data("Ingrese el nuevo ID del periodo >> ")
        id_salon = input_data("Ingrese el nuevo ID del salón >> ")
        id_profesor_curso = input_data("Ingrese el nuevo ID del profesor-curso >> ")
        self.malla.modificar_malla({
            'id_malla': id_malla
        }, {
            'id_periodo': id_periodo,
            'id_salon': id_salon,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        ==========================
            Malla Editada !
        ==========================
        ''')

    def eliminar_malla(self, id_malla):
        self.malla.eliminar_malla({
            'id_malla': id_malla
        })
        print('''
        ===========================
            Malla Eliminada !
        ===========================
        ''')