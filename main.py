from product import add_product
from purchase import add_purchase
from sales import add_sale

def main():
    while True:
        print("\n INVENTORY CLI Menu")
        print("1. add product")
        print("2. add purchase")
        print("3. add sale")
        print("0 exit")

        choice = input("choose an option:")
        if (choice == "1"):
            name = input("Name:")
            category = input("Category:")
            quantity = int(input("Quantity:"))
            price = float(input("Price:"))
            add_product(name, category, quantity, price)

        elif (choice == "2"):
            pid = int(input("Product ID: "))
            qty = int(input("Purchase Quantity: "))
            add_purchase(pid, qty)
        elif choice == '3':
            pid = int(input("Product ID: "))
            qty = int(input("Sale Quantity: "))
            add_sale(pid, qty)
        elif choice == '0':
            break
        else:
            print(" Invalid Choice")
        
if __name__ == "__main__":
         main()



