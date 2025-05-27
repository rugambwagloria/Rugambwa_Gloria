class Restaurant:
    
    def place_order(self, *args):
        
        if len(args) == 1 and isinstance(args[0], str):
            self.order_food(args[0])  # Just food item
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            self.order_food_with_drink(args[0], args[1])  # Food + drink
        elif len(args) == 1 and isinstance(args[0], list):
            self.order_combo(args[0])  # Combo meal (list of items)
        else:
            print("Invalid order")
    
    def order_food(self, item):
        print(f"Ordering: {item}")
    
    def order_food_with_drink(self, food, drink):
        print(f"Ordering: {food} with {drink}")
    
    def order_combo(self, items):
        print(f"Ordering combo meal: {', '.join(items)}")


class FancyRestaurant(Restaurant):
    def order_food(self, item):
        print(f"Ordering our exquisite: {item}")
    
    def order_combo(self, items):
        super().order_combo(items)
        print("Comes with our signature dessert!")

print("Method Resolution Order for FancyRestaurant:")
print(FancyRestaurant.mro())



simple_diner = Restaurant()
fancy_place = FancyRestaurant()

print("\nSimple diner orders:")
simple_diner.place_order("Burger")
simple_diner.place_order("Pizza", "Soda")
simple_diner.place_order(["Burger", "Fries", "Shake"])

print("\nFancy restaurant orders:")
fancy_place.place_order("Steak")
fancy_place.place_order("Salmon", "Wine")
fancy_place.place_order(["Soup", "Salad", "Bread"])