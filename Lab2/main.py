from system_facade import SystemFacade


def get_order_details():
    order_type = input("Enter the order type (dine-in/takeaway): ").strip().lower()
    customer_name = input("Enter customer name: ")
    order_id = int(input("Enter order ID: "))
    table_number = int(input("Enter table number: ")) if order_type == "dine-in" else None
    return order_type, order_id, customer_name, table_number


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


def main():
    facade = SystemFacade()

    while True:
        order_type, order_id, customer_name, table_number = get_order_details()
        items = get_order_items()

        order = facade.create_order(order_type, order_id, customer_name, items, table_number)

        print("\nOrder Reports:")
        print(facade.generate_report(order, format="text"))
        print(facade.generate_report(order, format="html"))

        more_orders = input("Do you want to add more orders? (yes/no): ").strip().lower()
        if more_orders != 'yes':
            break

    print("\nAll Orders:")
    facade.list_all_orders()


if __name__ == "__main__":
    main()
