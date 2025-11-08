from shop.models import Customer
from shop.payment import PaymentProcessor


class OrderItem:
    def __init__(self, product_sku: str, name: str, price: float, qty: int):
        self.product_sku = product_sku
        self.name = name
        self.price = price
        self.qty = qty

    def total_line(self) -> float:
        return self.price * self.qty


class Order:
    def __init__(
        self,
        order_id: int,
        items: list[OrderItem],
        payment_processor: PaymentProcessor,
        customer: Customer,
    ):
        self.order_id = order_id
        self.customer = customer
        self._items = items
        self.payment_processor = payment_processor

    def total_amount(self) -> float:
        return sum(item.total_line() for item in self._items)

    def process_order(self) -> bool:
        amount = self.total_amount()
        return self.payment_processor.process_payment(amount)

    def __str__(self) -> str:
        item_strs = [
            f"{item.name} (x{item.qty}): ${item.total_line():.2f}"
            for item in self._items
        ]
        items_description = "\n".join(item_strs)
        total = self.total_amount()
        return f"Order ID: {self.order_id}\nCustomer: {self.customer.name}\nItems:\n{items_description}\nTotal Amount: ${total:.2f}"
