
# Creational Design Patterns  

**Author**: Tabanschi Nichita  

## Objectives:
- Study and understand the Creational Design Patterns.
- Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.
- Use some creational design patterns for object instantiation in a sample project.

## Domain Area:
The domain chosen for this project is a **Restaurant Order Management System**. This system allows customers to place dine-in or takeaway orders and handles order management, processing, and report generation (in both text and HTML formats) for each order.

## Used Design Patterns:
- **Factory Method**: Used to create different types of orders (Dine-In and Takeaway).
- **Singleton**: Ensures there is only one `OrderManager` instance, providing centralized order management.
- **Builder**: Simplifies the creation of complex meal objects (such as combo meals with a main dish, drink, and dessert).

---

## Implementation

### **Design Pattern 1: Factory Method**

The **Factory Method** pattern is applied to create different types of orders, namely Dine-In and Takeaway. A dedicated factory creates the appropriate order object based on the type specified by the user.

Code explanation:
- `OrderFactory` : An abstract base class that defines a method create_order, which subclasses must implement to create an order.
- `DineInOrderFactory` and `TakeawayOrderFactory`: These are concrete factories that implement the `create_order` method for each type of order.
- `DineInOrderFactory` takes a `table_number` as an additional parameter, as it is specific to dine-in orders.
- `TakeawayOrderFactory` simply creates a takeaway order with the provided details.
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

### **Design Pattern 2: Singleton**
The **Singleton** pattern ensures that there is only one instance of `OrderManager` throughout the application, which prevents multiple instances of the manager from being created and provides centralized control over orders.


Code Explanation:
- `_instance`: A class-level attribute that holds the single instance of `OrderManager`.
- `__new__`: The `__new__` method is overridden to control instance creation. If `_instance` is `None`, it creates a new instance and stores it in `_instance`; otherwise, it returns the existing instance.
- `__init__`: This constructor initializes the `orders` list if it hasn’t been initialized already. This list stores all orders managed by the system.
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

### **Design Pattern 3: Builder**
The **Builder** pattern is useful for constructing complex objects in a step-by-step manner. In this project, the `Meal` class is constructed using the builder pattern, allowing a combo meal to be built by adding items such as a main course, drink, and dessert.

Code Explanation:
- `Meal`: This class represents a meal with a list of items. Items can be added one by one using the `add_item` method.
- `MealBuilder`: An abstract base class that defines methods (`add_main_course`, `add_drink`, `add_dessert`) for adding items to a meal. Concrete builders should implement these methods.
- `ComboMealBuilder`: A concrete builder that constructs a specific combo meal by adding predefined items (Burger, Soda, Ice Cream).
- `MealDirector`: A director class that takes a `MealBuilder` and coordinates the construction of a complete meal by calling the appropriate builder methods in sequence.
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

---

## Example of Interaction

```plaintext
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

## Results and Conclusion:
This project successfully implemented three creational design patterns:

- The **Factory Method** simplifies the creation of different order types, making it easy to extend the application with new types of orders.
- The **Singleton** pattern provides centralized order management, ensuring only one `OrderManager` instance is used across the system.
- The **Builder** pattern offers a structured way to construct complex meal objects, allowing for flexibility in adding various meal components.

By applying these patterns, the Restaurant Order Management System achieves modularity, scalability, and ease of maintenance. These design patterns make it easier to expand the system with new features, such as additional meal options, order types, and report formats, while keeping the code organized and reusable.
