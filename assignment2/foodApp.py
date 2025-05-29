import random
import time

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = sum(item.price for item in items)
        self.status = "Preparing"

    def generate_bill(self):
        print(f"\nBill for Order #{self.order_id}")
        for item in self.items:
            print(f"{item.name} - ${item.price:.2f}")
        print(f"Total: ${self.total:.2f}\n")

class FoodOrderingSystem:
    def __init__(self):
        self.menu = [
            MenuItem(1, "Cheeseburger", 7.99),
            MenuItem(2, "Chicken wings", 6.99),
            MenuItem(3, "Fries", 2.99),
            MenuItem(4, "Soda", 1.99),
            MenuItem(5, "Ice Cream", 3.00)
        ]
        self.orders = []

    def display_menu(self):
        print("\nMenu:")
        for item in self.menu:
            print(f"{item.item_id}. {item.name} - ${item.price:.2f}")

    def place_order(self):
        self.display_menu()
        try:
            item_ids = input("Enter item numbers separated by commas (e.g., 1,3,4): ")
            item_ids = [int(i.strip()) for i in item_ids.split(",")]
            selected_items = []

            for item_id in item_ids:
                item = next((i for i in self.menu if i.item_id == item_id), None)
                if item:
                    selected_items.append(item)
                else:
                    print(f"Item {item_id} not found, skipping.")

            if not selected_items:
                print("No valid items selected. Order canceled.\n")
                return

            order_id = len(self.orders) + 1
            order = Order(order_id, selected_items)
            self.orders.append(order)
            self.save_order_to_file(order)
            print(f"\nOrder #{order_id} placed successfully!\n")
            order.generate_bill()

        except ValueError:
            print("Invalid input. Please enter item numbers only.\n")

    def track_order(self):
        try:
            order_id = int(input("Enter your Order ID to track: "))
            order = next((o for o in self.orders if o.order_id == order_id), None)
            if order:
                print(f"\nOrder #{order.order_id} Status: {order.status}")
                if order.status != "Delivered":
                    order.status = random.choice(["Preparing", "Out for delivery", "Delivered"])
                    print(f"Updated Status: {order.status}\n")
                else:
                    print("Your order has already been delivered.\n")
            else:
                print("Order not found.\n")
        except ValueError:
            print("Please enter a valid order ID.\n")

    def save_order_to_file(self, order):
        try:
            with open("order_history.txt", "a") as f:
                f.write(f"Order #{order.order_id} - Items: {[item.name for item in order.items]}, Total: ${order.total:.2f}\n")
        except Exception as e:
            print(f"Error saving order: {e}")

def main():
    system = FoodOrderingSystem()

    while True:
        action = input("Enter your action (menu, order, track, exit): ").lower()

        if action == "menu":
            system.display_menu()
        elif action == "order":
            system.place_order()
        elif action == "track":
            system.track_order()
        elif action == "exit":
            print("Thank you for using our food ordering service. Goodbye!")
            break
        else:
            print("Invalid action. Please choose from (menu, order, track, exit).\n")

main()
