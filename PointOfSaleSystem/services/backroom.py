class Backroom:
    @staticmethod
    def inventory_report(inventory):
        print("Inventory Report:")
        for upc, item in inventory.items.items():
            print(f"UPC: {upc}, Name: {item.description}, On Hand: {item.item_on_hand}, Threshold: {item.order_threshold}")

    @staticmethod
    def daily_sales_report(inventory):
        print("Daily Sales Report:")
        total_sales = 0
        for sale_number, sale in inventory.sales.items():
            print(f"\nSale {sale_number}:")
            for upc, data in sale.items.items():
                item = data['item']
                qty = data['quantity']
                total = item.unit_price * qty
                total_sales += total
                print(f"UPC: {upc}, {item.description}, Quantity: {qty}, Total: ${total:.2f}")
        print(f"\nTotal Sales Today: ${total_sales:.2f}")




