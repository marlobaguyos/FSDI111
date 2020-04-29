"""
    Program: Warehouse management system
    Functionality:
        - Repeated menu
        - Register items to the catalog
            id (auto generated)
            title
            category
            price
            stock
        - Display Catalog
        - Display items with no stock (out of stock)
"""

from menu import menu, clear, header
from item import Item


# global vars
catalog = []



# functions
def register_item():
    header("Register new Item")

    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))

    new_item = Item() # <- create instances of a class (objects)
    new_item.id = 0
    new_item.title = title
    new_item.category = cat
    new_item.price = price
    new_item.stock = stock

    catalog.append(new_item)
    print("Item created!")

def display_catalog():
    size = len(catalog)
    header("Current Catalog (" + str(size) + " items)")

    print("|" + 'ID'.rjust(3)  
        + "|" + 'Title'.ljust(30) 
        + "|" + 'Category'.ljust(15) 
        + "|" + 'Price'.rjust(10) 
        + "|" + 'Stock'.rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        print("|" + str(item.id).rjust(3)  
        + "|" + item.title.ljust(30) 
        + "|" + item.category.ljust(15) 
        + "|" + str(item.price).rjust(11) 
        + "|" + str(item.stock).rjust(8) + "|" )
        print("-" * 70)
    
def display_no_stock():
    size = len(catalog)
    header("Out of Stock (" + str(size) + " items)")

    print("|" + 'ID'.rjust(3)  
        + "|" + 'Title'.ljust(30) 
        + "|" + 'Category'.ljust(15) 
        + "|" + 'Price'.rjust(10) 
        + "|" + 'Stock'.rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        if (item.stock == 0):
            print("|" + str(item.id).rjust(3)  
            + "|" + item.title.ljust(30) 
            + "|" + item.category.ljust(15) 
            + "|" + str(item.price).rjust(11) 
            + "|" + str(item.stock).rjust(8) + "|" )
            print("-" * 70)



# instructions
# start menu
opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc = input("Please select an option: ")
    print("-" * 70)
    if(opc == '1'):
        register_item()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '3'):
        display_no_stock()

    input("Press enter to continue...")