# Lab Report: Behavioral and Structural Design Patterns in Python

## Course: Software Engineering  
**Student Name**: [Tabanschi Nichita]  
**Lab Topic**: Integration of Behavioral and Structural Design Patterns in a Python-based System

---

## **Objective**

The goal of this lab was to extend an existing Python project by implementing at least one **behavioral design pattern** alongside previously implemented **structural design patterns**. The focus was on creating a functional and flexible system while demonstrating proficiency in software design principles.

---

## **Introduction**

Design patterns provide reusable solutions to common problems in software design. 

- **Structural Patterns** focus on simplifying the relationships between entities. These were applied in the project to handle order management, cost calculation, and data adaptation.
  
- **Behavioral Patterns** aim to manage interactions between objects in a system. These were used to enhance communication and ensure that the system components remained loosely coupled.

The resulting system simulates an **Order Management System** for restaurants or takeaways, allowing for:
- Order creation (dine-in or takeaway).
- Cost calculation (with optional taxes or service charges).
- Reporting (in text or HTML formats).
- Integration of external orders into the system.

---

## **Design Patterns Implemented**

### 1. **Observer Pattern** (Behavioral)
   - **Purpose**: To enable automatic notifications to observers when a new order is added.
   - **Implementation**:  
      - **Subject**: `OrderManager`, which manages the list of orders.  
      - **Observers**: `LoggingObserver` (logs new orders) and `ReportGeneratorObserver` (generates reports for new orders).  
      - **Usage**: When an order is added, all registered observers are notified.

```python
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
```


---

### 2. **Factory Method Pattern** (Creational)
   - **Purpose**: To create orders dynamically based on the type (Dine-in or Takeaway).
   - **Implementation**:  
      - Abstract class `OrderFactory` defines a method for creating orders.  
      - Concrete classes `DineInOrderFactory` and `TakeawayOrderFactory` implement specific order creation logic.  
   - **Usage**: Centralized order creation through factories ensures consistency and scalability.

---

### 3. **Decorator Pattern** (Structural)
   - **Purpose**: To dynamically add tax and service charge functionalities to the cost calculation without modifying the existing calculation logic.
   - **Implementation**:  
      - Base class `OrderCostDecorator` provides a foundation for extending cost calculations.  
      - `TaxDecorator` and `ServiceChargeDecorator` add specific functionalities.
   - **Usage**: These decorators wrap around the `RegularCostCalculator` for flexible and modular enhancements.

---

### 4. **Adapter Pattern** (Structural)
   - **Purpose**: To adapt external order data into the system's internal structure.
   - **Implementation**:  
      - `OrderAdapter` converts data from an external order dictionary into internal `Order` objects.
   - **Usage**: This ensures compatibility between external systems and the order management system.

---

## **System Features**

- **Order Types**: Support for dine-in and takeaway orders.
- **Cost Calculation**: Supports regular cost calculation, with optional tax and service charges.
- **Reporting**: Generates detailed reports in both text and HTML formats.
- **Observer Notifications**: Logs actions and generates reports automatically when new orders are added.
- **External Order Integration**: Adapts external data seamlessly into the system.

---

## **Implementation Details**

### **Modules and Classes**

#### **1. cost_calculator.py**
- Implements the **Strategy** for regular and discounted cost calculations.

#### **2. cost_decorator.py**
- Contains decorators for tax and service charge functionalities.

#### **3. order.py**
- Defines abstract and concrete classes for order types and factories.

#### **4. order_adapter.py**
- Converts external order formats into internal `Order` objects.

#### **5. order_manager.py**
- Implements the **Singleton Pattern** for managing the list of orders and registering observers.

#### **6. observer.py**
- Defines observer classes that react to changes in the order system.

#### **7. system_facade.py**
- Provides a simplified interface for creating orders, calculating costs, and generating reports.

#### **8. report_generator.py**
- Generates text and HTML reports for orders.

#### **9. main.py**
- The entry point of the application, demonstrating end-to-end functionality.

---



### Sample Run

#### **Input**:
```
Enter the order type (dine-in/takeaway): dine-in
Enter customer name: John Doe
Enter order ID: 101
Enter table number: 5
Enter item name (or 'done' to finish): Pizza
Enter quantity: 2
Enter price: 12.5
Enter item name (or 'done' to finish): done
```

#### **Output**:
```
Order ID: 101
Items:
Pizza - 2 @ 12.5 each
Total Cost: 25.0
Report saved in text and HTML formats.
```

---

## **Conclusion**

This lab project demonstrates the practical application of design patterns to enhance the flexibility, maintainability, and extensibility of software systems. The **Observer Pattern** effectively enables automated actions in response to system events, while structural patterns like **Factory**, **Decorator**, and **Adapter** streamline object creation, dynamic behavior addition, and external system integration, respectively.

This lab highlighted the importance of using appropriate design patterns to address specific challenges, resulting in a well-structured and highly adaptable order management system.

---

