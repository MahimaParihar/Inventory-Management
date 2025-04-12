from db import get_connection
def add_product(name, category, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()

    query = "insert into product (name, category, quantity, price) values (%s, %s, %s, %s)"

    cursor.execute(query, (name, category, quantity,price))
    conn.commit()
    print("Product added successfully")
    cursor.close()
    conn.close()