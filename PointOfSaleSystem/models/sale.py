import uuid
class Sale:
    def __init__(self, sale_number):
        self.sale_number = sale_number
        self.items = {}  # {upc: {'item': Item, 'quantity': qty}}
        self.total_price = 0.0

    def add_item(self, item, quantity):
        if item.upc in self.items:
            self.items[item.upc]['quantity'] += quantity
        else:
            self.items[item.upc] = {'item': item, 'quantity': quantity}
        self.total_price += quantity * item.unit_price

    def remove_item(self, upc, quantity):
        if upc in self.items:
            item_data = self.items[upc]
            if quantity >= item_data['quantity']:
                self.total_price -= item_data['quantity'] * item_data['item'].unit_price
                del self.items[upc]
            else:
                item_data['quantity'] -= quantity
                self.total_price -= quantity * item_data['item'].unit_price

    def generate_receipt_number(self):
        return str(uuid.uuid4())
