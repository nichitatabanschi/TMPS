from abc import ABC, abstractmethod

# Principle 1: Single Responsibility Principle (SRP)
# The Order class is responsible only for storing order details.

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items  # List of tuples (item_name, quantity, price_per_item)

# Principle 2: Open/Closed Principle (OCP)
# The CostCalculator class is open for extension but closed for modification.
# We can add new cost calculation strategies without modifying the base class.

class CostCalculator(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass

class RegularCostCalculator(CostCalculator):
    def calculate_total(self, order):
        total = 0
        for item in order.items:
            total += item[1] * item[2]  # quantity * price_per_item
        return total

class DiscountedCostCalculator(CostCalculator):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_total(self, order):
        total = 0
        for item in order.items:
            total += item[1] * item[2]  # quantity * price_per_item
        discount = total * self.discount_percentage / 100
        return total - discount

# Principle 1: Single Responsibility Principle (SRP)
# The ReportGenerator class is responsible only for generating reports.
# It does not handle any other logic like cost calculation.

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, order, total_cost):
        pass

class TextReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"Order ID: {order.order_id}\n"
        report += "Items:\n"
        for item in order.items:
            report += f"{item[0]} - {item[1]} @ {item[2]} each\n"
        report += f"Total Cost: {total_cost}\n"
        return report

class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"<h1>Order ID: {order.order_id}</h1>\n"
        report += "<ul>\n"
        for item in order.items:
            report += f"<li>{item[0]} - {item[1]} @ {item[2]} each</li>\n"
        report += "</ul>\n"
        report += f"<p>Total Cost: {total_cost}</p>\n"
        return report

# Example usage:

# Creating an order
order = Order(1, [("Laptop", 1, 1200), ("Mouse", 2, 50)])

# Using RegularCostCalculator
regular_calculator = RegularCostCalculator()
total_cost = regular_calculator.calculate_total(order)

# Generating a text report
text_report_generator = TextReportGenerator()
text_report = text_report_generator.generate_report(order, total_cost)
print("Text Report:\n", text_report)

# Using DiscountedCostCalculator (e.g., 10% discount)
discounted_calculator = DiscountedCostCalculator(10)
discounted_total_cost = discounted_calculator.calculate_total(order)

# Generating an HTML report
html_report_generator = HTMLReportGenerator()
html_report = html_report_generator.generate_report(order, discounted_total_cost)
print("HTML Report:\n", html_report)
