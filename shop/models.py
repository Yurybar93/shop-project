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


class Customer:
    def __init__(self, customer_id: str, email: str):
        self.customer_id = customer_id
        self._email = self._validate_email(email)

    @property
    def email(self) -> str:
        return self._email

    def change_email(self, new_email: str) -> None:
        self._email = self._validate_email(new_email)

    def _validate_email(self, email: str) -> str:
        if "@" not in email:
            raise ValueError("Invalid email address")
        return email


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self._quantity = self._validate_quantity(quantity)

    @property
    def quantity(self) -> int:
        return self._quantity

    def increase_quantity(self, n: int) -> None:
        self._quantity = self._validate_quantity(self._quantity + n)

    def set(self, n: int) -> None:
        self._quantity = self._validate_quantity(n)

    def _validate_quantity(self, n: int) -> int:
        if n <= 0:
            raise ValueError("Quantity must be at least 1")
        return n

    def total_line(self) -> float:
        return self.product.price * self.quantity


class Cart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self._items: dict[str, CartItem] = {}

    def add_item(self, product: Product, quantity: int) -> None:
        if product.sku in self._items:
            self._items[product.sku].increase_quantity(quantity)
        else:
            self._items[product.sku] = CartItem(product, quantity)

    def remove_item(self, sku: str) -> None:
        if sku in self._items:
            self._items.pop(sku)

    def clear(self) -> None:
        self._items.clear()

    def total_amount(self) -> float:
        return sum(item.total_line() for item in self._items.values())

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items.values())
