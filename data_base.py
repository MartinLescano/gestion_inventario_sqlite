import sqlite3

class Data_Base:
    def __init__(self, connection='', data_base=''):
        self.connection = connection
        self.data_base = data_base

    def create_table(self, data_base):
        try:
            self.connection = sqlite3.connect(data_base)
            cursor = self.connection.cursor()
            #print(f"Conexión exitosa con {data_base} 🔗")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                stock INTEGER NOT NULL,
                price REAL NOT NULL,
                category TEXT NOT NULL,
                status INTEGER NOT NULL
            )                  
            """)
            self.connection.commit()
        except sqlite3.Error as ex:
            print(f"❌ Error al crear la tabala en {ex}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            #print("Se cerró la conexión con la Base de Datos.")
            