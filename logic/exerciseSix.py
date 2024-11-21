## Ejercicio 6

# Escribir un programa que almacene las asignaturas de un 
# curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en 
# cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas 
# que el usuario tiene que repetir.


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
        
def fail_course(course, note):
    data = read_file("exerciseSixlist.json")
    data["subject"].append(course)
    data["finalNote"].append(note)
    write_file(data, "exerciseSixlist.json")
    return data


#dict
import json
def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        return json.loads(data)
         
def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)
        file.close()

def save_file(person_data):
    write_file(person_data, "exerciseSixDict.json")

def user_data(person_data, key, value):
    person_data[key] = value
    return person_data

def display_data(person_data):
    print("\nCurrent data:")
    for k, v in person_data.items():
        print(f"{k.capitalize()}: {v}")
    print()

