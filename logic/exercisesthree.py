
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
        
def save_course(course, note):
    data = read_file("exercisesThreelist.json")
    data["course"].append(course)
    data["grade"].append(note)

    write_file(data, "exercisesThreelist.json")
    return data

#ejercicio dict

def search_fruit(fruit):
    data = read_file("exerciseThreedict.json")
    dataLower = {key.lower(): value for key, value in data.items()}
    if fruit in dataLower:
        return dataLower[fruit]
    else:
        return None    

def fruit_price(fruit, weight):
    price = search_fruit(fruit)
    if price is not None:
        return price * weight
    else: 
        return "Fruit not found"