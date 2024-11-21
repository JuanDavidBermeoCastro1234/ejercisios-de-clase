
import json

def read_file(path):
    with open(f"databases/{path}", "r", encoding="utf-8") as file:
        data = file.read()
        convertirList = json.loads(data) 
        return convertirList
    
def write_file(data, path):
    with open(f"databases/{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_course(course):
    data = read_file("exercisesOnelist.json")
    data.append(course)
    write_file(data, "exercisesOnelist.json")
    return data


#diccionario 
def search_currency(currency):
    data = read_file("exerciseOnedict.json")
    if (data.get(currency)):
        return data.get(currency)
    else:
        return "Currency not found"


