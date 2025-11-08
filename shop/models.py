class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.__price = self._validate_price(price)

    def _validate_price(self, price: float) -> float:
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price

    @property
    def price(self) -> float:
        return self.__price

    def set_price(self, new_price: float):
        self.__price = self._validate_price(new_price)
