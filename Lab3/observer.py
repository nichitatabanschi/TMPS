from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, order):
        pass

class ReportGeneratorObserver(Observer):
    def update(self, order):
        print(f"[ReportGenerator] New order added: {order.order_type()}")

class LoggingObserver(Observer):
    def update(self, order):
        print(f"[Logger] Order ID {order.order_id} added for {order.customer_name}")
