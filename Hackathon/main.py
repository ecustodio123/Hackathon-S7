from helpers.menu import Menu
from controllers.profesores_controller import Profesores_controller
from controllers.cursos_controller import Cursos_controller
from controllers.periodo_controller import Periodo_controller
from controllers.alumno_controller import Alumno_controller
from controllers.salon_controller import Salon_controller
from controllers.malla_controller import Malla_controller
from controllers.nota_controller import Nota_controller
from controllers.alumno_final_controller import Alumno_final_controller
from controllers.profesores_final_controller import Profesor_final_controller
from controllers.notas_final_controller import Notas_final_controller

def iniciar_app():
    try:
        print('''
        ==========================
            Sistema de Colegio
        ==========================
        ''')
        menu_principal = ["Profesores", "Alumnos", "Cursos", "Periodo Escolar", "Salones", "Habilitar salones y cursos", "Registro de notas", "Registro de Alumnos-Final", "Registro de Profesores-Final","Notas Final", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            profesor = Profesores_controller()
            profesor.menu()
            if profesor.salir:
                iniciar_app()
        elif respuesta == 2:
            alumno = Alumno_controller()
            alumno.menu()
            if alumno.salir:
                iniciar_app()
        elif respuesta == 3:
            curso = Cursos_controller()
            curso.menu()
            if curso.salir:
                iniciar_app()
        elif respuesta == 4:
            periodo = Periodo_controller()
            periodo.menu()
            if periodo.salir:
                iniciar_app()
        elif respuesta == 5:
            salon = Salon_controller()
            salon.menu()
            if salon.salir:
                iniciar_app()
        elif respuesta == 6:
            malla = Malla_controller()
            malla.menu()
            if malla.salir:
                iniciar_app()
        elif respuesta == 7:
            nota = Nota_controller()
            nota.menu()
            if nota.salir:
                iniciar_app()
        elif respuesta == 8:
            alumno_final = Alumno_final_controller()
            alumno_final.alumno_total()
            iniciar_app()
        elif respuesta == 9:
            profesor_final = Profesor_final_controller()
            profesor_final.profesor_total()
            iniciar_app()
        elif respuesta == 10:
            notas_final = Notas_final_controller()
            notas_final.notas_total()
            iniciar_app()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()