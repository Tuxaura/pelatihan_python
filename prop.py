class Product:
    # def __init__(self, price):
    #     self.set_price(price)

    def __init__(self, price):
        self.__price = price

    # def get_price(self, value):
    #     return self.__price

    # def __get_price(self, value):
    #     return self.__price

    @property
    def price(self):
        return self.__price

    # def set_price(self, value):
    #     if value < 0:
    #         raise ValueError("Price Tidak Boleh Negatif")
    #     self.__price = value

    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError("Price Tidak Boleh Negatif")
    #     self.__price = value

    #price = property(get_price, set_price)


product = Product(12)
product.price = 20
print(product.price)
