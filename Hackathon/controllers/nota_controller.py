from classes.malla import Malla
from classes.alumno import Alumno
from classes.nota import Nota
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta 


class Nota_controller:
    def __init__(self):
        self.nota = Nota()
        self.malla = Malla()
        self.alumno = Alumno()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===========================
                    Registro de Notas
                ===========================
                ''')
                menu = ['Listar Notas', 'Buscar Notas', "Nuevo Registro", "Ver Alumnos completos","Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_notas()
                elif respuesta == 2:
                    self.buscar_nota()
                elif respuesta == 3:
                    self.insertar_nota()
                elif respuesta == 4:
                    self.alumnos_final()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_notas(self):
        print('''
        ==================================
            Lista total de notas
        ==================================
        ''')
        notas = self.nota.obtener_notas('id_malla')
        print(print_table(notas, ['ID_Notas', 'ID_Alumno', 'ID_Malla', 'Nota']))
        input("\nPresione una tecla para continuar...")

    def insertar_nota(self):
        print('''
        ===========================
                Alumnos
        ===========================
        ''')
        try:
            alumnos = self.alumno.obtener_alumnos('alumno_id')
            print(print_table(alumnos, ['ID_Alumno', 'Nombre', 'Edad', 'Correo']))
            alumno_seleccionado = input_data(f'\nSeleccione el ID del alumno del cual va registrar su nota: >> ', 'int')
            buscar_alumno = self.alumno.obtener_alumno({'alumno_id' : alumno_seleccionado})
            if not buscar_alumno:
                print(f'\nEl ID {alumno_seleccionado}  no existe')
                return
            print('''
                ===========================
                    Malla Curricular
                ===========================
            ''')
            malla = self.malla.obtener_mallas('id_malla')
            print(print_table(malla, ['ID_Malla', 'ID_Periodo', 'ID_Salon', 'ID_Profesor_Curso']))
            malla_seleccionada = input_data(f'\nSeleccione el ID de la malla  la cual va registrar su nota: >> ', 'int')
            buscar_malla = self.malla.obtener_malla({'id_malla' : malla_seleccionada})
            if not buscar_malla:
                print(f'\nEl ID {malla_seleccionada} no está registrado')
                return
            alumno_notas = self.nota.buscar_notas({
                'id_alumno' : alumno_seleccionado,
                'id_malla' : malla_seleccionada
            })
            if alumno_notas:
                print('\nEste Alumno ya tiene registrada una nota en dicho curso !')
                return
            nota = input_data("Por favor ingrese la nota correspondiente >> ", "int")
            self.nota.guardar_nota({
                'id_alumno' : alumno_seleccionado,
                'id_malla' : malla_seleccionada,
                'nota' : nota
            })
            print('''
            ===========================================
                Nuevo Registro de nota  agregado !
            ===========================================
            ''')

        finally:
            pass

    def buscar_nota(self):
        print('''
        =====================================
            Buscar en el Registro de Notas
        =====================================
        ''')
        try:
            id_nota = input_data("Ingrese el ID del registro de nota que desea buscar >> ", "int")
            nota = self.nota.obtener_nota({'id_nota' : id_nota})
            print(print_table(nota, ['ID_Nota','ID_Alumno', 'ID_malla', 'Nota']))

            if nota:
                if pregunta("¿Deseas dar mantenimiento al registro de nota seleccionada?"):
                    opciones = ['Editar nota', 'Eliminar nota', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_nota(id_nota)
                    elif respuesta == 2:
                        self.eliminar_nota(id_nota)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_nota(self, id_nota):
        id_alumno = input_data("Ingrese el nuevo ID del alumno >> ")
        id_malla = input_data("Ingrese el nuevo ID de la malla >> ")
        nota = input_data(f"Ingrese el nuevo nota del alumno con el ID {id_alumno} >> ", "int")
        self.nota.modificar_nota({
            'id_nota': id_nota
        }, {
            'id_alumno': id_alumno,
            'id_malla': id_malla,
            'nota': nota
        })
        print('''
        ==========================
            Nota Editada !
        ==========================
        ''')

    def eliminar_nota(self, id_nota):
        self.nota.eliminar_nota({
            'id_nota': id_nota
        })
        print('''
        ===========================
            Nota Eliminada !
        ===========================
        ''')


