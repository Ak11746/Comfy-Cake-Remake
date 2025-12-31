import os

def get_dimentions(type: str = "both"):
    column, row = os.get_terminal_size()
    
    match type.lower():
        case "column":
            return column
        case "row":
            return row
        case "both":
            return column, row

def clear(name:str):
    with open(name, 'w'):
        pass

def check_conection(name:str, writing: bool= True, question: str= f'Connected Commarade?\n', answer: str = f"aai_aai captain\n"):
    if writing:
        with open(name.strip().lower(), 'a+', encoding="utf-8") as file:
            file.write(question)
            while True:
                for line in file:
                    if line == answer:
                        colour_print("Conection established with "+ name.split(".")[0].split("_")[1].title(), False, "plain", colour="green", bold = False)
                        break
                else:
                    continue
                break
    else:
        with open(name.strip().lower(), 'a+', encoding="utf-8") as file:
            while True:
                for line in file:
                    if line == question:
                        file.write(answer)
                        colour_print("Conection established", False, "plain", colour="green", bold = False)
                        break
                else:
                    continue
                break

def  start(name):
    with open(name, 'r', encoding="utf-8") as file:
        while True:
            for line in file:
                if line == "start\n":
                    colour_print("Starting\n", False, "plain", colour="green", bold = False)
                    break
            else:
                continue
            break

def starter(list:list):
    for name in list:
        with open(name, 'a', encoding="utf-8") as file:
            file.write("start\n")

def error():
    print("Incorrect Arguments")

def colour_print(s, value= "print", colour_scheme= "og", **prop):
    if value in ["print", False, "value", True, "code"] and colour_scheme in ["plain", 3, "og", 4, "256", 256, 8, "rgb", 24]:
        match colour_scheme:
            case "plain" | 3:
                data = {}
                if len(prop) == 2:
                    for i in ["colour", "bold"]:
                        for j in prop:
                            if i.lower() == j.lower():
                                data[i] = prop.get(j)
                                break
                        else:
                            error()
                            break
                else:
                    error()

                match str(data["colour"]).lower():
                    case "red":
                        data["colour"] = 91
                    case "green":
                        data["colour"] = 92
                    case "golden" | "mustard" | "yellow":
                        data["colour"] = 93
                    case "blue":
                        data["colour"] = 94
                    case "pink" | "magenta":
                        data["colour"] = 95
                    case "cyan":
                        data["colour"] = 96
                    case "white":
                        data["colour"] = 97
                    case "black":
                        data["colour"] = 98
                    case _:
                        error()

                match value.lower() if str(type(value)).find("bool") == -1 else value:
                    case "print" | False:
                        print(f"\033[{int(data['bold'])};{int(data['colour'])}m{s}\033[00m")
                    case "value" | True:
                        return f"\033[{int(data['bold'])};{int(data['colour'])}m{s}\033[00m"
                    case "code":
                        return f"\033[{int(data['bold'])};{int(data['colour'])}m"
                    
            case "og" | 4:
                data = {}
                if len(prop) == 3:
                    for i in ["bg","fg", "bold"]:
                        for j in prop:
                            if i.lower() == j.lower():
                                data[i] = prop.get(j)
                                break
                        else:
                            error()
                            break
                else:
                    error()

                match data["bg"].lower():
                    case "black":
                        data["bg"] = 40
                    case "red":
                        data["bg"] = 41
                    case "green":
                        data["bg"] = 42
                    case "golden" | "mustard" | "yellow":
                        data["bg"] = 43
                    case "blue":
                        data["bg"] = 44
                    case "pink" | "magenta":
                        data["bg"] = 45
                    case "cyan":
                        data["bg"] = 46
                    case "white":
                        data["bg"] = 47

                match data["fg"].lower():
                    case "black":
                        data["fg"] = 30
                    case "red":
                        data["fg"] = 31
                    case "green":
                        data["fg"] = 32
                    case "golden" | "mustard" | "yellow":
                        data["fg"] = 33
                    case "blue":
                        data["fg"] = 34
                    case "pink" | "magenta":
                        data["fg"] = 35
                    case "cyan":
                        data["fg"] = 36
                    case "white":
                        data["fg"] = 37
            


                match value.lower() if str(type(value)).find("bool") == -1 else value:
                    case "print" | False:
                        print(f"\033[{int(data['bold'])};{int(data['fg'])};{int(data['bg'])}m{s}\033[00m")
                    case "value" | True:
                        return f"\033[{int(data['bold'])};{int(data['fg'])};{int(data['bg'])}m{s}\033[00m"
                    case "code":
                        return f"\033[{int(data['bold'])};{int(data['fg'])};{int(data['bg'])}m"
            
            case "256" | 256 | 8:
                data = {}
                if len(prop) == 2:
                    for i in ["layer", "code"]:
                        for j in prop:
                            if i.lower() == j.lower():
                                data[i] = prop.get(j)
                                break
                        else:
                            error()
                            break
                else:
                    error()
                match value.lower() if str(type(value)).find("bool") == -1 else value:
                    case "print" | False:
                        print(f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{5};{data['code']}m{s}\033[00m")
                    case "value" | True:
                        return f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{5};{data['code']}m{s}\033[00m"
                    case "code":
                        return f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{5};{data['code']}m"
            
            case "rgb" | 24:
                data = {}
                if len(prop) == 4:
                    for i in ["layer", "red", "green", "blue"]:
                        for j in prop:
                            if i.lower() == j.lower():
                                data[i] = prop.get(j)
                                break
                        else:
                            error()
                            break
                else:
                    error()

                match value.lower() if str(type(value)).find("bool") == -1 else value:
                    case "print" | False:
                        print(f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{2};{int(data['red'])};{int(data['green'])}:{int(data['blue'])}m{s}\033[00m")
                    case "value" | True:
                        return f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{2};{int(data['red'])};{int(data['green'])}:{int(data['blue'])}m{s}\033[00m"
                    case "code":
                        return f"\033[{48 if str(data['layer']).lower() == 'bg' else 38};{2};{int(data['red'])};{int(data['green'])}:{int(data['blue'])}m"
            



    else:
        error()

def end_code():
    return f"\033[00m"


def space(s):
    max_len = 0
    for i in str(s).split("\n"):
        max_len = len(i) if len(i) > max_len else max_len
    rem_col = get_dimentions("column") - max_len
    if rem_col % 2 == 0:
        left = right = rem_col/2 
    else:
        left = int((rem_col//2)+1)
        right = int(rem_col//2)
    return left,right
    
def align(s, pos = "center"):
    left,right = space(s)

    row = str(s).split("\n")
    for i in range(len(row)-1 , -1 , -1):
        if len(row[i]) == 0:
            row.pop(i)
        else:   
            if pos == "center":     
                row[i] = " "*int(left) + row[i] + " "*int(right)
            elif pos == "right":
                row[i] = " "*(int(left)+int(right)) + row[i]
            else:
                error()
    s_new = "\n".join(row)
    return  s_new 

def animate(text:str):
    frame = text.split("\n")
    text = ""
    for i in range(len(frame)):
        line = list(frame[i])
        line.insert(0, line.pop())
        frame[i] = ''.join([str(c) for c in line])
        text = text + str(frame[i])
    return text

if __name__ == "__main__":
    print(animate("123"))
    colour_print("abc",False,"og", bg = "black", fg = "cyan", bold = True)
    colour_print("abc", False, "rgb", layer = "fg", red = "250", green = "150", blue = "50")    
    print(colour_print("Hello@Hello", True, "plain", colour = "pink").replace("@", end_code() + colour_print("", "code", "256", layer = "fg", code = "178")))
    