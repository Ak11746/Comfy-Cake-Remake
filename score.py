from functions import *
from keyboard import press
from prettytable import PrettyTable
from time import sleep

input(":")
check_conection("check_score.txt", False)
data = {"left": 0, "baked": 0, "destroyed": 0}
score = {"score": 0, "out of": 0}
with open("check_score.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            if line in ["5\n", "6\n", "7\n"]:
                match line:
                    case "5\n":
                        data["left"] = 5
                        score["out of"] = 25
                    case "6\n":
                        data["left"] = 6
                        score["out of"] = 30
                    case "7\n":
                        data["left"] = 7
                        score["out of"] = 35
                colour_print("Difficulty level recieved", False, "plain", colour="green", bold = False)
                break
        else:
            continue
        break

start("check_score.txt")
print("\033[2J\033[1;1H")
print("*"*get_dimentions("column"))
colour_print(align("SCORE CARD"), False, "plain", colour = "blue", bold = True)
print("*"*get_dimentions("column"))
print()

def over(d,s):
    input("Ding Ding Ding")
    print("\033[2J\033[1;1H")
    press("f11")
    sleep(0.2)
    print("*"*get_dimentions("column"))
    colour_print(align("OVER"), False, "plain", colour = "blue", bold = True)
    print("*"*get_dimentions("column"))
    colour_print(align("Score Card"), False, "plain", colour = "blue", bold = True)
    print("*"*get_dimentions("column"))
    table = PrettyTable()
    table.field_names = ["Cake", "Value"]
    for i in d:
        table.add_row([i, d[i]])
    table.add_divider()
    table.add_row(["Score", "Out of"], divider=True)
    table.add_row([s["score"], s['out of']])
    colour_print(align(table.get_string()), False, "plain", colour ="Green", bold= True)

with open("check_score.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            if line in ["+\n", "-\n", "timesup\n"]:
                match line:
                    case "+\n":
                        data["left"] -= 1
                        data["baked"] +=1
                        score["score"] +=5
                    case "-\n":
                        data["left"] -= 1
                        data["destroyed"] +=1
                        score["score"] -=5
                    case "timesup\n":
                        over(data, score)
                        input(":")
                        exit()
                print("\033[2J\033[1;1H")
                print("*"*get_dimentions("column"))
                colour_print(align("SCORE CARD"), False, "plain", colour = "blue", bold = True)
                print("*"*get_dimentions("column"))
                print()
                for value in data:
                    colour_print(f"No. of cakes {value}: "+str(data[value]), False, "plain", colour = "blue", bold = False)
                print()
                colour_print(f"Score: "+str(score["score"])+"/"+str(score["out of"]), False, "plain", colour = "pink", bold = True)
            if score["score"]==score["out of"]:
                colour_print("\n"+align("You Won!!!")+"\n", False, "plain", colour = "green", bold = True)
                over(data, score)
                input(":")
                exit()
            elif data["left"]==0:
                colour_print("\n"+align("You Fail!!!")+"\n", False, "plain", colour = "Red", bold = True)
                over(data, score)
                input(":")
                exit()