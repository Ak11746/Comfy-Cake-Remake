from functions import *
input(":")
check_conection("check_progress.txt", False)
start("check_progress.txt")
clear("check_progress.txt")
clear()
colour_print("Orders:\n", False, "plain", colour = "blue", bold = True)
with open("check_progress.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            clear()
            print(line.replace("`", "\n"))
