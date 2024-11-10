# Singleton class for managing orders
class OrderManager:
    _instance = None  # Class-level private attribute

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        for order in self.orders:
            print(order.order_type())
