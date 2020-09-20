from classes.profesor_final import Profesor_final
from helpers.helper import print_table, input_data, pregunta 
from connection.conn import Conexion


class Profesor_final_controller:
    def __init__(self):
        self.profesor_final = Profesor_final()
        self.salir = False

    def profesor_total(self):
        try:
            conn = Conexion('profesor_final')
            query = '''
                DROP TABLE IF EXISTS profesor_final;
            '''
            
            conn.ejecutar_sentencia(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Conexion('profesor_final')
            query = '''
                CREATE TABLE IF NOT EXISTS profesor_final(
                    id_profesor_final SERIAL PRIMARY KEY NOT NULL,
                    id_profesor_curso INTEGER,
                    id_salon INTEGER,
                    id_alumno INTEGER
                );
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Conexion('profesor_final')
            query = f'''
            INSERT INTO profesor_final (id_profesor_curso, id_salon, id_alumno)
            SELECT id_profesor_curso, id_salon, id_alumno 
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
            Lista de Profesores-Final
        =============================
        ''')
        profesores_final = self.profesor_final.obtener_profesores_final('id_profesor_final')
        print(print_table(profesores_final, ['ID_Profesor_Final', 'ID_Profesor_Curso', 'ID_Salón', 'ID_Alumno']))
        input("\nPresione una tecla para continuar...")



   