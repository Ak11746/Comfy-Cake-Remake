from functions import *
from random import choices
from playsound3 import playsound
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
playsound(r".\media\music\PURBLE_BUTTON_STEREO.WMA", block=False)
for name in files:
    check_conection(name)
print()
colour_print("Checking Complete", False, "plain", colour= "green", bold = False)
playsound(r".\media\music\PURBLES_SHAKERBUTTON.WMA", block=False)
print()
difficulty= input(f"Select Difficulty level: \n{colour_print("", "code", "plain", colour="green", bold = True)}1. Easy{end_code()}\n{colour_print("", "code", "plain", colour="golden", bold = True)}2. Difficult{end_code()}\n{colour_print("", "code", "plain", colour="red", bold = True)}3. Asian{end_code()}\n: ")
playsound(r".\media\music\PURBLES_CAKEBUTTONS.WMA", block=False)
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

cakes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
cakes_discription = {
    0: [1, ["heart", "chocolate"]],
    1: [1, ["rectangle", "chocolate"]],
    2: [1, ["rectangle", "vanila"]],
    3: [2, ["circle", "chocolate"], ["icing", "vanila"]],
    4: [2, ["circle", "strawberry"], ["decor", "sprinkles"]],
    5: [2, ["circle", "vanila"], ["icing", "vanila"]],
    6: [3, ["rectangle", "chocolate"], ["circle", "strawberry"], ["icing", "vanila"]],
    7: [3, ["rectangle", "vanila"], ["heart", "vanila"], ["decor", "sprinkles"]],
    8: [3, ["rectangle", "strawberry"], ["rectangle", "chocolate"], ["icing", "strawberry"]],
    9: [4, ["circle", "vanila"], ["heart", "chocolate"], ["icing", "strawberry"], ["decor", "sprinkles"]],
    10: [4, ["rectangle", "strawberry"], ["heart", "chocolate"], ["icing", "vanila"], ["decor", "ganache"]],
    11: [4, ["heart", "vanila"], ["circle", "strawberry"], ["icing", "chocolate"], ["decor", "marzipan"]],
    12: [5, ["rectangle", "vanila"], ["circle", "chocolate"], ["heart", "strawberry"], ["icing", "vanila"], ["decor", "ganache"]],
    13: [5, ["rectangle", "strawberry"], ["circle", "vanila"], ["heart", "strawberry"], ["icing", "chocolate"], ["decor", "sprinkles"]],
    14: [5, ["rectangle", "chocolate"], ["circle", "strawberry"], ["heart", "vanila"], ["icing", "strawberry"], ["decor", "marzipan"]],
    15: [6, ["rectangle", "vanila"], ["icing", "chocolate"], ["circle", "chocolate"], ["icing", "strawberry"], ["circle", "strawberry"], ["icing", "vanila"], ["decor", "ganache"], ["decor", "marzipan"]],
    16: [6, ["circle", "chocolate"], ["icing", "vanila"], ["heart", "strawberry"], ["icing", "vanila"], ["rectangle", "vanila"], ["icing", "strawberry"], ["decor", "sprinkles"], ["decor", "ganache"]],
    17: [6, ["heart", "strawberry"], ["icing", "chocolate"], ["rectangle", "vanila"], ["icing", "chocolate"], ["heart", "chocolate"], ["icing", "chocolate"], ["decor", "marzipan"], ["decor", "sprinkles"]],
}
match difficulty.strip().lower():
    case "easy":
        weights = [10,10,10,20,20,20,10,10,10,1,1,1,1,1,1,1,1,1]
    case "difficult":
        weights = [1,1,1,1,1,1,5,5,5,20,20,20,10,10,10,5,5,5]
    case "asian":
        weights = [1,1,1,1,1,1,5,5,5,5,5,5,10,10,10,20,20,20]
list = []
for _ in range(cakes_n):
    list.append(choices(cakes, weights)[0])

def bake():
    clear()
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
        clear()
        print(colour_print("Current Active Tab: @"+tabs[n], True, "plain", colour = "White", bold= False).replace("@", end_code()+colour_print("", "code", "plain", colour = "White", bold = True)))
        print(colour_print("Available Options (Enter the resp. code):\n@"+options[tabs[n]][0], True, "plain", colour = "White", bold= False).replace("@", end_code()+colour_print("", "code", "plain", colour = "White", bold = True)))
        colour_print(": 'next' and 'previous'for next and previous menu respectively\n: 'undo' to undo\n: 'done' to finish and pack the cake\n", False, "plain", colour = "White", bold= True)
        match input("You response shall be: ").lower():
            case "next"|"n":
                playsound(r".\media\music\PURBLES_ROTATEBUTTON.WMA", block=False)
                n = n+1 if n<3 else n-3
            case "previous"|"p":
                playsound(r".\media\music\PURBLES_ROTATEBUTTON.WMA", block=False)
                n = n-1 if n >-4 else n+4
            case "1":
                playsound(r".\media\music\PURBLES_CAKEBUTTONS.WMA", block=False)
                cake.append(options[tabs[n]][1])
            case "2":
                playsound(r".\media\music\PURBLES_CAKEBUTTONS.WMA", block=False)
                cake.append(options[tabs[n]][2])
            case "3":
                playsound(r".\media\music\PURBLES_CAKEBUTTONS.WMA", block=False)
                cake.append(options[tabs[n]][3])
            case "undo"|"u":
                playsound(r".\media\music\PURBLE_BUTTON_STEREO.WMA", block=False)
                cake.pop()
            case "done"|"d":
                playsound(r".\media\music\PURBLES_SHAKERBUTTON.WMA", block=False)
                return cake
            case "lord hear our prayer":
                playsound(r".\media\music\PURBLES_SHAKERBUTTON.WMA", block=False)
                win = False
                return win
            
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

clear()

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
    playsound(r".\media\music\PURBLE_BUTTON_STEREO.WMA", block=False)
    package = bake()
    if str(type(package)) == "<class 'bool'>" and package:
        playsound(r".\media\music\WIN.WMA", block=False)
        with open("check_score.txt", 'a', encoding="utf-8") as file:
            file.write("backdoor\n")
        input(":")
        quit()
    order = sum(cakes_discription[list[n]][1:], [])
    clear()
    try:
        for i in package:
            order.remove(i)
    except Exception:
        playsound(r".\media\music\PURBLES_GENERALFAILURE.WMA", block=False)
        with open("check_score.txt", 'a', encoding="utf-8") as file:
            file.write("-\n")
        colour_print("One job bro, ONE JOB!!", False, "plain", colour = "red", bold = True)
    else:
        if not any(order):
            playsound(r".\media\music\WIN.WMA", block=False)
            with open("check_score.txt", 'a', encoding="utf-8") as file:    
                file.write("+\n")
            colour_print("Good Job", False, "plain", colour = "Green", bold = True)
        else:
            playsound(r".\media\music\PURBLES_GENERALFAILURE.WMA", block=False)
            with open("check_score.txt", 'a', encoding="utf-8") as file:
                file.write("-\n")
            colour_print("One job bro, ONE JOB!!", False, "plain", colour = "red", bold = True)
    input("Next: ")
    clear()

input(":")
quit()

            
