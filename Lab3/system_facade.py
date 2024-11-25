from order import DineInOrderFactory, TakeawayOrderFactory
from order_manager import OrderManager
from cost_calculator import RegularCostCalculator
from cost_decorator import TaxDecorator, ServiceChargeDecorator
from report_generator import TextReportGenerator, HTMLReportGenerator
from observer import LoggingObserver, ReportGeneratorObserver

class SystemFacade:
    def __init__(self):
        self.order_manager = OrderManager()

        # Register observers
        self.order_manager.register_observer(LoggingObserver())
        self.order_manager.register_observer(ReportGeneratorObserver())

        self.regular_calculator = RegularCostCalculator()
        self.text_report_generator = TextReportGenerator()
        self.html_report_generator = HTMLReportGenerator()

    def create_order(self, order_type, order_id, customer_name, items, table_number=None):
        if order_type == "dine-in":
            factory = DineInOrderFactory(table_number)
        else:
            factory = TakeawayOrderFactory()

        order = factory.create_order(order_id, customer_name)
        order.items = items
        self.order_manager.add_order(order)
        return order

    def calculate_cost(self, order, tax_rate=0, service_charge=0):
        calculator = self.regular_calculator
        if tax_rate > 0:
            calculator = TaxDecorator(calculator, tax_rate)
        if service_charge > 0:
            calculator = ServiceChargeDecorator(calculator, service_charge)

        return calculator.calculate_total(order)

    def generate_report(self, order, format="text"):
        total_cost = self.calculate_cost(order)
        if format == "text":
            return self.text_report_generator.generate_report(order, total_cost)
        elif format == "html":
            return self.html_report_generator.generate_report(order, total_cost)

    def list_all_orders(self):
        self.order_manager.list_orders()
