from __future__ import annotations


class Product:
    def __init__(self, prod_id: int, name: str, price: float):
        self.id = prod_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id}. Товар {self.name} за ціною {self.price}"

    def change_price(self, new_price: float):
        self.price = new_price


class Stock:
    def __init__(self, stock_quantity: dict[str, int] | None = None):
        self.stock_quantity = {} if stock_quantity is None else stock_quantity

    def change_quantity(self, product: Product, new_quantity: int):
        self.stock_quantity[product.name] = new_quantity

    def get_quantity(self, product: Product) -> int:
        return self.stock_quantity.get(product.name, 0)


class Customer:
    def __init__(self, last_name: str, first_name: str, phone_number: str,
                 email: str, orders_list: list[Order] | None = None):
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.email = email
        self.orders_list = [] if orders_list is None else orders_list

    def __str__(self):
        order_str = (
            "\n".join([f"  - {order}" for order in self.orders_list])
            if self.orders_list else "немає"
        )
        return (f"\nПокупець {self.last_name} {self.first_name}.\n"
                f"Телефон {self.phone_number}, email {self.email}.\n"
                f"Архів замовлень:\n{order_str}")

    def add_order_to_history(self, order: Order):
        self.orders_list.append(order)


class Order:
    def __init__(self, order: list[tuple[Product, int]] | None = None):
        self.order = [] if order is None else order

    def __str__(self):
        items = ", ".join([f"{prod.name} ({quant} шт.)"
                           for prod, quant in self.order])
        return (f"Замовлення: Товари: {items}. "
                f"Сумарна вартість: {self.calculate_total()} грн.")

    def add_order_to_cart(self, product: Product, quantity: int,
                          stock: Stock):
        if quantity <= stock.get_quantity(product):
            self.order.append((product, quantity))
            stock.change_quantity(product, stock.get_quantity(product) - quantity)
        else:
            print(f"Недостатньо товару '{product.name}'. "
                  f"(Доступно {stock.get_quantity(product)} шт).")

    def calculate_total(self) -> float:
        return sum(product.price * quant for product, quant in self.order)
