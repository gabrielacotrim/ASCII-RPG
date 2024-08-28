import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True

HP = 5
HPMAX = HP
ATK = 5
bandages = 3     # small healing
medicine = 0    # big healing
scrap = 0       # currency
bones = 0       # currency
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

e_list = ["Infected", "Variant", "Scavenger", "Cult Member", "Wolves Scout", "Wild Wolf", "Infected Wolf"]

mobs = {
    "Infected": {
        "hp": 10,
        "at": 5,
        "scr": 8,
        "bn": 0,
        "bndg": 0,
        "med": 0 
    },
    #"Variant": {
     #   "hp": 30,
      #  "at": 12,
       # "scr": 25,
        #"bn": 0,
        #"bndg": 0,
        #"med": 0
    #},
    "Scavenger": {
        "hp": 12,
        "at": 4,
        "scr": 15,
        "bn": 8,
        "bndg": 2,
        "med": 0
    },
    "Wolves Scout": {
        "hp": 22,
        "at": 7,
        "scr": 17,
        "bn" : 10,
        "bndg": 5,
        "med": 2
    },
    "Wild Wolf": {
        "hp": 15,
        "at": 5,
        "scr": 0,
        "bn" : 8,
        "bndg": 0,
        "med": 0
    },
    "Infected Wolf": {
        "hp": 18,
        "at": 9,
        "scr": 0,
        "bn" : 16,
        "bndg": 0,
        "med": 0
    }
}

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
        str(bandages),
        str(medicine),
        str(scrap),
        str(bones),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")
    
    for item in list:
        f.write(item + "\n")
    f.close()

def battle():
    global fight, play, run, HP, bandages, medicine, scrap, bones

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    s = mobs[enemy]["scr"]
    b = mobs[enemy]["bn"]
    bd = mobs[enemy]["bndg"]
    md = mobs[enemy]["med"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("BANDAGES: " + str(bandages))
        print("MEDICINE: " + str(medicine))
        draw()
        print("1 - ATTACK")
        if bandages > 0:
            print("2 - USE BANDAGE (25HP)")
        if medicine:   
            print("3- USE MEDICINE (50HP)")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
        elif choice == "2":
            pass
        elif choice == "3":
            pass

        if HP <= 0:
            print("The" + enemy + " killed " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print(" YOU HAVE FALLEN ")
            print(" GAME OVER ")
            print("             .")
            print("            -|-")
            print("             |")
            print("         .-'~~~`-.")
            print("       .'         `.")
            print("       |  R  I  P  |")
            print("       |           |")
            print("       |           |")
            print("     [[|           |]]")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            draw()
            input("> ")

            if hp <= 0:
                print(name + " slaughtered the " + enemy + "!")
                draw()
                fight = False
                scrap += s
                print("You've found:")
                print(str(s))
                bones += b
                bandages += bd
                medicine += md

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
                if len(load_list) == 10:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    bandages = int(load_list[3][:-1])
                    medicine = int(load_list[4][:-1])
                    scrap = int(load_list[5][:-1])
                    bones = int(load_list[6][:-1])
                    x = int(load_list[7][:-1])
                    y = int(load_list[8][:-1])
                    key = bool(load_list[9][:-1])
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

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("BANDAGE: " + str(bandages))
            print("MEDICINE: " + str(medicine))
            print("SCRAP: " + str(scrap))
            print("BONES: " + str(bones))
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
                    standing = False
                else:
                    menu = False
                    play = True
                    print("You have reach the border and can not go further...")
                    input("> ")
            elif dest == "2":           # MOVE RIGHT
                if x < x_len:
                    x += 1
                    standing = False
                else:
                    menu = False
                    play = True
                    print("You have reach the border and can not go further...")
                    input("> ")
            elif dest ==  "3":          # MOVE DOWN
                if y < y_len:
                    y += 1
                    standing = False
                else:
                    menu = False
                    play = True
                    print("You have reach the border and can not go further...")
                    input("> ")
            elif dest == "4":           # MOVE LEFT
                if x > 0:
                    x -= 1
                    standing = False
                else:
                    menu = False
                    play = True
                    print("You have reach the border and can not go further...")
                    input("> ")