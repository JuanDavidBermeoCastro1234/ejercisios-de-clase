from logica.exerciseOne import saveCourse
from tabulate import tabulate


def designOnelist ():

    course =input("what is the course name? ")
    grade = int(input ("and what the grade ?"))
    result= saveCourse(course, grade)
    table_data=list(zip(result["signature"], result ["grade"]))

    headers=["course", "grade"]
    print("\n current Course And Grades ")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
   