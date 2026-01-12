from functions import *
input(":")
check_conection("check_order.txt", False)
start("check_order.txt")
clear("check_order.txt")
clear()
colour_print("Orders:\n", False, "plain", colour = "blue", bold = True)
with open("check_order.txt", 'r', encoding="utf-8") as file:
    while True:
        for line in file:
            clear()
            print(line.replace("`", "\n"))
