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

