class Bill:
    def __init__(self):
        self.items = []  # List of tuples: (item, price)
        self.gst_rate = 0.05  # 5% GST

    def add_item(self, item_name, price):
        self.items.append((item_name, price))

    def generate(self):
        print("\n--- Final Bill ---")
        subtotal = 0
        for i, (item, price) in enumerate(self.items, start=1):
            print(f"{i}. {item} - ₹{price}")
            subtotal += price
        gst = subtotal * self.gst_rate
        total = subtotal + gst
        print(f"\nSubtotal: ₹{subtotal}")
        print(f"GST (5%): ₹{gst}")
        print(f"Total Bill: ₹{total}")
        print("\n--- Thank You! Visit Again ---\n")


class Veg:
    def __init__(self, tea, coffee, soup, manchuri, dosa, roti, gravey, rice, desserts, bill):
        self.tea = tea
        self.coffee = coffee
        self.soup = soup
        self.manchuri = manchuri
        self.dosa = dosa
        self.roti = roti
        self.gravey = gravey
        self.rice = rice
        self.desserts = desserts
        self.bill = bill

    def show_items(self, category_dict):
        while True:
            print("\nSelect an item to add to your bill:")
            for i, (item, price) in enumerate(category_dict.items(), start=1):
                print(f"{i}. {item} - ₹{price}")
            print("0. Back")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    break
                item_list = list(category_dict.items())
                if 1 <= choice <= len(item_list):
                    selected_item, price = item_list[choice - 1]   #unpacking
                    self.bill.add_item(selected_item, price)
                    print(f"You selected: {selected_item} - ₹{price}")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def morning(self):
        print("\n--- Morning Menu ---")
        combined = {**self.tea, **self.coffee, **self.dosa}  #packing
        self.show_items(combined)

    def starters(self):
        print("\n--- Starters ---")
        combined = {**self.soup, **self.manchuri}
        self.show_items(combined)

    def meal(self):
        print("\n--- Veg Meal ---")
        combined = {**self.roti, **self.gravey, **self.rice}
        self.show_items(combined)

    def dessert(self):
        print("\n--- Desserts ---")
        self.show_items(self.desserts)


class Non_Veg(Veg):
    def __init__(self, tea, coffee, soup, manchuri, dosa, roti, gravey, rice, desserts,
                 Nroti, Ngravey, Nrice, bill):
        super().__init__(tea, coffee, soup, manchuri, dosa, roti, gravey, rice, desserts, bill)
        self.Nroti = Nroti
        self.Ngravey = Ngravey
        self.Nrice = Nrice

    def NVmeal(self):
        print("\n--- Non-Veg Meal ---")
        combined = {**self.Nroti, **self.Ngravey, **self.Nrice}
        self.show_items(combined)


class Restaurant(Non_Veg):
    def __init__(self, bill):
        super().__init__(
            tea={"Masala Tea": 15, "Kadak Tea": 10, "Normal Tea": 8},
            coffee={"Filter Coffee": 20, "Cold Coffee": 30},
            soup={"Tomato Soup": 25, "Sweet Corn Soup": 30},
            manchuri={"Veg Manchurian Dry": 50, "Veg Manchurian Gravy": 60},
            dosa={"Masala Dosa": 40, "Set Dosa": 35, "Plain Dosa": 30},
            roti={"Butter Roti": 12, "Plain Roti": 10},
            gravey={"Paneer Butter Masala": 80, "Veg Kurma": 60},
            rice={"Veg Biryani": 90, "Fried Rice": 70},
            desserts={"Gulab Jamun": 20, "Ice Cream": 25, "Rasgulla": 25},
            Nroti={"Tandoori Roti": 15},
            Ngravey={"Chicken Curry": 100, "Butter Chicken": 120},
            Nrice={"Chicken Biryani": 110, "Mutton Biryani": 150},
            bill=bill
        )


# Body of restaurant menu (This is displayed to user)

bill = Bill()
menu = Restaurant(bill)

print("\n--- Welcome to the Restaurant ---")

while True:
    print("\nMain Menu:")
    print("1. Veg")
    print("2. Non-Veg")
    print("3. Generate Bill & Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    match choice:
        case 1:
            while True:
                print("\n--- Veg Menu ---")
                print("1. Morning")
                print("2. Starters")
                print("3. Meal")
                print("4. Dessert")
                print("0. Back")
                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match sub_choice:
                    case 1:
                        menu.morning()
                    case 2:
                        menu.starters()
                    case 3:
                        menu.meal()
                    case 4:
                        menu.dessert()
                    case 0:
                        break
                    case _:
                        print("Invalid option")

        case 2:
            while True:
                print("\n--- Non-Veg Menu ---")
                print("1. Morning")
                print("2. Starters")
                print("3. Meal")
                print("4. Dessert")
                print("0. Back")
                try:
                    sub_choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                match sub_choice:
                    case 1:
                        menu.morning()
                    case 2:
                        menu.starters()
                    case 3:
                        menu.NVmeal()
                    case 4:
                        menu.dessert()
                    case 0:
                        break
                    case _:
                        print("Invalid option")

        case 3:
            bill.generate()
            break

        case _:
            print("Invalid main choice.")
