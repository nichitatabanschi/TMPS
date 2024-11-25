from abc import ABC, abstractmethod

# Abstract Order Class
class Order(ABC):
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name

    @abstractmethod
    def order_type(self):
        pass

# Concrete DineInOrder Class
class DineInOrder(Order):
    def __init__(self, order_id, customer_name, table_number):
        super().__init__(order_id, customer_name)
        self.table_number = table_number

    def order_type(self):
        return f"Dine-In Order at Table {self.table_number}"

# Concrete TakeawayOrder Class
class TakeawayOrder(Order):
    def __init__(self, order_id, customer_name):
        super().__init__(order_id, customer_name)

    def order_type(self):
        return "Takeaway Order"

# Factory Method Abstract Class
class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, order_id, customer_name):
        pass

# Concrete DineInOrderFactory
class DineInOrderFactory(OrderFactory):
    def __init__(self, table_number):
        self.table_number = table_number

    def create_order(self, order_id, customer_name):
        return DineInOrder(order_id, customer_name, self.table_number)

# Concrete TakeawayOrderFactory
class TakeawayOrderFactory(OrderFactory):
    def create_order(self, order_id, customer_name):
        return TakeawayOrder(order_id, customer_name)
