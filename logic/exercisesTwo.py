# ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje `Yo estudio <asignatura>`, donde `<asignatura>` es cada una de las asignaturas de la lista.

from logic.exercisesOne import read_file, write_file 


def save_subjects(course):
        subjects = read_file("exercisesTwolist.json")
        subjects.append(course)
        write_file(subjects, "exercisesTwolist.json")
        return subjects

#dict
def write_info(name, age, adress, phone):
    data = read_file("exerciseTwoDict.json")
    data.append(name)
    data.append(age)
    data.append(adress)
    data.append(phone)
    write_file(data, "exerciseTwoDict.json")
    return data
