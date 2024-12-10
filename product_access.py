from product import Product
from data_base import Data_Base
import sqlite3
import os
import traceback

class Product_Access(Product, Data_Base):
    def __init__(self, obj_product, data_base):
        super().__init__(obj_product) #Se hereda el consturctor de 'Product'
        super().__init__(data_base) #Se hereda el consturctor de 'Data_Base'

    #REGISTRA LA INFORMACION DE UN PRODUCTO
    def register_product(self):
        valid = 0
        self.name = input("Ingresar Nombre del Producto: ")
        self.description = input("Ingresar Descripcion: ")
        while valid == 0:
            try:
                self.stock = int(input("Ingresar Stock: "))
                valid = 1
            except Exception as ex:
                print()
                print("⛔ Ingresar un STOCK valido.")
                valid = 0
        valid = 0
        while valid == 0:
            try:
                self.price = float(input("Ingresar Precio Unitario: "))
                valid = 1
            except Exception as ex:
                print()
                print("⛔ Ingresar un PRECIO valido.")
                valid = 0
        self.category = input("Ingresar categoría: ")
        self.status = 1
    
    #AGREGA EL PRODUCTO A LA BASE DE DATOS
    def add_product(self, data_base):
        try:
            with sqlite3.connect(data_base) as cursor:
                #cursor = cur.cursor()
                cursor.execute("INSERT INTO inventario (name, description, stock, price, category, status) VALUES (?,?,?,?,?,?)",(self.name, self.description, self.stock, self.price, self.category, self.status))
                cursor.commit()
                print("✅ Producto agregado a la Base de Datos")
        except sqlite3.Error as ex:
            print(f"❌Error al ingresar producto.")
            traceback.print_exc()

    #AVERIGUA SI ES QUE NO HAY LINEAS EN LA TABLA. True = "No hay filas" / False = "sí, hay filas"
    def no_queues(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                cursor = cur.cursor()
                cursor.execute("SELECT COUNT(*) FROM inventario")
                count = cursor.fetchall()
                for row in count:
                    if row[0] == 0:
                        return True
                    else: 
                        return False
        except sqlite3.Error as ex:
            print(f"❌Error al consultar la base de datos.")
            return False
            traceback.print_exc()

    #BUSCA UN PRODUCTO POR NOMBRE BASADO EN UNA COINCIDENCIA PARCIAL (PUEDE ARROJAR UNO O MAS RESULTADOS)
    def find_product(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+------------🔎 Buscar Producto------------+")
                search = input("Ingresar Nombre del Producto: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE ? AND status = 1", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nDescripcion:",product[2],
                            "\nStock:",product[3],
                            "\nPrecio:",product[4],
                            "\nCategoria:",product[5])
                        print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #ACTUALIZAR STOCK
    def update_stock(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+--------------📝 ACTUALIZAR STOCK -----------------+")
                search = input("Ingresar Nombre del Producto: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE (?)", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nStock:",product[3])
                        print("------------------------------------------")
                    valid = 0
                    while valid == 0:
                        try:
                            id_to_update = int(input("Confirmar ID del Producto: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    valid = 0
                    while valid == 0:
                        try:
                            new_stock = int(input("Ingresar Nuevo Stock: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un STOCK valido.")
                            valid = 0
                    os.system('cls')
                    cursor.execute("""
                                    UPDATE inventario 
                                    SET stock = ? 
                                    WHERE id = ?"""
                                    , (new_stock, id_to_update,))
                    cur.commit()
                    cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                    results_updated = cursor.fetchall()
                    print("+--------------📝 ACTUALIZAR STOCK -----------------+")
                    print("✅ Stock actualizado.")
                    for product in results_updated:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nStock:",product[3])
                        print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #ACTUALIZAR NOMBRE
    def update_name(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+--------------📝 ACTUALIZAR NOMBRE -----------------+")
                search = input("Ingresar Nombre Actual: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE (?)", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1])
                        print("------------------------------------------")
                    valid = 0
                    while valid == 0:
                        try:
                            id_to_update = int(input("Confirmar ID del Producto: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    new_name = input("Ingresar Nuevo Nombre: ")
                    os.system('cls')
                    cursor.execute("""
                                    UPDATE inventario 
                                    SET name = ? 
                                    WHERE id = ?"""
                                    , (new_name, id_to_update,))
                    cur.commit()
                    cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                    results_updated = cursor.fetchall()
                    print("+--------------📝 ACTUALIZAR NOMBRE -----------------+")
                    print("✅ Nombre Actualizado.")
                    for product in results_updated:
                        print("ID:",product[0],
                            "\nProducto:",product[1])
                        print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #ACTUALIZAR DESCRIPCION
    def update_description(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+----------📝 ACTUALIZAR DESCRIPCION ------------+")
                search = input("Ingresar Nombre del Producto: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE (?)", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                             "\nDescripcion:",product[2])
                        print("------------------------------------------")
                    valid = 0
                    while valid == 0:
                        try:
                            id_to_update = int(input("Confirmar ID del Producto: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    new_description = input("Ingresar Nueva Descripcion: ")
                    os.system('cls')
                    cursor.execute("""
                                    UPDATE inventario 
                                    SET description = ? 
                                    WHERE id = ?"""
                                    ,(new_description, id_to_update))
                    cur.commit()
                    cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                    results_updated = cursor.fetchall()
                    print("+----------📝 ACTUALIZAR DESCRIPCION ------------+")
                    print("✅ Descripcion Actualizada.")
                    for product in results_updated:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nDescripcion:",product[2])
                        print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #ELIMINAR PRODUCTO MODIFICANDO ESTADO
    def delete_product(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+--------------🛑 ELIMIAR PRODUCTO -----------------+")
                search = input("Ingresar Nombre del Producto a ELIMINAR: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE (?) AND status = 1", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nEstado:",product[6])
                        print("------------------------------------------")
                    valid = 0
                    while valid == 0:
                        try:
                            id_to_update = int(input("Confirmar ID del Producto a ELIMINAR: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    add_low= 'x'
                    while add_low != 's' and add_low != 'n':
                        add_low = input("Desea ELIMINAR el Producto? ('s': sí / 'n': no): ")
                        add_low = add_low.lower()
                        os.system('cls')
                        if add_low == 'n':
                            cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                            results_updated = cursor.fetchall()
                            print("+--------------🛑 ELIMIAR PRODUCTO -----------------+")
                            print()
                            print("❌ NO se ha eliminado el producto: ")
                            for product in results_updated:
                                print("ID:",product[0],
                                    "\nProducto:",product[1],
                                    "\nEstado:",product[6])
                            print("------------------------------------------")
                            return
                        elif add_low == 's':
                            os.system('cls')
                            cursor.execute("""
                                            UPDATE inventario
                                            SET status = 0
                                            WHERE id = ?"""
                                            ,(id_to_update,))
                            cur.commit()
                            cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                            results_updated = cursor.fetchall()
                            print("+--------------🛑 ELIMIAR PRODUCTO -----------------+")
                            print("❌ Producto Eliminado.")
                            for product in results_updated:
                                print("ID:",product[0],
                                    "\nProducto:",product[1],
                                    "\nEstado:",product[6])
                                print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #REACTIVAR PRODUCTO ELIMINADO
    def activate_product(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+--------------✅ REACTIVAR PRODUCTO -----------------+")
                search = input("Ingresar Nombre del Producto a ELIMINAR: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE ? AND status = 0", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nEstado:",product[6])
                        print("------------------------------------------")
                    valid = 0
                    while valid == 0:
                        try:
                            id_to_update = int(input("Confirmar ID del Producto a REACTIVAR: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    add_low= 'x'
                    while add_low != 's' and add_low != 'n':
                        add_low = input("Desea REACTIVAR el Producto? ('s': sí / 'n': no): ")
                        add_low = add_low.lower()
                        os.system('cls')
                        if add_low == 'n':
                            cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                            results_updated = cursor.fetchall()
                            print("+-----------✅ REACTIVAR PRODUCTO ------------+")
                            print()
                            print("❌ NO se ha reactivado el producto: ")
                            for product in results_updated:
                                print("ID:",product[0],
                                    "\nProducto:",product[1],
                                    "\nEstado:",product[6])
                            print("------------------------------------------")
                            return
                        elif add_low == 's':
                            os.system('cls')
                            cursor.execute("""
                                            UPDATE inventario 
                                            SET status = 1 
                                            WHERE id = ?"""
                                            ,(id_to_update,))
                            cur.commit()
                            cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_update,))
                            results_updated = cursor.fetchall()
                            print("+-----------✅ REACTIVAR PRODUCTO ------------+")
                            print("✔ Producto Nuevamente Disponible.")
                            for product in results_updated:
                                print("ID:",product[0],
                                    "\nProducto:",product[1],
                                    "\nEstado:",product[6])
                                print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #MOSTRAR LISTADO DE PRODUCTOS (ACTIVOS)
    def show_products(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE status =1")
                results = cursor.fetchall()
                print("+------------📝 Lista de Productos ------------+")
                if self.no_queues(data_base) == False:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nDescripcion:",product[2],
                            "\nStock:",product[3],
                            "\nPrecio:",product[4],
                            "\nCategoria:",product[5])
                        print("------------------------------------------")
                else:
                    print()
                    print("⛔ Inventario vacío.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()

    #LISTAR PRODUCTOS ELIMINADOS
    def show_inactive_products(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE status = 0")
                results = cursor.fetchall()
                print("+------------🛑 LISTA DE PRODUCTOS ELIMINADOS ------------+")
                count = 0
                for product in results:
                    print("ID:",product[0],
                        "\nProducto:",product[1],
                        "\nDescripcion:",product[2],
                        "\nStock:",product[3],
                        "\nPrecio:",product[4],
                        "\nCategoria:",product[5])
                    print("------------------------------------------")
                    count += 1
                if count == 0:
                    print()
                    print("⛔ No hay productos eliminados.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productoS.")
            traceback.print_exc()

    #LISTAR PRODUCTOS CON STOCK BAJO
    def show_low_stock(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE stock < 10")
                results = cursor.fetchall()
                print("+------------❗LISTA DE BAJO STOCK ------------+")
                count = 0
                for product in results:
                    print("ID:",product[0],
                        "\nProducto:",product[1],
                        "\nDescripcion:",product[2],
                        "\nStock:",product[3],
                        "\nPrecio:",product[4],
                        "\nCategoria:",product[5])
                    print("------------------------------------------")
                    count += 1
                if count == 0:
                    print()
                    print("✅ No hay productos con bajo stock.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()
    
    #ELIMINA EL PRODUCTO DE LA BASE DE DATOS SIN DEJAR REGISTRO
    def delete_product_db(self, data_base):
        try:
            with sqlite3.connect(data_base) as cur:
                print("+---🛑 ELIMIAR PRODUCTO DE LA BASE SE DATOS ---+")
                search = input("Ingresar Nombre del Producto a ELIMINAR: ")
                cursor = cur.cursor()
                cursor.execute("SELECT * FROM inventario WHERE name LIKE (?)", (f"%{search}%",))
                results = cursor.fetchall()
                if results:
                    for product in results:
                        print("ID:",product[0],
                            "\nProducto:",product[1],
                            "\nEstado:",product[6])
                        print("------------------------------------------")
                        valid = 0
                    while valid == 0:
                        try:
                            id_to_delete = int(input("Confirmar ID del Producto a ELIMINAR: "))
                            valid = 1
                        except Exception as ex:
                            print()
                            print("⛔ Ingresar un ID valido.")
                            valid = 0
                    add_low= 'x'
                    while add_low != 's' and add_low != 'n':
                        add_low = input("Desea ELIMINAR el Producto? ('s': sí / 'n': no): ")
                        add_low = add_low.lower()
                        os.system('cls')
                        if add_low == 'n':
                            cursor.execute("SELECT * FROM inventario WHERE id = ?", (id_to_delete,))
                            results_updated = cursor.fetchall()
                            print("+---🛑 ELIMIAR PRODUCTO DE LA BASE SE DATOS ---+")
                            print()
                            print("❌ NO se ha eliminado el producto: ")
                            for product in results_updated:
                                print("ID:",product[0],
                                    "\nProducto:",product[1],
                                    "\nEstado:",product[6])
                            print("------------------------------------------")
                            return
                        elif add_low == 's':
                            os.system('cls')
                            cursor.execute("DELETE FROM inventario WHERE id = ?",(id_to_delete,))
                            cur.commit()
                            print("+---🛑 ELIMIAR PRODUCTO DE LA BASE SE DATOS ---+")
                            print()
                            print("❌Producto ELIMINADO de la base de datos.")
                            print()
                            print("------------------------------------------")
                else:
                    print()
                    print("⛔ Producto no encontrado.")
                    print()
                    print("+----------------------------------------------+")
        except sqlite3.Error as ex:
            print(f"❌Error al consultar productos.")
            traceback.print_exc()
