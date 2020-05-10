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

        - Saving / retrieving data to/fron file

        - Update the stock of an item
            - show the list items
            - ask the user to choose and id
            - ask the user for the new stock value
            - find the item with selected id
            - update the stock
            - save changes

        - Print the Total value of the stock (sum (price * stock))

        - Remove an Item from the Catalog

        - Register a Sale
            - show the list of items
            - ask the user to choose an id
            - ask the user to provide the qnty
            - update the stock

        - Have a log of events
            - file name for the logs
            - a list for the log entries (list of string)
            - save_log
            - read_log
            - add_log_event function that receives an string
            - update existing fns to register log entries

        - Display the log of events
"""

from menu import menu, clear, header
from item import Item
import pickle
import datetime


# global vars
catalog = []
log = []
last_id = 0
data_file = 'warehouse.data'
log_file = 'log.data'

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
        global last_id
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id

        how_many = len(catalog)
        print("** Loaded " + str(how_many) + " items")
    except:
        print("** No data file found, db is empty")

def save_log():
    global log_file
    writer = open(log_file, "wb")
    pickle.dump(log, writer)
    writer.close()
    print("** Log Saved!")

def read_log():
    try:
        global log_file
        reader = open(log_file, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)

        how_many = len(log)
        print("** Loaded " + str(how_many) + " log entries")
    except:
        print("** Error loading log entries")

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
    add_log_event("NewItem", "Added item: " + str(last_id))
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
            + "|" + str(item.price).rjust(10)
            + "|" + str(item.stock).rjust(5) + "|")
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

def update_stock(opc):
    display_catalog()
    id = int(input("Select an ID:"))
    # find the item with id = id
    found = False 
    for item in catalog:
        if(item.id == id):
            found = True

            if(opc == 1):
                stock = int(input("New Stock value: "))
                item.stock = stock
                print('Stock updated!')
            else:
                sold = int(input("Number of items to sale: "))
                item.stock -= sold # decrease the stock value by the number of sold items
                print('Sale registered!')

    if(not found):
        print("Error: Selected Id does not exist, try again")

def cal_total_stock():
    total = 0
    for item in catalog:
        total += float(item.price * item.stock)
    print("Total Stock Value: $" + str(total))

# def delete_item():
#     display_catalog()
#     id = int(input("Select an ID: "))
#     for item in catalog:
#         if (id == item.id):
#             catalog.remove(item)

def delete_item():
    display_catalog()
    id = int(input("Select the id of the item to remove: "))      
    found = False
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            break
    
    if(found):
        print("Item removed from catalog")
    else:
        print("**Error, selected id is incorrect, try again")

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y %T")

def add_log_event(event_type, event_description):
    entry = get_current_time + " | " + event_type.ljust(10) + " | " + event_description
    log.append(entry)
    save_log()

# instructions
# start menu
read_catalog()
read_log()
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
    elif (opc == '4'):
        update_stock(1) # update stock
        save_catalog()
    elif (opc == '5'):
        cal_total_stock()
    elif (opc == '6'):
        delete_item()
        save_catalog()
        display_catalog()
    elif (opc == '7'):
        update_stock(2) # register sale
        save_catalog()

    input("Press enter to continue...")
