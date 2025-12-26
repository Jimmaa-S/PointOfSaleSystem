import os

def save_receipt(sale):
    if not os.path.exists("receipts"):
        os.makedirs("receipts")
    filepath = f"receipts/{sale.sale_id}.txt"
    with open(filepath, "w") as f:
        f.write(f"Receipt Number: {sale.sale_id}\n")
        for upc, data in sale.items.items():
            f.write(f"{data['item'].description}: {data['quantity']} x {data['item'].unit_price} = ${data['quantity']*data['item'].unit_price:.2f}\n")
        f.write(f"Total: ${sale.total_price:.2f}\n")
    print(f"Receipt saved: {filepath}")



