from functions import *
input(":")
check_conection("check_order.txt", False)
start("check_order.txt")
clear("check_order.txt")
print("\033[2J\033[1;1H")
colour_print("Orders:\n", False, "plain", colour = "blue", bold = True)
with open("check_order.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            print("\033[2J\033[1;1H")
            print(line.replace("`", "\n"))
