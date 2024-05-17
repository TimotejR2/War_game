class Vehicle:
    def __init__(self, parameters):
        self.name = parameters['name']
        self.protection = parameters['protection']
        self.speed = parameters['speed']
        self.capacity = parameters['capacity']
        self.hp = parameters['hp']
        self.role = parameters['role']
        self.category = parameters['category']
        self.price = parameters['price']
        self.damage = parameters['damage']
        self.location = None
    
    def move(self, field):
        field.add_vehicle(self)
        print(f"{self.name} moved to {field.location}")
        self.location = field

    def attack(self, field):
        
        if field.vehicles:
            for enemy_vehicle in field.vehicles:
                print(f"{self.name} attacked! {enemy_vehicle.name}")
                enemy_vehicle.get_damage(self.damage)
        else:
            print("Attack failed. Field is empty")
    
    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} is destroyed")
            self.location.vehicles.remove(self)
        print(f"{self.name} took {damage} damage and current HP is {self.hp}")
        