class PaymentProcessor:
    def process_payment(self, amount: float) -> bool:
        raise NotImplementedError("Subclasses must implement this method")


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${self.amount}")
        return True


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True


class BitcoinPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Bitcoin payment of ${amount}")
        return True
