from prettytable import PrettyTable

def print_table(data, header=[]):
    tabla = 'Algo ocurrio mal'
    if not data:
        raise ValueError('No hay ningún dato para mostrar')

    if isinstance(data, list):
        if isinstance(data[0], dict):
            header = list(data[0].keys())
            tabla = PrettyTable(header)
            for row in data:
                tabla.add_row(list(row.values()))
        elif isinstance(data[0], tuple):
            header = table_header(data[0], header)
            tabla = PrettyTable(header)
            for row in data:
                tabla.add_row(list(row))
    elif isinstance(data, dict):
        header = list(data.keys())
        tabla = PrettyTable(header)
        tabla.add_row(list(data.values()))
    elif isinstance(data, tuple):
        header = table_header(data, header)
        tabla = PrettyTable(header)
        tabla.add_row(list(data))
    return tabla

def table_header(data, head):
    if not head:
        head = list(range(1, len(data) + 1))
    if len(head) < len(data):
        head.extend(list(range(len(head) + 1, len(data) + 1)))
    if len(head) > len(data):
        del head[len(data):]
    return head

def input_data(texto, tipo='string'):
    while True:
        try:
            if tipo == 'string':
                dato = input(texto).strip()
            elif tipo == 'int':
                dato = int(input(texto).strip())
            elif tipo == 'float':
                dato = float(input(texto).strip())

            if str(dato):
                if (isinstance(dato, int) or isinstance(dato, float)) and dato < 0:
                    raise ValueError("")
                break
            else:
                print("No ingreso ningún dato")
        except ValueError:
            print('Debes ingresar el tipo de dato correcto')
    return dato


def input_fecha():
    while True:
        try:
            while  True:
                dia = int(input("Por favor ingrese el día correspondiente a la fecha >> "))
                if  int(dia) > 0 and int(dia) <=31:
                    # print(dia)
                    break
                else:
                    print("Debes ingresar una día entre el 1 al 31")

            while True:
                mes = int(input("Por favor ingrese el mes correspondiente a la fecha >> "))
                if  int(mes) > 0 and int(mes) <=12:
                    # print(mes)
                    break
                else:
                    print("Debes ingresar un mes entre el 1 al 12")

            while True:
                anio = int(input("Por favor ingrese el año correspondiente a la fecha >> "))
                if  int(anio) >= 2000 and int(anio) <=2030:
                    # print(anio)
                    break
                else:
                    print("Debes ingresar un año entre el 2000 al 2030")
            fecha = str(anio)+"/"+str(mes)+"/"+str(dia)
            # print(fecha)
            break
        except ValueError:
            print('Debes ingresar el tipo de dato correcto')
    return fecha

def pregunta(texto):
    print(f'\n{texto}\n')
    response = False
    while True:
        dato = input("Seleccione (si) o (no) >> ").strip()
        if dato.lower() == 'si':
            response = True
            break
        elif dato.lower() == 'no':
            response = False
            break
        else:
            print('Debe elegir una opción...')
    print("\n")
    return response
