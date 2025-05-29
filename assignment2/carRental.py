import datetime

class Car:
    def __init__(self, car_id, model, rate_per_day):
        self.car_id = car_id
        self.model = model
        self.rate_per_day = rate_per_day
        self.available = True

class CarRentalSystem:
    def __init__(self):
        self.cars = [
            Car(1, "Toyota Camry", 40),
            Car(2, "Honda Pilot", 55),
            Car(3, "Tesla Model S", 60)
        ]
        self.rental_history = []

    def display_available_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            if car.available:
                print(f"{car.car_id}. {car.model} - ${car.rate_per_day}/day")

    def rent_car(self):
        self.display_available_cars()
        try:
            car_id = int(input("Enter the car ID to rent: "))
            days = int(input("Enter number of days to rent: "))
            car = next((c for c in self.cars if c.car_id == car_id and c.available), None)
            if car:
                cost = car.rate_per_day * days
                confirm = input(f"Total cost is ${cost:.2f}. Confirm rental? (yes/no): ").lower()
                if confirm == "yes":
                    car.available = False
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    self.rental_history.append(
                        f"Rented {car.model} for {days} days on {date} - Cost: ${cost:.2f}"
                    )
                    print(f"You have successfully rented {car.model}.\n")
                else:
                    print("Rental cancelled.\n")
            else:
                print("Invalid selection or car not available.\n")
        except ValueError:
            print("Please enter valid input.\n")

    def return_car(self):
        try:
            car_id = int(input("Enter the car ID to return: "))
            car = next((c for c in self.cars if c.car_id == car_id and not c.available), None)
            if car:
                car.available = True
                print(f"{car.model} returned successfully.\n")
            else:
                print("Invalid selection or car not currently rented.\n")
        except ValueError:
            print("Please enter a valid car ID.\n")

    def view_rental_history(self):
        print("\nRental History:")
        if not self.rental_history:
            print("No rentals yet.")
        else:
            for record in self.rental_history:
                print(record)


def main():
    system = CarRentalSystem()

    while True:
        action = input("Enter your action (View Cars, Rent Car, Return Car, Rent History, Exit): ").lower()

        if action == "view cars":
            system.display_available_cars()
        elif action == "rent car":
            system.rent_car()
        elif action == "return car":
            system.return_car()
        elif action == "rent history":
            system.view_rental_history()
        elif action == "exit":
            print("Thank you for using the Car Rental System.")
            break
        else:
            print("Invalid action. Please choose from (view, rent, return, history, exit).\n")



main()
