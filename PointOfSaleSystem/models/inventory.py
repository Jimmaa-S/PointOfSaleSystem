import csv
from models.item import Item
from models.sale import Sale
import uuid

class Inventory:
    def __init__(self):
        self.items = {}
        self.sales = {}  # {sale_number: Sale}
        self.current_sale = None
        self.sale_counter = 1

    def load_items(self, filepath="data/RetailStoreItemData.txt"):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 8:  # Skip invalid rows
                    continue
                upc, desc, max_qty, threshold, reorder_qty, qty, price, order_placed = row[:8]
                item = Item(upc, desc, max_qty, threshold, reorder_qty, qty, price, order_placed)
                self.items[upc] = item

    def start_sale(self):
        sale = Sale(self.sale_counter)
        self.sale_counter += 1
        self.current_sale = sale
        print("New sale started.")
        while True:
            upc = input("Enter UPC of the item (or 'done' to finish): ")
            if upc.lower() == 'done':
                break
            item = self.items.get(upc)
            if not item:
                print("Item not found. Try again.")
                continue
            qty = int(input("Enter quantity: "))
            if 0 < qty <= item.item_on_hand:
                sale.add_item(item, qty)
                item.update_unit_on_hand(-qty)
                print(f"{qty} {item.description}(s) added.")
                print(f"Running Total: ${sale.total_price:.2f}\n")
            else:
                print("Invalid quantity or insufficient stock.")
        self.sales[sale.sale_number] = sale
        print(f"Receipt Number: {sale.sale_number}")
        print(f"Total: ${sale.total_price:.2f}")
        self.current_sale = None

    def return_sale(self):
        receipt_number = int(input("Enter Receipt Number: "))
        sale = self.sales.get(receipt_number)
        if not sale:
            print("Sale not found.")
            return
        print("Return Options:\n1: Return Single Item\n2: Return All Items")
        option = input("Select option: ")
        if option == '1':
            upc = input("Enter UPC of item to return: ")
            item_data = sale.items.get(upc)
            if not item_data:
                print("Item not found in sale.")
                return
            qty = int(input("Enter quantity to return: "))
            if 0 < qty <= item_data['quantity']:
                sale.remove_item(upc, qty)
                item_data['item'].update_unit_on_hand(qty)
                print(f"Return Amount: ${qty * item_data['item'].unit_price:.2f}")
            else:
                print("Invalid quantity.")
        elif option == '2':
            confirm = input("Are you sure you want to return all items? (Y/N): ")
            if confirm.upper() == 'Y':
                for upc, item_data in list(sale.items.items()):
                    item_data['item'].update_unit_on_hand(item_data['quantity'])
                print(f"Return Amount: ${sale.total_price:.2f}")
                sale.items.clear()
            else:
                print("Return cancelled.")






