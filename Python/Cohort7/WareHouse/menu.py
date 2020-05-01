import os

def menu():
    print('\n' * 5)
    print("-" * 30)
    print("      Warehouse Control")
    print("-" * 30)
    print('[1] Register Items')
    print('[2] Catalog')
    print('[3] Display Out of Stock Items')
    print('[4] Update item stock')
    print('[5] Calculate total stock value')
    print('[6] Delete an Item')
    print('[x] - Close')
    print('\n')
    print("-" * 30)

# def clear():
#     return os.system('cls' if os.name == 'nt' else 'clear')

clear = lambda: os.system('cls')
clear()

def header(title):
    clear()
    print("-" * 70)
    print(" " + title)
    print("-" * 70)