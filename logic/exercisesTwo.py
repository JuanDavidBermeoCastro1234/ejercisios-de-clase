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

