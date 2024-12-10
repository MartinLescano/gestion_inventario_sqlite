from menu_access import Menu_Access
import os
class Menu:
    def __init__(self, option=-1):
        self.option = option
        
    def print_menu(self):
        obj_menu_access = Menu_Access()
        print("+-------------- MENU ----------------+")
        print("|                                    |")
        print("|    1: Gestion de Productos         |")
        print("|    2: Reportes                     |")
        print("|    0: Salir                        |")
        print("|                                    |")
        print("+------------------------------------+")
        self.option = obj_menu_access.option_validation_menu()
        
    def back_to_menu(self):
        print()
        input("Presiona una tecla para continuar...")
        os.system('cls')

    def clear(self):
        os.system('cls')

    def product_menu(self):
        obj_menu_access = Menu_Access()
        print("+------------ PRODUCTOS -------------+")
        print("|                                    |")
        print("|    1: Registrar Producto           |")
        print("|    2: Buscar Producto              |")
        print("|    3: Actualizar Stock             |")
        print("|    4: Actualizar Nombre            |")
        print("|    5: Actualizar Descripcion       |")
        print("|    6: Eliminar Producto            |")
        print("|    7: Reactivar Producto           |")
        print("|    0: Volver al Menu               |")
        print("|                                    |")
        print("+------------------------------------+")
        self.option = obj_menu_access.option_validation_product()

    def reports_menu(self):
        obj_menu_access = Menu_Access()
        print("+------------ REPORTES --------------+")
        print("|                                    |")
        print("|    1: Listar Productos Activos     |")
        print("|    2: Listar Productos Inactivos   |")
        print("|    3: Listar Stock Bajo            |")
        print("|    0: Volver al Menu               |")
        print("|                                    |")
        print("+------------------------------------+")
        self.option = obj_menu_access.option_validation_report()

    
    def exit(self):
        print("+------------------------------------+")
        print("|                                    |")
        print("| Gracias por utilizar la aplicación |")
        print("|              😀😁😉                |")
        print("|                                    |")
        print("+------------------------------------+")
        print()
        input("Presiona una tecla para continuar...")
        os.system('cls')
        