class Employee:
    def __init__(self, selected_employee):
        self.name = selected_employee['name']
        self.role = selected_employee['role']
        self.equipment = selected_employee['equipment']
        self.hp = 100