import os

class Product:
    def __init__(self, id=0, name = '', description = '', stock = 0, price = 0.0, category = '', status = 1):
        self.id = id
        self.name = name
        self.description = description
        self.stock = stock
        self.price = price
        self.category = category
        self.status = status
        