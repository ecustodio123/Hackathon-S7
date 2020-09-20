class Menu:
    def __init__(self, lista_menu): # ["Alumnos", "Profesores", "Salones"]
        self.lista_menu = lista_menu

    def show(self):
        response = 0
        print('Selecciona una opción:\n')
        for x in range(0,len(self.lista_menu)):
            if x == len(self.lista_menu) - 1:
                print(f"    {str(x + 1)})   {str(self.lista_menu[x])}\n")
            else:
                print(f"    {str(x + 1)})   {str(self.lista_menu[x])}")
        while True:
            try:
                response = int(input(">> "))
                if response in range(1, len(self.lista_menu) + 1):
                    break
                else:
                    print("Debes ingresar una opción valida")
            except ValueError:
                print('Debes ingresar una opción valida')
        return response