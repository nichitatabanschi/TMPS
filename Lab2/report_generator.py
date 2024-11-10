from abc import ABC, abstractmethod

# Abstract Class for Report Generation
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, order, total_cost):
        pass

# Text Report Generation
class TextReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"Order ID: {order.order_id}\nItems:\n"
        for item in order.items:
            report += f"{item[0]} - {item[1]} @ {item[2]} each\n"
        report += f"Total Cost: {total_cost}\n"
        return report

# HTML Report Generation
class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"<h1>Order ID: {order.order_id}</h1>\n<ul>\n"
        for item in order.items:
            report += f"<li>{item[0]} - {item[1]} @ {item[2]} each</li>\n"
        report += f"</ul>\n<p>Total Cost: {total_cost}</p>\n"
        return report
