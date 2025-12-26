class Item:
    def __init__(self, upc, description, item_max_qty, order_threshold, replenishment_order_qty, item_on_hand, unit_price, order_placed):
        self.upc = upc
        self.description = description
        self.item_max_qty = float(item_max_qty)
        self.order_threshold = float(order_threshold)
        self.replenishment_order_qty = float(replenishment_order_qty)
        self.item_on_hand = float(item_on_hand)
        self.unit_price = float(unit_price)
        self.order_placed = order_placed

    def update_unit_on_hand(self, quantity):
        self.item_on_hand += quantity





