## Ejercicio 10

# Escribir un programa que almacene en una lista los siguientes 
# precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla 
# el menor y el mayor de los precios.

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
    data = read_file("exerciseTenlist.json")
    write_file(data, "exerciseTenlist.json")
    return data
