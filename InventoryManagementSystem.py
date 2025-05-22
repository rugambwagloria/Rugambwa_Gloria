class InventoryManager:
    def __init__(self):
        self.inventory = {
            'laptop': {'price': 1000000, 'quantity': 15, 'category': 'Electronics'},
            'mouse': {'price': 95000, 'quantity': 50, 'category': 'Electronics'},
            'keyboard': {'price': 237500, 'quantity': 30, 'category': 'Electronics'},
            'desk_chair': {'price': 240000, 'quantity': 8, 'category': 'Furniture'},
            'notebook': {'price': 10800, 'quantity': 100, 'category': 'Stationery'},
            'pen': {'price': 2000, 'quantity': 200, 'category': 'Stationery'}
        }

    def show_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 60)
        print("INVENTORY MANAGEMENT SYSTEM".center(60))
        print("=" * 60)
        print("1. Show All Items")
        print("2. Show Items by Category")
        print("3. Search Item")
        print("4. Add New Item")
        print("5. Update Quantity")
        print("6. Update Price")
        print("7. Remove Item")
        print("8. Show Low Stock Items")
        print("9. Show Summary")
        print("0. Exit")
        print("=" * 60)
        print("\nPress Enter to continue...")
    def show_all_items(self):
        """Display all items in inventory"""
        print("\nALL ITEMS:")
        print("=" * 90)
        header = f"{'Item':<20} {'Price (UGX)':>15} {'Qty':>10} {'Category':>15} {'Total Value (UGX)':>25}"
        print(header)
        print("-" * 90)
        
        total_value = 0
        for name, item in self.inventory.items():
            value = item['price'] * item['quantity']
            total_value += value
            row = f"{name:<20} {item['price']:>15,.0f} {item['quantity']:>10} {item['category']:>15} {value:>25,.0f}"
            print(row)
        
        print("-" * 90)
        print(f"{'TOTAL INVENTORY VALUE:':<60} {total_value:>25,.0f} UGX")
        print("=" * 90)

    def show_items_by_category(self):
        """Group and display items by category"""
        categories = {}
        for name, item in self.inventory.items():
            categories.setdefault(item['category'], []).append((name, item))
        
        print("\nITEMS BY CATEGORY:")
        print("=" * 70)
        
        for category, items in categories.items():
            print(f"\n{category.upper()}:")
            print(f"{'Item':<20} {'Price (UGX)':>15} {'Qty':>10} {'Value (UGX)':>20}")
            print("-" * 65)
            cat_total = 0
            for name, item in items:
                value = item['price'] * item['quantity']
                cat_total += value
                print(f"{name:<20} {item['price']:>15,.2f} {item['quantity']:>10} {value:>20,.2f}")
            print(f"{'Category Total:':<45} {cat_total:>20,.2f} UGX")

    def search_item(self):
        """Search for items by name"""
        search = input("Enter item name to search: ").lower().strip()
        results = [(name, item) for name, item in self.inventory.items() if search in name.lower()]
        
        if results:
            print(f"\nSearch Results for '{search}':")
            print(f"{'Item':<20} {'Price (UGX)':>15} {'Qty':>10} {'Category':>15}")
            print("-" * 60)
            for name, item in results:
                print(f"{name:<20} {item['price']:>15,.2f} {item['quantity']:>10} {item['category']:>15}")
        else:
            print(f"No items found matching '{search}'")

    def add_item(self):
        """Add a new item to inventory"""
        name = input("Enter item name: ").lower().strip()
        if name in self.inventory:
            print(f"Item '{name}' already exists!")
            return
        try:
            price = float(input("Enter price in UGX: "))
            qty = int(input("Enter quantity: "))
            category = input("Enter category: ").title().strip()
            self.inventory[name] = {'price': price, 'quantity': qty, 'category': category}
            print(f"Item '{name}' added successfully!")
        except ValueError:
            print("Invalid input! Use numbers for price and quantity.")

    def update_quantity(self):
        """Update item quantity"""
        name = input("Enter item name: ").lower().strip()
        if name not in self.inventory:
            print(f"Item '{name}' not found!")
            return
        print(f"Current quantity: {self.inventory[name]['quantity']}")
        try:
            action = input("Add or Set quantity? (a/s): ").lower().strip()
            new_qty = int(input("Enter quantity: "))
            if action == 'a':
                self.inventory[name]['quantity'] += new_qty
            elif action == 's':
                self.inventory[name]['quantity'] = new_qty
            else:
                print("Invalid action!")
                return
            print(f"Updated quantity: {self.inventory[name]['quantity']}")
        except ValueError:
            print("Invalid input! Enter a number.")

    def update_price(self):
        """Update item price"""
        name = input("Enter item name: ").lower().strip()
        if name not in self.inventory:
            print(f"Item '{name}' not found!")
            return
        print(f"Current price: {self.inventory[name]['price']:,.2f} UGX")
        try:
            new_price = float(input("Enter new price in UGX: "))
            self.inventory[name]['price'] = new_price
            print(f"Price updated to {new_price:,.2f} UGX")
        except ValueError:
            print("Invalid price! Enter a number.")

    def remove_item(self):
        """Remove item from inventory"""
        name = input("Enter item name to remove: ").lower().strip()
        if name in self.inventory:
            confirm = input(f"Remove '{name}'? (y/n): ").lower().strip()
            if confirm == 'y':
                del self.inventory[name]
                print(f"Item '{name}' removed!")
            else:
                print("Removal cancelled.")
        else:
            print(f"Item '{name}' not found!")

    def show_low_stock(self):
        """Show items with low stock"""
        try:
            threshold = int(input("Enter low stock threshold: "))
        except ValueError:
            print("Invalid input! Using default threshold of 10.")
            threshold = 10
        
        low_stock = [(name, item) for name, item in self.inventory.items() if item['quantity'] <= threshold]
        
        if low_stock:
            print(f"\nLOW STOCK ITEMS (≤ {threshold}):")
            print(f"{'Item':<20} {'Qty':>10} {'Price (UGX)':>15} {'Category':>15}")
            print("-" * 60)
            for name, item in low_stock:
                print(f"{name:<20} {item['quantity']:>10} {item['price']:>15,.2f} {item['category']:>15}")
        else:
            print(f"No items with stock ≤ {threshold}")

    def show_summary(self):
        """Display inventory summary"""
        total_items = len(self.inventory)
        total_qty = sum(item['quantity'] for item in self.inventory.values())
        total_value = sum(item['price'] * item['quantity'] for item in self.inventory.values())
        categories = sorted({item['category'] for item in self.inventory.values()})
        
        print("\nINVENTORY SUMMARY:")
        print("=" * 60)
        print(f"Total Items: {total_items}")
        print(f"Total Quantity: {total_qty}")
        print(f"Total Value: {total_value:,.2f} UGX")
        print(f"Categories: {len(categories)}")
        print(f"Category List: {', '.join(categories)}")
        print("=" * 60)

    def run(self):
        """Main program loop"""
        print("Welcome to Inventory Management System!")
        while True:
            self.show_menu()
            try:
                choice = input("\nEnter choice (0-9): ").strip()
                if choice == '1':
                    self.show_all_items()
                elif choice == '2':
                    self.show_items_by_category()
                elif choice == '3':
                    self.search_item()
                elif choice == '4':
                    self.add_item()
                elif choice == '5':
                    self.update_quantity()
                elif choice == '6':
                    self.update_price()
                elif choice == '7':
                    self.remove_item()
                elif choice == '8':
                    self.show_low_stock()
                elif choice == '9':
                    self.show_summary()
                elif choice == '0':
                    print("\nThank you! Goodbye!")
                    break
                else:
                    print("Invalid choice! Enter 0-9.")
                input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                print("\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                input("Press Enter to continue...")


if __name__ == "__main__":
    system = InventoryManager()
    system.run()
