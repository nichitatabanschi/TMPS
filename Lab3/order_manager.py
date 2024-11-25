# Singleton class for managing orders (with Observer Pattern)
class OrderManager:
    _instance = None  # Class-level private attribute

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.orders = []
        self.observers = []  # List to hold registered observers

    def add_order(self, order):
        self.orders.append(order)
        self.notify_observers(order)  # Notify all observers about the new order

    def list_orders(self):
        for order in self.orders:
            print(order.order_type())

    # Observer Pattern: Register an observer
    def register_observer(self, observer):
        self.observers.append(observer)

    # Observer Pattern: Remove an observer
    def remove_observer(self, observer):
        self.observers.remove(observer)

    # Notify all observers
    def notify_observers(self, order):
        for observer in self.observers:
            observer.update(order)
