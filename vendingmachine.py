# Import modules  
import time 
from rich.console import Console
from rich.table import Table
from rich import print

# Header
print('''[bright_magenta]
                                                  █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
                                                  ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄
      [/bright_magenta]''')

# Welcome prompt
print('\t\t\t\t\t\tWelcome! Enjoy a quick snack or drink from my vending machine :)')

# Vending machine items, prices, and stocks
menu = {
    '\n/// snacks ///': {
        'S1': {'Item': 'Lays', 'Price': 2.00, 'Stock': 10},
        'S2': {'Item': 'Doritos', 'Price': 2.00, 'Stock': 5},
        'S3': {'Item': 'Cheetos', 'Price': 4.50, 'Stock': 5},
        'S4': {'Item': 'Doritos', 'Price': 4.50, 'Stock': 7},
        'S5': {'Item': 'Oman Chips', 'Price': 1.50, 'Stock': 4},
        'S6': {'Item': 'Snickers', 'Price': 3.00, 'Stock': 3},
        'S7': {'Item': 'Maltesers', 'Price': 3.25, 'Stock': 9},
        'S8': {'Item': 'Peanut Bar', 'Price': 1.00, 'Stock': 10},
    },
    '\n/// drinks ///': {
        'D1': {'Item': 'Water', 'Price': 1.00, 'Stock': 4},
        'D2': {'Item': 'Gatorade', 'Price': 4.50, 'Stock': 5},
        'D3': {'Item': 'Sprite', 'Price': 2.25, 'Stock': 8},
        'D4': {'Item': 'Mountain Dew', 'Price': 2.25, 'Stock': 10},
        'D5': {'Item': 'Apple Juice', 'Price': 3.00, 'Stock': 2},
        'D6': {'Item': 'Orange Juice', 'Price': 3.00, 'Stock': 3},
        'D7': {'Item': 'Chocolate Milk', 'Price': 2.50, 'Stock': 6},
        'D8': {'Item': 'Iced Coffee', 'Price': 5.00, 'Stock': 6},
    }
}

# Displaying vending machine menu
def display_menu(category, items):
    console = Console()
    subheading_color = "bright_yellow" if category == "\n/// snacks ///" else "bright_cyan"

    table = Table(title=f"[bold {subheading_color}]{category.upper()}[/]", title_justify="center", show_lines=True)
    table.add_column("Code", justify="center")
    table.add_column("Item", justify="center")
    table.add_column("Price", justify="center")
    table.add_column("Stock", justify="center")

    for code, item in items.items():
        table.add_row(code, item['Item'], f"AED{item['Price']:.2f}", str(item['Stock']))

    console.print(table, justify="center")

for category, items in menu.items():
    display_menu(category, items)

# User inserting cash
def cash_input():
    while True:
        try:
            balance = float(input("Please insert your cash: "))
            if balance > 0:
                return balance
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# User selecting a snack or drink 
def select_item(menu, balance):
    order_summary = []  # List to store all purchased items
    
    while True:
        print('\n[bold bright_magenta]// SELECT AN ITEM //[/bold bright_magenta]')
        order = input("Enter the code of the item you want to select: ").upper()
        
        # Check if the entered code is valid
        if order not in {code for items in menu.values() for code in items}:
            print("Error occurred. Please enter a valid code.")
            continue

        selected_item = None
        for category, items in menu.items():
            if order in items:
                selected_item = items[order]
                break
                
        if selected_item:
            # Check if the item is in stock
            if selected_item['Stock'] > 0:
                selected_item['Stock'] -= 1
                print(f"This item has {selected_item['Stock']} left in stock.")
                    
                # Check if the inserted money is enough
                price = selected_item['Price']
                if balance < price:
                    print("Insufficient money. Please input the correct amount.")
                    break
                else:
                    # Dispense the item
                    change = balance - price
                    time.sleep(2)
                    print(f"\nDispensing {selected_item['Item']}...")
                    order_summary.append(selected_item)  # Add purchased item to order summary

                    # Update user balance
                    balance -= price
                    remaining_balance = balance  # Save the remaining balance before updating
                    time.sleep(2)
                    print(f"[green]\nRemaining Balance: AED{remaining_balance:.2f}[/green]")

                    # Ask if the user wants to buy additional items
                    buy_additional = input("Do you want to buy additional items? (YES/NO): ").upper()
                    
                    if buy_additional == 'NO':
                        time.sleep(2)
                        print('\n[bold bright_blue]// ORDER SUMMARY //[/bold bright_blue]')
                        total_amount = 0  # Reset the total amount
                        for item in order_summary:
                            print(f"[white]{item['Item']} | AED{item['Price']:.2f}[/white]")
                            total_amount += item['Price']  # Add the price to the total
                        print(f"[bright_green]\nTotal Amount: AED{total_amount:.2f}[/bright_green]")
                        print(f"[green]Change: AED{change:.2f}.[/green]")
                        print("\nThank you for purchasing. Enjoy!")
                        break

            else:
                print("Sorry, the selected item is currently out of stock. Please choose another item.")

# Allow the user to select an item
initial_balance = cash_input()
select_item(menu, initial_balance)