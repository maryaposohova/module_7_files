# from pprint import pprint
#
#
# class Product:
#     def __init__(self, name, weight: float, category):
#         self.name = name
#         self.weight = weight
#         self.category = category
#
#     def __str__(self):
#         return f'{self.name}, {self.weight}, {self.category}\n'
#
#
# class Shop(Product):
#     def __init__(self):
#         # super().__init__(name=None, weight=0.0, category=None)
#         super().__init__(name='Potato', weight=50.5, category='Vegetables')
#         self.products = None
#         self.__file_name = 'products.txt'
#
#     def get_products(self):
#         file_name = 'products.txt'
#         file = open(file_name, 'r')
#         file_content = file.read()
#         file.close()
#         return file_content
#
#     # def get1_products(self):
#     #     file_name = 'products.txt'
#     #     file = open(file_name, 'r+')
#     #     file_content = file.read()
#     #     file.write(f'{self.name}, {self.weight}, {self.category}\n')
#     #     file.close()
#     #     return file_content
#
#     def add(self, *products):
#         # self.products = products
#         file_name = 'products.txt'
#         file = open(file_name, 'a')
#         file.write(f'{self.name}, {self.weight}, {self.category}\n')
#         file.close()
#         # return file_content
#
#
#
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(1, p2)  # __str__
#
# s1.add( p2, p3)
#
# print(2, s1.get_products())
#
#
#


"""4"""


class Product:
    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    # def __eq__(self, other):
    #     return self.name == other.name and self.weight == other.weight and self.category == other.category


class Shop(Product):
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_name = self.__file_name
        file = open(file_name, 'r')
        file_content = file.read()
        file.close()
        return file_content

    def add(self, *products):
        yes_products = self.get_products().strip().split("\n")
        yes_products = [line.strip() for line in yes_products]
        file_name = self.__file_name
        file = open(file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str not in yes_products:
                file.write(product_str + '\n')
            else:
                print(f"Продукт {product_str} уже есть в магазине")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
