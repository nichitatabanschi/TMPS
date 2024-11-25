from order import DineInOrderFactory, TakeawayOrderFactory

class OrderAdapter:
    def __init__(self, external_order):
        self.external_order = external_order

    def to_internal_order(self):
        order_id = self.external_order["id"]
        customer_name = self.external_order["customer_name"]
        items = [(item["name"], item["quantity"], item["price"]) for item in self.external_order["items"]]
        order_type = self.external_order.get("order_type", "takeaway")

        if order_type == "dine-in":
            table_number = self.external_order.get("table_number", 0)
            dine_in_factory = DineInOrderFactory(table_number)
            order = dine_in_factory.create_order(order_id, customer_name)
        else:
            takeaway_factory = TakeawayOrderFactory()
            order = takeaway_factory.create_order(order_id, customer_name)

        order.items = items
        return order
