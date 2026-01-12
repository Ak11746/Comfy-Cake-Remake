from time import sleep
from functions import *
input(":")
check_conection("check_clock.txt", False)

with open("check_clock.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            if line in ["easy\n", "diff\n", "asian\n"]:
                match line:
                    case "easy\n":
                        min = 5
                    case "diff\n":
                        min = 2
                    case "asian\n":
                        min = 1
                colour_print("Difficulty level recieved", False, "plain", colour="green", bold = False)
                break
        else:
            continue
        break

start("check_clock.txt")
clear()
sec = 00
over = False
faces = {
    0: [" ▄▄▄▄ ", " █  █ ", " █  █ ", " █▄▄█ "],
    1: [" ▄    "," █    "," █    "," █    "],
    2: [" ▄▄▄▄ ", "    █ ", " █▀▀▀ ", " █▄▄▄ "],
    3: [" ▄▄▄▄ ", "    █ ", " ▀▀▀█ ", " ▄▄▄█ "],
    4: [" ▄  ▄ ", " █  █ ", " ▀▀▀█ ", "    █ "],
    5: [" ▄▄▄▄ ", " █    ", " ▀▀▀█ ", " ▄▄▄█ "],
    6: [" ▄▄▄▄ ", " █    ", " █▀▀█ ", " █▄▄█ "],
    7: [" ▄▄▄▄ ", "    █ ", "    █ ", "    █ "],
    8: [" ▄▄▄▄ ", " █  █ ", " █▀▀█ ", " █▄▄█ "],
    9: [" ▄▄▄▄ ", " █  █ ", " ▀▀▀█ ", " ▄▄▄█ "],
    ":": ["   ", " ▀ ", " ▄ ", "   "]
    }

def clock_face(m,s):
    if min < 10:
        clock = [m, ":", s//10, s%10]
    elif min <= 60:
        clock = [m//10, m%10, ":", s//10, s%10]
    str = ""
    for i in range(4):
        for j in clock:
            str += faces[j][i]
        str+= "\n"
    return str


while not over:
    if sec == 00:
        sec = 59
        min -=1
    else:
        sec -= 1
    if min == -1:
        break
    if min >4:
        colour_print(clock_face(min,sec), False, "plain", colour = "green", bold = False)
    elif min > 1:
        colour_print(clock_face(min,sec), False, "plain", colour ="golden", bold = False)
    elif min <= 1:
        colour_print(clock_face(min,sec), False, "plain", colour = "red", bold = False)
    if min == 0 and sec == 00:
        clear("check_clock.txt")
        with open("check_clock.txt", 'a', encoding="utf-8") as file:
            file.write("OVER\n")
        over = True
    sleep(1)
    clear()
else:
    with open("check_score.txt", 'a', encoding="utf-8") as lr:
        lr.write("timesup\n")
    colour_print(align("Time Over"), False, "plain", colour= "red", bold = True)
    input(":")