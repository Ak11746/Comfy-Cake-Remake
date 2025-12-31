from functions import *
from random import choices
rows = get_dimentions("row")
columns = get_dimentions("column")
lr = columns if columns < rows else rows

files = ["check_clock.txt", "check_score.txt", "check_progress.txt", "check_order.txt"] #"check_img.txt", 

for name in files:
    clear(name)

colour_print("\n"+"*"*columns, False, "256", layer = "fg", code = "153")
colour_print(align("COMFY CAKES"), False, "256", layer = "fg", code = "153")
colour_print("*"*columns+ '\n', False, "256", layer = "fg", code = "153")
print()
input("Press Enter to start the necessary checking: ")
for name in files:
    check_conection(name)
print()
colour_print("Checking Complete", False, "plain", colour= "green", bold = False)

print()
difficulty= input(f"Select Difficulty level: \n{colour_print("", "code", "plain", colour="green", bold = True)}1. Easy{end_code()}\n{colour_print("", "code", "plain", colour="golden", bold = True)}2. Difficult{end_code()}\n{colour_print("", "code", "plain", colour="red", bold = True)}3. Asian{end_code()}\n: ")
match difficulty.strip().lower():
    case "easy"|"1":
        difficulty = "easy"
    case "difficult"|2:
        difficulty = "difficult"
    case "asian":
        difficulty = "asian"

with open("check_clock.txt", 'a', encoding="utf-8") as file:
    match difficulty.strip().lower():
        case "easy":
            file.write("easy\n")
        case "difficult":
            file.write("diff\n")
        case "asian":
            file.write("asian\n")

with open("check_score.txt", 'a', encoding="utf-8") as file:
    match difficulty.strip().lower():
        case "easy":
            file.write("5\n")
            cakes_n = 5
        case "difficult":
            file.write("6\n")
            cakes_n = 6
        case "asian":
            file.write("7\n")
            cakes_n = 7

starter(files)

cakes = [0,1,2,3,4,5]
cakes_discription = {
    0: [1, ["heart", "chocolate"]],
    1: [2, ["circle", "chocolate"], ["icing", "vanila"]],
    2: [3, ["rectangle", "chocolate"], ["circle", "strawberry"], ["icing", "vanila"]],
    3: [4, ["circle", "vanila"], ["heart", "chocolate"], ["icing", "vanila"], ["decor", "sprinkles"]],
    4: [5, ["rectangle", "vanila"], ["circle", "chocolate"], ["heart", "strawberry"], ["icing", "vanila"], ["decor", "ganache"]],
    5: [6, ["rectangle", "vanila"], ["icing", "chocolate"], ["circle", "chocolate"], ["icing", "strawberry"], ["circle", "strawberry"], ["icing", "vanila"], ["decor", "ganache"], ["decor", "marzipan"]],
}
match difficulty.strip().lower():
    case "easy":
        weights = [0.4, 0.5, 0.05, 0.05, 0, 0]
    case "difficult":
        weights = [0.05, 0.05, 0.4, 0.4, 0.05, 0.05]
    case "asian":
        weights = [0.01, 0.01, 0.04, 0.04, 0.45, 0.45]
list = []
for _ in range(cakes_n):
    list.append(choices(cakes, weights)[0])

def bake():
    print("\033[2J\033[1;1H")
    cake = []
    tabs = ["layer", "flavour", "icing", "decor"]
    options ={
        "layer": ["1. Circle\n2. Rectangle\n3. Heart", "circle", "rectangle", "heart"], 
        "flavour": ["1. Chocolate\n2. Vanila\n3. Strawberry", "chocolate", "vanila", "strawberry"],
        "icing": ["1. Chocolate\n2. Vanila\n3. Strawberry", "chocolate", "vanila", "strawberry"],
        "decor": ["1. Sprinklers\n2. Marzipan\n3. Ganache", "sprinklers", "marzipan", "ganache" ]
    }
    n = size = 0
    while True:
        print("\033[2J\033[1;1H")
        print(colour_print("Current Active Tab: @"+tabs[n], True, "plain", colour = "White", bold= False).replace("@", end_code()+colour_print("", "code", "plain", colour = "White", bold = True)))
        print(colour_print("Available Options (Enter the resp. code):\n@"+options[tabs[n]][0], True, "plain", colour = "White", bold= False).replace("@", end_code()+colour_print("", "code", "plain", colour = "White", bold = True)))
        colour_print(": 'next' and 'previous'for next and previous menu respectively\n: 'undo' to undo\n: 'done' to finish and pack the cake\n", False, "plain", colour = "White", bold= True)
        match input("You response shall be: "):
            case "next"|"n":
                n = n+1 if n<3 else n-3
            case "previous"|"p":
                n = n-1 if n >-4 else n+4
            case "1":
                cake.append(options[tabs[n]][1])
            case "2":
                cake.append(options[tabs[n]][2])
            case "3":
                cake.append(options[tabs[n]][3])
            case "undo"|"u":
                cake.pop()
                undo = True
            case "done"|"d":
                return cake
        if tabs[n] in ["icing", "decor"] and len(cake)>size:
            cake.insert(size, tabs[n])
        print(cake)

        b_message = colour_print(f"Contents:", True, "plain", colour = "blue", bold = True)
        b_message += "`"
        i = None
        for i in cake:
            if i in ["circle", "rectangle", "heart", "icing", "decor"]:
                b_message += colour_print(f"layer: @{i}", True, "plain", colour = "cyan", bold = False).replace("@", end_code()+colour_print("", "code", "plain", colour = "cyan", bold = True))
                b_message += "`"
            elif len(i) > 1:
                b_message += colour_print(f"flavour/type: @{i}", True, "plain", colour = "cyan", bold = False).replace("@", end_code()+colour_print("", "code", "plain", colour = "cyan", bold = True))
                b_message += "`"
        b_message +="\n"
        with open("check_progress.txt", 'a', encoding="utf-8") as file:
            file.write(b_message)
            file.flush()
        print(b_message)
            
        size = len(cake)

print("\033[2J\033[1;1H")

for n in range(cakes_n):
    message = colour_print(f"Order {n+1}:", True, "plain", colour = "blue", bold = True)
    message +="`"
    for i in cakes_discription[list[n]]:
        if not str(type(i)) == "<class 'int'>":
            message += colour_print(f"layer: @{i[0]}! and flavour/type: @{i[1]}!", True, "plain", colour = "cyan", bold = False).replace("@", end_code()+colour_print("", "code", "plain", colour = "cyan", bold = True)).replace("!", end_code()+colour_print("", "code", "plain", colour = "cyan", bold = False))
            message +="`"           
        else:
            message += colour_print(f"No of layers: @{i}", True, "plain", colour = "cyan", bold = False).replace("@", end_code()+colour_print("", "code", "plain", colour = "cyan", bold = True))
            message +="`"   
    message +="\n"
    with open("check_order.txt", 'a', encoding="utf-8") as file:
        q =10000
        while q > 0:
            q-=1
        file.write(message)
        file.flush()

    print(message.replace("`", "\n"))         
    input("Take a gooood looong loook and press enter: ")

    package = bake()
    order = sum(cakes_discription[list[n]][1:], [])
    print("\033[2J\033[1;1H")
    try:
        for i in package:
            order.remove(i)
    except Exception:
        with open("check_score.txt", 'a', encoding="utf-8") as file:
            file.write("-\n")
        colour_print("One job bro, ONE JOB!!", False, "plain", colour = "red", bold = True)
    else:
        if not any(order):
            with open("check_score.txt", 'a', encoding="utf-8") as file:    
                file.write("+\n")
            colour_print("Good Job", False, "plain", colour = "Green", bold = True)
        else:
            with open("check_score.txt", 'a', encoding="utf-8") as file:
                file.write("-\n")
            colour_print("One job bro, ONE JOB!!", False, "plain", colour = "red", bold = True)
    input("Next: ")
    print("\033[2J\033[1;1H")

input(":")


            