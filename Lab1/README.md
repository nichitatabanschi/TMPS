# Creational Design Patterns  

**Author**: Tabanschi Nichita  

## Objectives:
- Get familiar with Creational Design Patterns (CDPs).
- Choose a specific domain.
- Implement at least 3 CDPs for the chosen domain.

## Domain Area:
The domain chosen for this project is a **Restaurant Order Management System**. Customers can place dine-in or takeaway orders, and the system is responsible for managing and processing the orders, as well as generating reports (in text and HTML formats) for each order.

## Used Design Patterns:
- **Factory Method**: Used for creating different types of orders (e.g., Dine-In and Takeaway).
- **Singleton**: Implemented for managing orders through a single `OrderManager` instance, ensuring there is only one point of control for order management.
- **Builder**: Used to simplify the construction of complex meal objects (e.g., combo meals consisting of a main dish, drink, and dessert).

---

## Implementation

### **Design Pattern 1: Factory Method**

The **Factory Method** pattern is used to create different types of orders (Dine-In or Takeaway). A separate factory is responsible for creating the right kind of order object based on the type of order specified.

#### Code:
```python
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
     
### **Design Pattern 2: Singleton**###
The Singleton pattern ensures that there is only one OrderManager managing all orders throughout the program. This prevents multiple instances of the manager from being created.


class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'orders'):
            self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        for order in self.orders:
            print(order.order_type())