## Ejercicio 4

# Escribir un programa que pregunte al usuario los números ganadores de la lotería 
# primitiva, los almacene en una lista y 
# los muestre por pantalla ordenados de menor a mayor.

from logic.exerciseFour import save_numbers, format_date

def designFourList():
    number= int(input ("whats the number  the lotery? : "))

    result = save_numbers(number)
    
    result.sort()
    print(result)



def designFourDict():
    date = input("What is the date? ")
    print(format_date(date))
    return 0