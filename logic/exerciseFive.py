## Ejercicio 5

# Escribir un programa que almacene en una lista los
# números del 1 al 10 y los muestre por pantalla
# en orden inverso separados por comas.

import json

def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        convertirList = json.loads(data) 
        return convertirList
    
def write_file(data, path):
    with open(f"databases/{path}", "wb+") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
        
def save_numbers():
    data = read_file("exerciseFivelist.json")
    write_file(data, "exerciseFivelist.json")
    return data


#five diccionario

def show_credits():
    data = read_file("exerciseFiveDict.json")
    total_credits = 0 
    for subject, credits in data.items():
        print(f"{subject} has {credits} credits")
        total_credits += credits
        
    print(f"The total of credits is {total_credits}")