"""
    Program: Warehouse management system
    Functionality:
        - Repeated menu
"""

from menu import menu, clear


def separator():
    print("-" * 30)





# start menu

opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc = input("Please select an option: ")

    input("Press enter to continue...")