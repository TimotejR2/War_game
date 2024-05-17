import json
from map.map import Map, Map_field
from objects.vehicle import Vehicle
from objects.employee import Employee
import utils.convertor as convertor

# Read files
vehicles = json.load(open('data/shop/vehicle.json'))
employees = json.load(open('data/shop/employee.json'))
map_data = open('data/map.txt').readlines()

class Player:
    def __init__(self, name, money = 100):
        self.name = name
        self.money = money
        self.vehicles = []
        self.employees = []
    
    def buy_vehicle(self, selected_vehicle):
        """
        Buy a vehicle if the player has enough money.
        
        Parameters:
            vehicle: dict with data about the vehicle

        """
        selected_vehicle['price'] = selected_vehicle['price']
        if self.money >= selected_vehicle['price']:
            # Create new vehicle
            new_vehicle = Vehicle(selected_vehicle)
            print(f"You bought {selected_vehicle['name']}.")
            self.vehicles.append(new_vehicle)
            self.money -= selected_vehicle['price']
    
    def hire_employee(self, selected_employee):
        
        if self.money >= selected_employee['price']:
            new_employee = Employee(selected_employee)
            print(f"You hired {selected_employee['name']}.")
            self.employees.append(new_employee)
            self.money -= selected_employee['price']

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
                    

def main():
    map = Map(map_data)
    map.generate_map()

    player1 = Player('player1', money=1000)
    player1.buy_vehicle(vehicles[2])

    player2 = Player('player2', money=1000)
    player2.buy_vehicle(vehicles[0])

    player1.vehicles[0].move(convertor.location_to_field([3,3], map))

    player2.vehicles[0].move(convertor.location_to_field([0,0], map))

    player2.vehicles[0].attack(convertor.location_to_field([3,0], map))



main()



