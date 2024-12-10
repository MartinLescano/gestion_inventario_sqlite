from menu import Menu
from product import Product
from product_access import Product_Access
from data_base import Data_Base
import os
import traceback

os.system('cls')
obj_menu = Menu()
data_base = "inventario.db"

#DICCIONARIOS MENU PRINCIPAL
def menu_op_1():
    while True:
        obj_menu.product_menu()
        os.system('cls')
        function = switch_product.get(obj_menu.option, invalid_option)
        if obj_menu.option !=0:
            function()
        else:
            function()
            break

def menu_op_2():
    while True:
        obj_menu.reports_menu()
        os.system('cls')
        function = switch_report.get(obj_menu.option, invalid_option)
        if obj_menu.option !=0:
            function()
        else:
            function()
            break

def menu_op_0():
    obj_menu.exit()

#DICCIONARIOS MENU PRODUCTOS
def product_op_1():
    add = 'x'
    add_low = add
    while add != 'n':
        data_base = "inventario.db"
        obj_product = Product()
        obj_product_access = Product_Access(obj_product, data_base)
        obj_data_base = Data_Base(data_base)
        print("+--------------REGISTRAR PRODUCTO 📦------------------+")
        try:
            obj_data_base.create_table(data_base)
            obj_product_access.register_product()
            obj_product_access.add_product(data_base)
            obj_data_base.close_connection()
        except Exception as ex:
            print()
            print("❌Error al guardar el producto.")
            print()
            print("+---------------------------------------------+")
            traceback.print_exc()
            obj_menu.back_to_menu()
            break
        add_low= 'x'
        while add_low != 's' and add_low != 'n':
            add = input("Registrar otro Producto? ('s': sí / 'n': no): ")
            add_low = add.lower()
            os.system('cls')
            if add_low == 'n':
                return
            elif add_low != 's':
                print("+----------REGISTRAR PRODUCTO 📦-------------+")
                print()
                input("Ingresar una opción válida!")
                print()
                print("+---------------------------------------------+")

def product_op_2():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.find_product(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
    obj_menu.back_to_menu()

def product_op_3():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.update_stock(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def product_op_4():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.update_name(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def product_op_5():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.update_description(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def product_op_6():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.delete_product(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def product_op_7():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.activate_product(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def product_op_0():
    obj_menu.clear()

#DICCIONARIOS MENU REPORTES
def report_op_1():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.show_products(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌ Error al consultar Productos.")
        traceback.print_exc()   
    obj_menu.back_to_menu()

def report_op_2():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.show_inactive_products(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌ Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def report_op_3():
    obj_product = Product()
    obj_product_access = Product_Access(obj_product, data_base)
    obj_data_base = Data_Base(data_base)
    try:
        obj_data_base.create_table(data_base)
        obj_product_access.show_low_stock(data_base)
        obj_data_base.close_connection()
    except Exception as ex:
        print("❌ Error al consultar Productos.")
        traceback.print_exc()
    obj_menu.back_to_menu()

def report_op_0():
    obj_menu.clear()

def invalid_option():
    return

switch_menu = {
    1: menu_op_1,
    2: menu_op_2,
    0: menu_op_0
}

switch_product = {
    1: product_op_1,
    2: product_op_2,
    3: product_op_3,
    4: product_op_4,
    5: product_op_5,
    6: product_op_6,
    7: product_op_7,
    0: product_op_0
}

switch_report = {
    1: report_op_1,
    2: report_op_2,
    3: report_op_3,
    0: report_op_0
}

#MENU
while True:
    obj_menu.print_menu()
    os.system('cls')

    function = switch_menu.get(obj_menu.option, invalid_option)

    if obj_menu.option !=0:
        function()
    else:
        function()
        break
    