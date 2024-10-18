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
   ```  
### **Design Pattern 2: Singleton**###
The Singleton pattern ensures that there is only one OrderManager managing all orders throughout the program. This prevents multiple instances of the manager from being created.

```python
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

```
# Design Pattern 3: Builder
The Builder pattern helps in building complex objects step-by-step. In this project, the Meal class is constructed using the builder pattern, where a combo meal is built by adding items like a main course, drink, and dessert.

```python
class ComboMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self):
        self.meal.add_item("Burger")

    def add_drink(self):
        self.meal.add_item("Soda")

    def add_dessert(self):
        self.meal.add_item("Ice Cream")

    def get_meal(self):
        return self.meal

```
# Example of Interaction
```githubexpressionlanguage
Enter the order type (dine-in/takeaway): dine-in
Enter customer name: Alice
Enter order ID: 1
Enter table number: 5
Enter item name (or 'done' to finish): Burger
Enter quantity for Burger: 1
Enter price for Burger: 10
Enter item name (or 'done' to finish): Fries
Enter quantity for Fries: 2
Enter price for Fries: 5
Enter item name (or 'done' to finish): done
Do you want to add more orders? (yes/no): no

All Orders:
Dine-In Order at Table 5

Text Report:
Order ID: 1
Items:
Burger - 1 @ 10 each
Fries - 2 @ 5 each
Total Cost: 20

HTML Report:
<h1>Order ID: 1</h1>
<ul>
<li>Burger - 1 @ 10 each</li>
<li>Fries - 2 @ 5 each</li>
</ul>
<p>Total Cost: 20</p>
```
---

# Results and Conclusion:
This project successfully implemented three creational design patterns:

- The Factory Method allows easy creation of different order types.
- The Singleton ensures centralized management of all orders.
- The Builder pattern makes constructing complex meals simple and manageable.

These patterns were used in the context of a restaurant order management system, making the codebase flexible, maintainable, and easy to extend. By using these patterns, the system can be easily expanded to handle more complex scenarios or new features, such as additional meal options, new order types, and different reporting methods.