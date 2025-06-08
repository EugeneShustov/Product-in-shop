class product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def info(self):
        return f"{self.__name}: {self.__store}, {self.__price} руб."

    def name(self):
        return self.__name

    def store(self):
        return self.__store

    def price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, product):
            return self.__price + other.__price
        raise TypeError("Нельзя сложить продукт")

class warehouse:
    def __init__(self):
        self.__products = []

    def add(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.__products):
            return self.__products[index].info()
        return "Продукт не найден"

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.name() == name:
                return product.info()
        return "Продукт не найден"

    def sort_products(self, key="name"):
        if key == "name":
            self.__products.sort(key=lambda p: p.name())
        elif key == "store":
            self.__products.sort(key=lambda p: p.store())
        elif key == "price":
            self.__products.sort(key=lambda p: p.price())
        else:
            raise ValueError("Неправильная сортировка")

    def show_products(self):
        return [product.info() for product in self.__products]

product_one = product("Бананы", "Санта", 10)
product_two = product("Груши", "Грин", 15)
product_three = product("Яблоки", "Белмаркет", 10)

warehouse = warehouse()
warehouse.add(product1)
warehouse.add(product2)
warehouse.add(product3)

print(warehouse.get_product_by_index(1))
print(warehouse.get_product_by_name("Яблоки"))

warehouse.sort_products("price")
print(warehouse.show_products())

print(product1 + product3)
