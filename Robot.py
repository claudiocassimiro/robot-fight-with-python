from Part import Part
from robot_assets import robot_art, colors

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5, robot_energy=self.energy),
            Part("Weapon", attack_level=15, defense_level=20, energy_consumption=10, robot_energy=self.energy),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=10, robot_energy=self.energy),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=10, robot_energy=self.energy),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consumption=15, robot_energy=self.energy),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15, robot_energy=self.energy),
        ]


    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].reduce_defense(self.parts[part_to_use].attack_level) 
        self.energy -= self.parts[part_to_use].energy_consumption
            

    def print_status(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"])
    

    def greet(self):
        print("Hello, my name is", self.name)
    

    def print_energy(self):
        print("We have", self.energy, " percent energy left")


    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status
      

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def check_if_part_is_available(self, part):
        if self.parts[part].is_available():
            return True
    
        return False

    def is_on(self):
        return self.energy >= 0