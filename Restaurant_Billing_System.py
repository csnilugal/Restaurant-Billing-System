import sys

class Bill:
    def __init__(self):
        self.items = []  # List of tuples: (item_name, unit_price, qty)
        self.gst_rate = 0.05  # 5% GST

    def add_item(self, item_name, unit_price, qty):
        self.items.append((item_name, unit_price, qty))
        print(f"Added {qty} x {item_name} - ₹{unit_price * qty}")

    def generate(self):
        print("\n" + "=" * 44)
        print(f"{'RESTAURANT BILL':^44}")
        print("=" * 44)
        print(f"{'No.':<4} {'Item':<20} {'Qty':<5} {'Price':>10}")
        print("-" * 44)

        subtotal = 0
        for i, (item_name, unit_price, qty) in enumerate(self.items, start=1):
            total_price = unit_price * qty
            subtotal += total_price
            print(f"{i:<4} {item_name:<20} {qty:<5} ₹{total_price:>9.2f}")

        gst = round(subtotal * self.gst_rate, 2)
        total = round(subtotal + gst, 2)

        print("-" * 44)
        print(f"{'Subtotal':<31} ₹{subtotal:>9.2f}")
        print(f"{'GST (5%)':<31} ₹{gst:>9.2f}")
        print("=" * 44)
        print(f"{'TOTAL':<31} ₹{total:>9.2f}")
        print("=" * 44)
        print(f"{'Thank You! Visit Again!':^44}")
        print("=" * 44 + "\n")


class Veg:
    def __init__(self, drinks, starters, meals, desserts, bill):
        self.drinks = drinks
        self.starters = starters
        self.meals = meals
        self.desserts = desserts
        self.bill = bill

    def show_subcategories(self, category_name, subcategories):
        while True:
            print(f"\n--- {category_name} Subcategories ---")
            for i, sub in enumerate(subcategories, start=1):
                print(f"{i}. {sub}")
            print("0. Back")
            print("9. Generate Bill & Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    break
                elif choice == 9:
                    self.bill.generate()
                    sys.exit()
                selected_subcat = list(subcategories.keys())[choice - 1]
                self.show_items(subcategories[selected_subcat])
            except (ValueError, IndexError):
                print("Invalid choice. Try again.")

    def show_items(self, items_dict):
        while True:
            print("\nSelect an item to add to your bill:")
            for i, (item, price) in enumerate(items_dict.items(), start=1):
                print(f"{i}. {item} - ₹{price}")
            print("0. Back")
            print("9. Generate Bill & Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    break
                elif choice == 9:
                    self.bill.generate()
                    sys.exit()
                item_list = list(items_dict.items())
                if 1 <= choice <= len(item_list):
                    selected_item, price = item_list[choice - 1]
                    qty = int(input(f"Enter quantity for {selected_item}: "))
                    self.bill.add_item(selected_item, price, qty)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")


class Restaurant(Veg):
    def __init__(self, bill):
        drinks = {
            "Tea": {"Masala Tea": 15, "Kadak Tea": 10, "Green Tea": 12},
            "Coffee": {"Filter Coffee": 20, "Cold Coffee": 30},
            "Juice": {"Orange Juice": 25, "Apple Juice": 30}
        }

        starters = {
            "Soups": {"Tomato Soup": 25, "Sweet Corn Soup": 30},
            "Manchurian": {"Veg Manchurian Dry": 50, "Veg Manchurian Gravy": 60}
        }

        meals = {
            "North Indian": {
                "Butter Roti": 12,
                "Paneer Butter Masala": 80,
                "Veg Kurma": 60
            },
            "Chinese": {
                "Veg Biryani": 90,
                "Fried Rice": 70
            },
            "Western": {
                "Pasta": 100,
                "Pizza Slice": 80
            }
        }

        desserts = {
            "Gulab Jamun": 20,
            "Ice Cream": 25,
            "Rasgulla": 25
        }

        super().__init__(drinks, starters, meals, desserts, bill)


bill = Bill()
menu = Restaurant(bill)

print("\n--- Welcome to the Restaurant ---")

while True:
    print("\nMain Menu:")
    print("1. Drinks")
    print("2. Starters")
    print("3. Meals")
    print("4. Desserts")
    print("5. Generate Bill & Exit")

    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                menu.show_subcategories("Drinks", menu.drinks)
            case 2:
                menu.show_subcategories("Starters", menu.starters)
            case 3:
                menu.show_subcategories("Meals", menu.meals)
            case 4:
                menu.show_items(menu.desserts)
            case 5:
                bill.generate()
                break
            case _:
                print("Invalid choice.")
    except ValueError:
        print("Invalid input.")