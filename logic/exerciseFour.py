## Ejercicio 4

# Escribir un programa que pregunte al usuario los números ganadores de la lotería 
# primitiva, los almacene en una lista y 
# los muestre por pantalla ordenados de menor a mayor.

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
        
def save_numbers(number):
    data = read_file("exerciseFourlist.json")
    data.append(number)
    write_file(data, "exerciseFourlist.json")
    return data

