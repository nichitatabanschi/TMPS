# Creational Design Patterns in Restaurant Order Management System
---
**Author**: Tabanschi Nichita
---
## Objective:
The objective of this project is to demonstrate how creational design patterns (SRP and OCP) can be implemented in a Restaurant Order Management System using Python. The system takes user inputs for order details (items, quantities, prices) and generates reports in both text and HTML formats.

## Design Patterns Implemented:

### 1. Single Responsibility Principle (SRP):
- The `Order` class is responsible solely for storing order details (order ID, items, quantity, price). 
- The `ReportGenerator` class is responsible for generating reports (in text or HTML formats). It does not handle cost calculations or data management.

### 2. Open/Closed Principle (OCP):
- The `CostCalculator` class is open for extension but closed for modification. 
- We have two different implementations:
  1. **RegularCostCalculator**: Calculates total cost based on quantity and price.
  2. **DiscountedCostCalculator**: Extends cost calculation with a discount logic.

## Implementation Snippets:

```python

# Abstract base class for CostCalculator (OCP implementation)
from abc import ABC, abstractmethod

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


# Report generation (SRP implementation)
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, order, total_cost):
        pass

class TextReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"Order ID: {order.order_id}\\n"
        report += "Items:\\n"
        for item in order.items:
            report += f"{item[0]} - {item[1]} @ {item[2]} each\\n"
        report += f"Total Cost: {total_cost}\\n"
        return report

class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, order, total_cost):
        report = f"<h1>Order ID: {order.order_id}</h1>\\n"
        report += "<ul>\\n"
        for item in order.items:
            report += f"<li>{item[0]} - {item[1]} @ {item[2]} each</li>\\n"
        report += "</ul>\\n"
        report += f"<p>Total Cost: {total_cost}</p>\\n"
        return report

# Function to take order details from the user
def get_order_details():
    order_id = int(input("Enter order ID: "))
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {item_name}: "))
        price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, quantity, price))
    return Order(order_id, items)

```
# Example Interaction:

The system allows user input for order creation and applies cost calculation and report generation based on input.

# Input:
```
Enter order ID: 1
Enter item name (or 'done' to finish): Laptop
Enter quantity for Laptop: 1
Enter price for Laptop: 1200
Enter item name (or 'done' to finish): Mouse
Enter quantity for Mouse: 2
Enter price for Mouse: 50
Enter item name (or 'done' to finish): done
```
# Output:
```
Order ID: 1
Items:
Laptop - 1 @ 1200 each
Mouse - 2 @ 50 each
Total Cost: 1300.0

<h1>Order ID: 1</h1>
<ul>
<li>Laptop - 1 @ 1200 each</li>
<li>Mouse - 2 @ 50 each</li>
</ul>
<p>Total Cost: 1300.0</p>
```
---
# Conclusion:
In this project, the principles of SOLID design were followed by implementing the SRP and OCP principles. The system's flexibility is achieved through different cost calculation strategies and report generation mechanisms, making it easy to extend functionality without modifying existing code.