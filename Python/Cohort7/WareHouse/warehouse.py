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
    header("Current Catalog")

    size = len(catalog)
    print("there are: " + str(size) + " items")

# instructions
# start menu
opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc = input("Please select an option: ")
    print("-" * 30)
    if(opc == '1'):
        register_item()
    elif (opc == '2'):
        display_catalog()

    input("Press enter to continue...")