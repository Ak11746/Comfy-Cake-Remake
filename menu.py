from os import system
from time import sleep
from functions import *
input(":")
while True:
    clear()
    colour_print(align("Computer Science Project 2025-26"), False, "plain", colour="cyan", bold=True)
    colour_print(align("Team: Akhilesh Kumar Bhardwaj, Rajinder Singh, Raghav Sharma"), False, "plain", colour="cyan", bold=True)
    print()
    print()
    colour_print("Select an option:", False, "plain", colour="blue", bold=True)
    colour_print(" 1. Comfy Cake Remake", False, "plain", colour="green", bold=False)
    colour_print(" 2. Number guesser", False, "plain", colour="green", bold=False)
    match input(": "):
        case "1":
            colour_print("Comfy Cake Remake Selected", False, "plain", colour="green", bold=True)
            system('python main.py')
            system('python orders.py')
            system('python progress.py')
            system('python clock.py')
            system('python score.py')
            sleep(1)
            exit()
        case "2":
            colour_print("Number Guesser Selected", False, "plain", colour="green", bold=True)
            system('python project_2.py')
            sleep(1)
            exit()
        case _:
            colour_print("Select the correct option", False, "plain", colour="red", bold=True)
            sleep(0.5)