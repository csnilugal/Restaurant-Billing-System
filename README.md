# 🍽️ Restaurant Billing System (Python – Console App)

This project is a **menu-driven restaurant billing system** built using Python.  
It allows customers to select items from various categories (Drinks, Starters, Meals, Desserts), add quantities, and automatically generates a formatted bill with GST.

## 📌 Features

- Interactive **console-based menu system**
- Organized categories and subcategories  
- Add items with dynamic quantity input  
- Auto-calculated **subtotal, GST (5%)**, and final total  
- Nicely formatted and readable bill output  
- Graceful exit with bill generation at any point  

## 🧩 Project Structure

```
Bill Class
 ├── add_item()    # Adds item entry to the bill
 └── generate()    # Prints formatted bill

Veg Class
 ├── show_subcategories()   # Navigate nested menus
 └── show_items()           # Show items & take quantity

Restaurant Class (inherits Veg)
 └── Defines all menu data (drinks, starters, meals, desserts)

Main Program Loop
 └── Displays menu and interacts with user
```

## 🚀 How to Run

1. Save the file as **restaurant.py**
2. Run it using:

```bash
python3 restaurant.py
```

3. Follow the prompts on the screen to select items and generate the bill.

## 📋 Example Output

```
============================================
                RESTAURANT BILL             
============================================
No.  Item                 Qty        Price
--------------------------------------------
1    Masala Tea           2       ₹   30.00
2    Veg Biryani          1       ₹   90.00
--------------------------------------------
Subtotal                          ₹  120.00
GST (5%)                          ₹    6.00
============================================
TOTAL                             ₹  126.00
============================================
         Thank You! Visit Again!         
============================================
```

## 🔧 Requirements

- Python 3.6+
- No external libraries required

## 📁 Future Improvements

- Add discount options  
- Add support for take-away vs dine-in  
- Save bill as PDF or text file  
- Add admin mode to customize menu items  
