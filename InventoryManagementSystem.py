
inventory = {
    "Apples": {"quantity": 10, "price": 1500},
    "Bananas": {"quantity": 20, "price": 1200},
    "Oranges": {"quantity": 15, "price": 1800}
}

def show_inventory():
    print("\nCurrent Inventory:")
    print(f"{'Item':<10} {'Quantity':<10} {'Price (UGX)':<10}")
    print("-" * 30)
    for item, details in inventory.items():
        print(f"{item:<10} {details['quantity']:<10} {details['price']:<10}")


def update_stock():
    item = input("Enter the item name to update: ")
    if item in inventory:
        new_quantity = int(input(f"Enter new quantity for {item}: "))
        inventory[item]["quantity"] = new_quantity
        print(f"{item} quantity updated to {new_quantity}.")
    else:
        print(f"{item} is not in the inventory.")


def update_price():
    item = input("Enter the item name to update price: ")
    if item in inventory:
        new_price = int(input(f"Enter new price for {item} (UGX): "))
        inventory[item]["price"] = new_price
        print(f"{item} price updated to {new_price} UGX.")
    else:
        print(f"{item} is not in the inventory.")


def add_item():
    item = input("Enter the new item name: ")
    if item in inventory:
        print(f"{item} already exists.")
    else:
        quantity = int(input(f"Enter quantity for {item}: "))
        price = int(input(f"Enter price for {item} (UGX): "))
        inventory[item] = {"quantity": quantity, "price": price}
        print(f"{item} added with quantity {quantity} and price {price} UGX.")

def delete_item():
    item = input("Enter the item name to delete: ")
    if item in inventory:
        del inventory[item]
        print(f"{item} has been deleted.")
    else:
        print(f"{item} not found in inventory.")


while True:
    print("\n--- Inventory Menu ---")
    print("1. Show Inventory")
    print("2. Update Stock Quantity")
    print("3. Update Item Price")
    print("4. Add New Item")
    print("5. Delete Item")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        update_price()
    elif choice == "4":
        add_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
