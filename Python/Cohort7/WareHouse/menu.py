import os

def menu():
    print('\n' * 5)
    print("-" * 30)
    print("      Warehouse Control")
    print("-" * 30)
    print('[1] Register Items')
    print('[2] Catalog')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Close')
    print('\n')
    print("-" * 30)

# def clear():
#     return os.system('cls' if os.name == 'nt' else 'clear')

clear = lambda: os.system('cls')
clear()

def header(title):
    clear()
    print("-" * 30)
    print(" " + title)
    print("-" * 30)