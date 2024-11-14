

inventory = {} 

def display_inventory():
    """Displays the current inventory."""
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    print()  # Blank line for readability

def add_item():
    """Adds a new item or updates the quantity of an existing item."""
    item = input("Enter the item name to add: ").strip()
    try:
        quantity = int(input(f"Enter the quantity of '{item}': "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
        if item in inventory:
            inventory[item] += quantity
            print(f"Updated '{item}' quantity to {inventory[item]}.")
        else:
            inventory[item] = quantity
            print(f"Added '{item}' with quantity {quantity}.")
    except ValueError:
        print("Invalid input. Quantity must be a number.")

def remove_item():
    """Removes an item or decreases its quantity."""
    item = input("Enter the item name to remove: ").strip()
    if item not in inventory:
        print(f"'{item}' does not exist in the inventory.")
    else:
        try:
            quantity = int(input(f"Enter the quantity to remove from '{item}': "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                return
            if quantity >= inventory[item]:
                del inventory[item]
                print(f"Removed '{item}' from inventory.")
            else:
                inventory[item] -= quantity
                print(f"Reduced '{item}' quantity to {inventory[item]}.")
        except ValueError:
            print("Invalid input. Quantity must be a number.")

def update_item():
    """Updates the quantity of an existing item."""
    item = input("Enter the item name to update: ").strip()
    if item not in inventory:
        print(f"'{item}' does not exist in the inventory.")
    else:
        try:
            quantity = int(input(f"Enter the new quantity for '{item}': "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[item] = quantity
                print(f"Updated '{item}' quantity to {quantity}.")
        except ValueError:
            print("Invalid input. Quantity must be a number.")

def main():
    """Main function to run the inventory management system."""
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item Quantity")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()