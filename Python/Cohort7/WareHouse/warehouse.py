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

from menu import menu, clear

# global vars

# functions
def register_item():

    title = input("New item title: ")
    cat = input("New item category: ")
    price = input("New item price: ")
    stock = input("New item stock: ")


# start menu

opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc = input("Please select an option: ")
    if(opc == '1'):
        register_item()

    input("Press enter to continue...")