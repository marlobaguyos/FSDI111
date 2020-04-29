import os

def menu():
    print("-" * 30)
    print("Warehouse Control")
    print("-" * 30)

    print('[1] - Add')
    print('[2] - Substract')
    print('[3] - Multiply')
    print('[4] - Divide')

    print('[x] - Close')
    print("-" * 30)

# def clear():
#     return os.system('cls' if os.name == 'nt' else 'clear')

clear = lambda: os.system('cls')
clear()