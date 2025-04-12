# from db import get_connection
# def add_sale(product_id,quantity):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("select quantity from product where id=%s", (product_id))
#     current_stock = cursor.fetchone()[0]

#     if current_stock >= quantity:
#         cursor.execute("insert into sales,(product_id,quantity) values (%s,%s)",(product_id,quantity))
#         cursor.execute("update product set quantity = quantity - %s where id =%s",(quantity,product_id))
#         conn.commit()
#         print("sale recorded successfully")
#     else:
#          print("Insufficient stock!")

#     conn.close()

# sales.py
from db import get_connection

def add_sale(product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    # Fetch current stock
    cursor.execute("SELECT quantity FROM product WHERE product_id = %s", (product_id,))

    result = cursor.fetchone()

    if result:
        current_stock = result[0]
        if current_stock >= quantity:
            cursor.execute(
                "INSERT INTO sales (product_id, quantity) VALUES (%s, %s)",
                (product_id, quantity)
            )
            cursor.execute(
                "UPDATE product SET quantity = quantity - %s WHERE product_id = %s"
,
                (quantity, product_id)
            )
            conn.commit()
            print("Sale recorded successfully")
        else:
            print("Insufficient stock!")
    else:
        print("Product not found!")

    cursor.close()
    conn.close()
