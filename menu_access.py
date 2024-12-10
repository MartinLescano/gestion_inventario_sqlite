import os

class Menu_Access:
    def __init__(self):
        pass

    #VALIDACION PARA EL MENU PRINCIPAL
    def option_validation_menu(self):
        try: 
            option = int(input("Ingresar opción: "))
            if option <= 2:
                return option
            else:
                print("❗ Ingresar una opción válida")
                print()
                input("Presiona una tecla para continuar...")
                option=-1 #resetea el valor de self.option
                os.system('cls')
            return option
        except Exception:
            print("❗ Ingresar una opción válida.")
            print()
            input("Presiona una tecla para continuar...")
            self.option=-1 #resetea el valor de self.option
            os.system('cls')
            return

    #VALIDACION PARA EL MENU DE PRODUCTOS
    def option_validation_product(self):
        try:
            option = int(input("Ingresar opción: "))
            if option <= 7:
                return option
            else:
                print("❗ Ingresar una opción válida")
                print()
                input("Presiona una tecla para continuar...")
                option=-1 #resetea el valor de self.option
                os.system('cls')
            return option
        except Exception:
            print("❗ Ingresar una opción válida")
            print()
            input("Presiona una tecla para continuar...")
            self.option=-1 #resetea el valor de self.option
            os.system('cls')
            return
    
    #VALIDACION PARA EL MENU REPORTES
    def option_validation_report(self):
        try:
            option = int(input("Ingresar opción: "))
            if option <= 3:
                return option
            else:
                print("❗ Ingresar una opción válida")
                print()
                input("Presiona una tecla para continuar...")
                option=-1 #resetea el valor de self.option
                os.system('cls')
            return option
        except Exception:
            print("❗ Ingresar una opción válida")
            print()
            input("Presiona una tecla para continuar...")
            self.option=-1 #resetea el valor de self.option
            os.system('cls')
            return
        