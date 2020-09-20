from classes.alumno_final import Alumno_final
from helpers.helper import print_table, input_data, pregunta 
from connection.conn import Conexion


class Alumno_final_controller:
    def __init__(self):
        self.alumno_final = Alumno_final()
        self.salir = False

    def alumno_total(self):
        while True:
            try:
                conn = Conexion('alumnos_final')
                query = '''
                    DROP TABLE IF EXISTS alumnos_final;
                '''
                conn.ejecutar_sentencia(query)
                conn.commit()

            except Exception as e:
                print(f'{str(e)}')

            try:
                conn = Conexion('alumnos_final')
                query = '''
                    CREATE TABLE IF NOT EXISTS alumnos_final(
                        id_alumno_final SERIAL PRIMARY KEY NOT NULL,
                        id_alumno INTEGER,
                        id_salon INTEGER,
                        id_profesor_curso INTEGER
                    );
                '''
                conn.ejecutar_sentencia(query)
                conn.commit()

            except Exception as e:
                print(f'{str(e)}')

            try:
                conn = Conexion('alumnos_final')
                query = f'''
                INSERT INTO alumnos_final (id_alumno, id_salon, id_profesor_curso)
                SELECT id_alumno, id_salon, id_profesor_curso 
                FROM notas INNER JOIN malla_curricular on notas.id_malla = malla_curricular.id_malla
                '''
                cursor = conn.ejecutar_sentencia(query)
                conn.commit()

            except Exception as e:
                print(f'{str(e)}')

            finally:
                conn.close_connection()

            print('''
            =============================
                Lista de Alumnos-Final
            =============================
            ''')
            alumnos_final = self.alumno_final.obtener_alumnos_final('id_alumno_final')
            print(print_table(alumnos_final, ['ID_Alumno_Final', 'ID_Alumno', 'ID_Salón', 'ID_Profesor_Curso']))
            input("\nPresione una tecla para continuar...")
            self.salir = True
            conn = ""
            break



   