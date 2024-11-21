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