import getpass

users_db = {
    "admin": {"password": "adminpass", "role": "Admin"},
    "user": {"password": "userpass", "role": "User"}
}

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

class Inventory:
    def __init__(self):
        self.products = {}  
        self.low_stock_threshold = 5

    def add_product(self, product_id, name, category, price, stock_quantity):
        if product_id in self.products:
            print(f"Product ID '{product_id}' already exists.")
        else:
            product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = product
            print(f"Product '{name}' added successfully.")

    def edit_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if not product:
            print(f"Product ID '{product_id}' not found.")
            return
        if name:
            product.name = name
        if category:
            product.category = category
        if price:
            product.price = price
        if stock_quantity is not None:
            product.stock_quantity = stock_quantity
        print(f"Product ID '{product_id}' updated successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID '{product_id}' deleted successfully.")
        else:
            print(f"Product ID '{product_id}' not found.")

    def view_all_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        print("\nInventory:")
        for product in self.products.values():
            self.print_product_details(product)

    def search_product(self, keyword):
        found = False
        for product in self.products.values():
            if keyword.lower() in product.name.lower() or keyword.lower() in product.category.lower():
                self.print_product_details(product)
                found = True
        if not found:
            print("No products found with the given keyword.")

    def filter_by_stock_level(self, low_stock=False):
        if low_stock:
            print("\nLow Stock Products (Below Threshold):")
            for product in self.products.values():
                if product.stock_quantity < self.low_stock_threshold:
                    self.print_product_details(product)
        else:
            self.view_all_products()

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if not product:
            print(f"Product ID '{product_id}' not found.")
        else:
            product.update_stock(quantity)
            print(f"Updated stock for Product ID '{product_id}'. New stock: {product.stock_quantity}")
            if product.stock_quantity < self.low_stock_threshold:
                print(f"Warning: Stock for '{product.name}' is below threshold! Consider restocking.")

    @staticmethod
    def print_product_details(product):
        print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
              f"Price: ${product.price}, Stock: {product.stock_quantity}")

# Authentication function
def login():
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()
    user_data = users_db.get(username)

    if user_data and user_data["password"] == password:
        print(f"Welcome, {username} ({user_data['role']})!")
        return user_data["role"]
    else:
        print("Invalid username or password.")
        return None

# Main program function
def main():
    inventory = Inventory()
    role = None
    while not role:
        print("\n=== Inventory Management System Login ===")
        role = login()

    while True:
        print("\n=== Inventory Management System ===")
        print("1. View All Products")
        print("2. Search Products by Name or Category")
        print("3. View Low Stock Products")
        if role == "Admin":
            print("4. Add New Product")
            print("5. Edit Product")
            print("6. Delete Product")
            print("7. Adjust Stock")
        print("8. Logout")
        
        choice = input("Choose an option: ").strip()

        if choice == '1':
            inventory.view_all_products()
        elif choice == '2':
            keyword = input("Enter product name or category to search: ").strip()
            inventory.search_product(keyword)
        elif choice == '3':
            inventory.filter_by_stock_level(low_stock=True)
        elif choice == '4' and role == "Admin":
            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            category = input("Enter Product Category: ").strip()
            try:
                price = float(input("Enter Product Price: ").strip())
                stock_quantity = int(input("Enter Stock Quantity: ").strip())
                inventory.add_product(product_id, name, category, price, stock_quantity)
            except ValueError:
                print("Invalid input for price or stock quantity.")
        elif choice == '5' and role == "Admin":
            product_id = input("Enter Product ID to edit: ").strip()
            name = input("Enter new Product Name (leave blank to skip): ").strip()
            category = input("Enter new Product Category (leave blank to skip): ").strip()
            try:
                price = input("Enter new Product Price (leave blank to skip): ").strip()
                stock_quantity = input("Enter new Stock Quantity (leave blank to skip): ").strip()
                inventory.edit_product(
                    product_id,
                    name=name if name else None,
                    category=category if category else None,
                    price=float(price) if price else None,
                    stock_quantity=int(stock_quantity) if stock_quantity else None
                )
            except ValueError:
                print("Invalid input for price or stock quantity.")
        elif choice == '6' and role == "Admin":
            product_id = input("Enter Product ID to delete: ").strip()
            inventory.delete_product(product_id)
        elif choice == '7' and role == "Admin":
            product_id = input("Enter Product ID to adjust stock: ").strip()
            try:
                quantity = int(input("Enter quantity to adjust (negative to reduce): ").strip())
                inventory.adjust_stock(product_id, quantity)
            except ValueError:
                print("Invalid input. Quantity must be an integer.")
        elif choice == '8':
            print("Logging out...")
            role = None
            main()  # restart login process
        else:
            print("Invalid choice or permission denied.")

if __name__ == "__main__":
    main()