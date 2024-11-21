## Ejercicio 8

#Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla si es un palíndromo.
 
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
        
def save_word(word): 
        data = read_file("exerciseEightlist.json")
        data.append(word)
        write_file(data, "exerciseEightlist.json")

def palindrome(word):
     return word == word [::-1]

#dict

def read_translation_dict(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        return json.loads(data)

def write_translation_dict(diccionario, path):
    with open(f"databases/{path}", "wb+") as file:
        convertJson = json.dumps(diccionario, indent=4)
        file.write(convertJson.encode("utf-8"))
        file.close()

def create_translation_dict():
    diccionario = read_translation_dict("exerciseEightDict.json")
    palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
    for i in palabras.split(','):
        clave, valor = i.split(':')
        diccionario[clave.strip()] = valor.strip()
    write_translation_dict(diccionario, "exerciseEightDict.json")
    return diccionario

def translate_sentence(diccionario):
    frase = input('Introduce una frase en español: ')
    traduccion = []
    for palabra in frase.split():
        if palabra in diccionario:
            traduccion.append(diccionario[palabra])
        else:
            traduccion.append(palabra)
    return ' '.join(traduccion)
