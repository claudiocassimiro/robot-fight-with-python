from Robot import Robot 
from robot_assets import colors

def build_robot():
    robot_name = input("Robot name: ").capitalize()
    color_code = choose_color()
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot

def choose_color():
    available_colors = colors
    print("Available colors:")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])
    chosen_color = input("Choose a color: ")
    color_code = available_colors[chosen_color.capitalize()]
    return color_code

def play():
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1:")
    robot_one = build_robot()
    print("Datas for player 2:")
    robot_two = build_robot()
    
    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0
    
    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()
        print("What part should I use to attack?:")

        part_is_available = True
        while part_is_available: # Esse while verifica se a part escolhida para atacar está disponivel antes de fazer o ataque
          part_to_use = int(input("Choose a number part: "))
          is_available = current_robot.check_if_part_is_available(part_to_use)
          if is_available == False:
              print("Please select an available part")
          
          part_is_available = not is_available
        
        enemy_robot.print_status()
        print("Which part of the enemy should we attack?")
        part_to_attack = int(input("Choose a enemy number part to attack: "))
        
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
          
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False

        if enemy_robot.is_on():
            print("Parabéns, {} venceu!".format(enemy_robot.name))
        else:
            print("Parabéns, {} venceu!".format(current_robot.name))
play()


