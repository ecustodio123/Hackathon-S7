from classes.notas_final import Nota_final
from helpers.helper import print_table, input_data, pregunta 
from connection.conn import Conexion

class Notas_final_controller:
    def __init__(self):
        self.nota_final = Nota_final()
        self.salir = False

    def notas_total(self):
        try:
            conn = Conexion('notas_final')
            query = '''
                DROP TABLE IF EXISTS notas_final;
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Conexion('notas_final')
            query = '''
                CREATE TABLE IF NOT EXISTS notas_final(
                    id_nota_final SERIAL PRIMARY KEY NOT NULL,
                    id_periodo INTEGER,
                    id_salon INTEGER,
                    nota INTEGER
                );
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Conexion('notas_final')
            query = f'''
            INSERT INTO notas_final (id_periodo, id_salon, nota)
            SELECT id_periodo,  id_salon, nota
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
            Lista de Notas-Final
        =============================
        ''')
        notas_final = self.nota_final.obtener_notas_final('id_nota_final')
        print(print_table(notas_final, ['ID_Nota_Final', 'ID_Periodo', 'ID_Salon', 'Nota']))
        if notas_final:
            for nota in notas_final:
                id_periodo = nota[2]
                id_salon = nota[3]

        input("\nPresione una tecla para continuar...")
        self.salir = True


