import random

class Car:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def __repr__(self):
        return "{} {} with {} HP".format(self.brand, self.model, self.power)

class Upgrades:
    def __init__(self, name, power_upgrade, cost):
        self.name = name
        self.power_upgrade = power_upgrade
        self.cost = cost

    @staticmethod
    def upgrade_car(car, upgrade_name, upgrades_list):
        selected_upgrade = next((upgrade for upgrade in upgrades_list if upgrade.name == upgrade_name), None)
        if selected_upgrade:
            car.power += selected_upgrade.power_upgrade
            print(f"Congratulations! {selected_upgrade.name} has been installed. Your car's power is now {car.power} HP.")
        else:
            print("Upgrade not found.")

    @staticmethod
    def visit_shop(car, upgrades_list):
        part_list = [upgrade.name for upgrade in upgrades_list]
        print(f"Hi! Welcome to Furious but not fast. Nice {car}. Our stock contains: {', '.join(part_list)}")

        choice = input("Do you want to upgrade your car? (yes/no): ").lower()
        if choice == "yes":
            upgrade_name = input("Enter upgrade part name: ")
            Upgrades.upgrade_car(car, upgrade_name, upgrades_list)

class Race:
    def __init__(self, car1, car2):
        self.car1 = car1
        self.car2 = car2
        
    def simulate_race(self):
        if self.car1.power > self.car2.power:
            print(f"Congratulations! You won the race against {self.car2.brand} {self.car2.model}!")
            return True
        else:
            print(f"Unfortunately, you lost the race against {self.car2.brand} {self.car2.model}.")
            return False

def main():
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    power = int(input("Enter car power (HP): "))

    player_car = Car(brand, model, power)
    opponent_car = Car("Jimmy's", "Mercedes-Benz", random.randint(150, 250))

    # Define a list of available upgrades
    upgrades_list = [
        Upgrades("Turbocharger", 50, 1000),
        Upgrades("Intercooler", 30, 800),
        Upgrades("Exhaust", 20, 600),
        Upgrades("Injectors", 40, 1200)
    ]

    Upgrades.visit_shop(player_car, upgrades_list)

    choice2 = input("Do you want to race your first opponent? (yes/no): ").lower()
    if choice2 == "yes":
        race = Race(player_car, opponent_car)
        result = race.simulate_race()

        if result:
            print("You earned $1000 for winning the race!")
            upgrade_budget = 1000
            while True:
                print("You can spend your winnings on upgrades:")
                for upgrade in upgrades_list:
                    print(f"{upgrade.name}: ${upgrade.cost}")
                choice = input("Enter the name of the upgrade you want to purchase (or 'quit' to exit): ").lower()
                if choice == "quit":
                    break
                selected_upgrade = next((upgrade for upgrade in upgrades_list if upgrade.name.lower() == choice), None)
                if selected_upgrade:
                    if upgrade_budget >= selected_upgrade.cost:
                        player_car.power += selected_upgrade.power_upgrade
                        print(f"Congratulations! You upgraded your car with {selected_upgrade.name}. Your car's power is now {player_car.power} HP.")
                        upgrade_budget -= selected_upgrade.cost
                    else:
                        print("You don't have enough money to purchase this upgrade.")
                else:
                    print("Invalid upgrade choice.")
        else:
            print("Better luck next time!")

if __name__ == "__main__":
    main()