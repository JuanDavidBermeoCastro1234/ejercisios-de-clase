import json
import os

def read_file():
    try:
        with open("databases/exerciseSevendict.json", "r", encoding="utf-8") as file:
            datos = file.read()
            convertirdict = json.loads(datos)
            return convertirdict
    except FileNotFoundError:
        # Si el archivo no existe, retorna una lista vacía
        return []
    except json.JSONDecodeError:
        # Si el archivo está corrupto o vacío, retorna una lista vacía
        return []

def write_file(data):
    with open("databases/exerciseSevendict.json", "w", encoding="utf-8") as file:
        # Escribe directamente la data en formato JSON
        json.dump(data, file, indent=4, ensure_ascii=False)

def saveCourse(articule):
    data = read_file()
    data.append(articule)
    write_file(data)
    return data
