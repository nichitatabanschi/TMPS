from order import DineInOrderFactory, TakeawayOrderFactory
from cost_calculator import RegularCostCalculator, DiscountedCostCalculator
from report_generator import TextReportGenerator, HTMLReportGenerator
from order_manager import OrderManager
from meal_builder import ComboMealBuilder, MealDirector


# Function to take user input for an order
def get_order_details():
    order_type = input("Enter the order type (dine-in/takeaway): ").strip().lower()
    customer_name = input("Enter customer name: ")
    order_id = int(input("Enter order ID: "))

    # Create the order based on the type
    if order_type == 'dine-in':
        table_number = int(input("Enter table number: "))
        dine_in_factory = DineInOrderFactory(table_number)
        order = dine_in_factory.create_order(order_id, customer_name)
    elif order_type == 'takeaway':
        takeaway_factory = TakeawayOrderFactory()
        order = takeaway_factory.create_order(order_id, customer_name)
    else:
        print("Invalid order type. Defaulting to takeaway.")
        takeaway_factory = TakeawayOrderFactory()
        order = takeaway_factory.create_order(order_id, customer_name)

    return order


# Function to get order items from the user
def get_order_items():
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {item_name}: "))
        price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, quantity, price))
    return items


# Main program
def main():
    # Singleton to manage orders
    order_manager = OrderManager()

    while True:
        # Get order details from the user
        order = get_order_details()

        # Get the items for this order
        order.items = get_order_items()

        # Add the order to the order manager
        order_manager.add_order(order)

        # Ask if the user wants to add more orders
        more_orders = input("Do you want to add more orders? (yes/no): ").strip().lower()
        if more_orders != 'yes':
            break

    # List all orders
    print("\nAll Orders:")
    order_manager.list_orders()

    # Calculate total cost using RegularCostCalculator
    regular_calculator = RegularCostCalculator()

    # For each order, calculate and display the total cost
    for order in order_manager.orders:
        total_cost = regular_calculator.calculate_total(order)

        # Generate a text report
        text_report_generator = TextReportGenerator()
        print("\nText Report:")
        print(text_report_generator.generate_report(order, total_cost))

        # Generate an HTML report
        html_report_generator = HTMLReportGenerator()
        print("\nHTML Report:")
        print(html_report_generator.generate_report(order, total_cost))


if __name__ == "__main__":
    main()
