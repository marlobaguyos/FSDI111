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
import pickle


# global vars
catalog = []
last_id = 0
data_file = 'warehouse.data'


def save_catalog():
    global data_file
    # creat file (overwrite), open it to Write Binary
    writer = open(data_file, "wb")
    pickle.dump(catalog, writer)
    writer.close()
    print("** Data Saved!!")


def read_catalog():
    try:
        global data_file
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        how_many = len(catalog)
        print("** Loaded " + str(how_many) + " items")
    except:
        print("** No data file found, db is empty")

# data
# total item
# id|title|asd|asda


# functions
def register_item():
    global last_id
    header("Register new Item")

    title = input("New item title: ")
    cat = input("New item category: ")
    price = float(input("New item price: "))
    stock = int(input("New item stock: "))

    new_item = Item()  # <- create instances of a class (objects)
    last_id += 1 
    new_item.id = last_id
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
            + "|" + str(item.stock).rjust(8) + "|")
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
                + "|" + str(item.stock).rjust(8) + "|")
            print("-" * 70)


# instructions
# start menu
read_catalog()
input("Press enter to continue...")

opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc = input("Please select an option: ")
    print("-" * 70)
    if(opc == '1'):
        register_item()
        save_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '3'):
        display_no_stock()

    input("Press enter to continue...")
