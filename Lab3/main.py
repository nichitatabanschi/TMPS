from system_facade import SystemFacade

def get_order_details():
    order_type = input("Enter the order type (dine-in/takeaway): ").strip().lower()
    customer_name = input("Enter customer name: ")
    order_id = int(input("Enter order ID: "))
    table_number = int(input("Enter table number: ")) if order_type == "dine-in" else None
    items = []
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        items.append((item_name, quantity, price))
    return order_type, order_id, customer_name, items, table_number

def main():
    facade = SystemFacade()

    while True:
        order_type, order_id, customer_name, items, table_number = get_order_details()
        order = facade.create_order(order_type, order_id, customer_name, items, table_number)
        print(facade.generate_report(order, "text"))
        print("Do you want to add another order? (yes/no): ")
        if input().strip().lower() != "yes":
            break

if __name__ == "__main__":
    main()
