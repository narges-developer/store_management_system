# ===========================================
# Project: Store management system
# Description:
# A simple program about store management 
# system.
#
# Concepts Used:
# - Variables
# - List
# - Dictionary
# - for loop
# - while loop
# - Functions (def)
# - if / elif / else
# - input
# - int
# - return
# - global
# ===========================================
products = {
    1: {"name": "Keyboard", "price": 500000, "stock": 5},
    2: {"name": "Mouse", "price": 250000, "stock": 10}
}

total_sales = 0

def show_products():
    for product in products:
        print("ID: ", product)
        print("Name:", products[product]["name"])
        print("Price:", products[product]["price"])
        print("Stock:", products[product]["stock"])
        print("------------------")

def add_product():
    product_id = int(input("Enter product id: "))
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price:"))
    product_stock = int(input("Enter product stock:"))
    if product_id in products:
        print("Product ID already exists.")
    else:
        products.update({
            product_id : {
                "name": product_name,
                "price": product_price,
                "stock": product_stock
            }
        })

def search_product():
    search_name = input("Enter product name: ")
    found = False
    for product in products:
        if products[product]["name"] == search_name:
            print("ID: ", product)
            print("Name:", products[product]["name"])
            print("Price:", products[product]["price"])
            print("Stock:", products[product]["stock"])
            found = True
    if not found:
        print("Product not found.")

def buy_product():
    product_id = int(input("Enter product id: "))
    product_quantity = int(input("Enter quantity:"))
    if product_id in products:
        print("Product found.")
    else:
        print("Product not found.")
        return
    if product_quantity <= 0:
        print("Quantity must be positive.")
        return
    if product_quantity > products[product_id]["stock"]:
        print("Not enough stock.")
        return
    total_price = product_quantity * products[product_id]["price"]
    print("Total price: ", total_price)
    products[product_id]["stock"] -= product_quantity
    global total_sales
    total_sales += total_price

def add_stock():
    product_id = int(input("Enter product id: "))
    new_stock = int(input("Enter quantity to add:"))
    if product_id in products:
        print("Product found.")
    else:
        print("Product not found.")
        return
    if new_stock <= 0 :
        print("Stock must be positive.")
        return 
    products[product_id]["stock"] += new_stock
    print("Stock added successfully.")
    print("New stock: ",products[product_id]["stock"])

def show_total_sales():
    print("Total sales: ",total_sales)

menu = [
    "1. Show products",
    "2. Add product",
    "3. Search product",
    "4. Buy product",
    "5. Add stock",
    "6. Show total sales",
    "7. Exit"
]
def main():
    while True:
        for item in menu:
            print(item)
        user_selection = int(input("Enter the number corresponding to your choice: "))  
        if user_selection == 1:
            show_products()
            print("-----------------------")
        elif user_selection == 2:
            add_product()
            print("-----------------------")
        elif user_selection == 3:
            search_product()
            print("-----------------------")
        elif user_selection == 4:
            buy_product()
            print("-----------------------")
        elif user_selection == 5:
            add_stock()
            print("-----------------------")
        elif user_selection == 6:
            show_total_sales()
            print("-----------------------")
        elif user_selection == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
main()