## Ejercicio 3

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje `En <asignatura> has sacado <nota>` donde `<asignatura>` 
# es cada una des las asignaturas de la lista y `<nota>` cada una de las correspondientes notas introducidas por el usuario.


from tabulate import tabulate
from logic.exercisesthree import save_course, fruit_price

def designThreeList():
    course = input("whats the name of the Subject? :  ")
    note = float(input("whats the note of the Subject? :  "))
    result = save_course(course, note)
    print(result)

    table_notes = list(zip(result["course"], result["grade"]))

    headers = ["COURSE", "NOTES"]
    
    print("\subjects with Final notes:  ")
    print(tabulate(table_notes, headers=headers, tablefmt="grid" ))


#diccionario
def designThreeDict():
    fruit = input("Enter the fruit: ")
    try: 
        weight = float(input("Enter the weight in kilos of that fruit: "))
    except ValueError:
        print("Invalid weight. Please enter a number.")
        return
    
    total_price = fruit_price(fruit, weight)
    print(f"The price of {weight} kg of {fruit} is: {total_price}")


