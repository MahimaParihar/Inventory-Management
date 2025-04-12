from db import get_connection
def stock_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, quantity, price FROM products")
    rows = cursor.fetchall()
    print("ID | Name | Category | Quantity | Price")
    for row in rows:
        print(row)
    conn.close()

def low_stock_alert(threshold=5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity FROM products WHERE quantity < %s", (threshold,))
    rows = cursor.fetchall()
    print("\n Low Stock Products:")
    for row in rows:
        print(f"Product: {row[0]} | Qty: {row[1]}")
    conn.close()
