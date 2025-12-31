from functions import *
input(":")
check_conection("check_progress.txt", False)
start("check_progress.txt")
clear("check_progress.txt")
print("\033[2J\033[1;1H")
colour_print("Orders:\n", False, "plain", colour = "blue", bold = True)
with open("check_progress.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            print("\033[2J\033[1;1H")
            print(line.replace("`", "\n"))
