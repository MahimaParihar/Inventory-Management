# from db import get_connection 

# def add_purchase(product_id, quantity):
#     conn = get_connection()
#     cursor = conn.cursor()
#     insert_query = "insert into purchase (product_id, quantity) values(%s, %s)"
#     cursor.execute(insert_query,(product_id, quantity))

#     update_query = "UPDATE product SET quantity = quantity + %s WHERE product_id = %s"
#     cursor.execute(update_query,(quantity,product_id))

#     result = cursor.execute("select * from purchase")
#     print(result)
#     conn.commit()
#     conn.close()


from db import get_connection 

def add_purchase(product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = "INSERT INTO purchase (product_id, quantity) VALUES (%s, %s)"
    cursor.execute(insert_query, (product_id, quantity))

    update_query = "UPDATE product SET quantity = quantity + %s WHERE product_id = %s"
    cursor.execute(update_query, (quantity, product_id))

    conn.commit()  # ✅ Commit before doing SELECT

    # Display all purchases (optional)
    cursor.execute("SELECT * FROM purchase")
    all_purchases = cursor.fetchall()
    for purchase in all_purchases:
        print(purchase)

    cursor.close()
    conn.close()
