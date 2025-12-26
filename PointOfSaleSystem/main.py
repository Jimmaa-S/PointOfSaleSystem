from models.security import Security
from models.inventory import Inventory
from services.backroom import Backroom

security = Security()
if not security.login():
    exit()

inventory = Inventory()
inventory.load_items()

while True:
    print("\nOptions:\n1: New Sale\n2: Return Item/s\n3: Backroom Operations\n9: Exit")
    option = input("Select option: ")
    if option == '1':
        inventory.start_sale()
    elif option == '2':
        inventory.return_sale()
    elif option == '3':
        print("Backroom Options:\n1: Inventory Report\n2: Daily Sales Report")
        b_option = input("Select: ")
        if b_option == '1':
            Backroom.inventory_report(inventory)
        elif b_option == '2':
            Backroom.daily_sales_report(inventory)
        else:
            print("Invalid option.")
    elif option == '9':
        print("Exiting POS System.")
        break
    else:
        print("Invalid option.")
