from shop.models import Product, Customer, CartItem
from shop.orders import OrderItem


def test_product():
    product = Product(sku="123", name="Test Product", price=10.0)
    assert product.sku == "123"
    assert product.name == "Test Product"
    assert product.price == 10.0

    product.set_price(15.0)
    assert product.price == 15.0

    try:
        product.set_price(-5.0)
    except ValueError as e:
        assert str(e) == "Price cannot be negative"


def test_customer():
    customer = Customer(customer_id="cust1", email="john@example.com")
    assert customer.customer_id == "cust1"
    assert customer.email == "john@example.com"

    customer.change_email("john.doe@example.com")
    assert customer.email == "john.doe@example.com"

    try:
        customer.change_email("invalid_email")
    except ValueError as e:
        assert str(e) == "Invalid email address"


def test_cart_item():
    product = Product(sku="123", name="Test Product", price=20.0)
    cart_item = CartItem(product=product, quantity=2)
    assert cart_item.product == product
    assert cart_item.quantity == 2
    assert cart_item.total_line() == 40.0

    cart_item.increase_quantity(3)
    assert cart_item.quantity == 5
    assert cart_item.total_line() == 100.0

    cart_item.set(1)
    assert cart_item.quantity == 1
    assert cart_item.total_line() == 20.0

    try:
        cart_item.set(0)
    except ValueError as e:
        assert str(e) == "Quantity must be at least 1"


def test_order_item_total_line():
    item = OrderItem(product_sku="sku1", name="Item 1", price=10.0, qty=3)
    assert item.total_line() == 30.0
