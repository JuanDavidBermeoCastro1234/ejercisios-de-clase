
from logic.exercisesTwo import save_subjects

def designTwoList():
    course = input ("whats the name of the subject? : ")

    result = save_subjects(course)

    for course in result:
        print(f"I'm study : {course}")
         

         