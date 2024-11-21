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

#ejercicio diccionario
def format_date(date):
    date_parts = date.split("/")
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    data = read_file("exerciseFourdict.json")
    month_ind = int(date_parts[1])
    if not (1 <= month_ind <= 12): 
        raise ValueError("Invalid number for the month, try between 1 - 12")
    format = {
        "day": int(date_parts[0]),
        "month": month[month_ind - 1],
        "year": date_parts[2],
        "message": f"{date_parts[0]} of {month[month_ind - 1]} of {date_parts[2]}"
    }
    data.append(format)
    write_file(data, "exerciseFourdict.json")
    
    return format.get("message")