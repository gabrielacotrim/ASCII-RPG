import os

run = True
menu = True
play = False
rules = False
key = False

HP = 50
HPMAX = HP
ATK = 5
bandage = 3     # small healing
medicine = 0    # big healing
scrap = 0       # currency
x = 0
y = 0

        #   x = 0       x = 1       x = 2       x = 3       x = 4         x = 5           x = 6 
map = [["fields",   "fields",      "fields",   "fields",        "woods",     "mountain",        "mines"],  # y = 0
       [ "woods",    "woods",       "woods",    "woods",        "woods",   "ashe field",     "mountain"],  # y = 1 
       [ "woods",    "swamp",      "bridge",   "fields",   "ashe field",        "woods",   "ashe field"],  # y = 2
       ["fields",     "shop",  "settlement",   "bunker",       "fields",   "ashe field",     "mountain"],  # y = 3
       ["fields",    "swamp",       "swamp",   "fields",   "ashe field",     "mountain",     "mountain"]]  # y = 4

y_len = len(map)-1
x_len = len(map[0])-1


biom = {
    "fields": {
        "t": "FIELDS",      # NAME
        "e": True},         # SPAWN ENEMYES
    "woods" : {
        "t": "WOODS",
        "e": True},
    "mountain": {
        "t": "MOUNTAINS",
        "e": True},
    "swamp": {
        "t": "SWAMP",
        "e": True},
    "ashe field": {
        "t": "ASHE FIELD",
        "e": True},
    "mines": {
        "t": "MINES",
        "e": True},
     "bridge": {
        "t": "BRIDGE",
        "e": True},
    "settlement": {
        "t": "settlement",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "bunker": {
        "t": "BUNKER", 
        "e": False}    } 

current_tile = map[y][x]
print(current_tile)
name_of_tile = biom[current_tile]["t"]
print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
print(enemy_tile)

def clear():
    os.system("cls")


def draw():
    print("->->->->->->->->->->->->->->->->->->->->->")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(bandage),
        str(medicine),
        str(scrap),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")
    
    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()
        
        if rules:
            print("Welcome! This are the rules: ")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")
        
        if choice == "1":
            clear()
            draw()
            name = input("# What is your name, traveler? ")
            draw()
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    bandage = int(load_list[3][:-1])
                    medicine = int(load_list[4][:-1])
                    scrap = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    draw()
                    print("Welcome back, " + name + "!")
                    draw()
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupted save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()
            
    while play:
        save() # autosave
        clear()
        draw()
        print("NAME: " + name)
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("BANDAGE: " + str(bandage))
        print("MEDICINE: " + str(medicine))
        print("SCRAP: " + str(scrap))
        print("COORD:", x, y)
        draw()
        print("LOCATION: " + biom[map[y][x]]["t"])       # current location
        draw()
        print("0 - SAVE AND QUIT")
        if y > 0:
            print("1 - NORTH")          # UP
        if x < x_len:
            print("2 - EAST")           # RIGHT
        if y < y_len:
            print("3 - SOUTH")          # DOWN
        if x > 0:
            print("4 - WEST")           # LEFT
        draw()
        
        dest = input("# ")
        
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":           # MOVE UP
            if y > 0:
                y -= 1
            else:
                menu = False
                play = True
                print("You have reach the border and can not go further...")
                input("> ")
        elif dest == "2":           # MOVE RIGHT
            if x < x_len:
                x += 1
            else:
                menu = False
                play = True
                print("You have reach the border and can not go further...")
                input("> ")
        elif dest ==  "3":          # MOVE DOWN
            if y < y_len:
                y += 1
            else:
                menu = False
                play = True
                print("You have reach the border and can not go further...")
                input("> ")
        elif dest == "4":           # MOVE LEFT
            if x > 0:
                x -= 1
            else:
                menu = False
                play = True
                print("You have reach the border and can not go further...")
                input("> ")