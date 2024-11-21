
from logic.exercisesTwo import save_subjects, write_info


def designTwoList():
    course = input ("whats the name of the subject? : ")

    result = save_subjects(course)

    for course in result:
        print(f"I'm study : {course}")
         

#dict

def designTwoDict():
    adress = input("Enter your adress: ")
    age = input("Enter your age: ")
    phone = input("Type your phone number: ")
    name = input("Enter your name: ")
    write_info(name, age, adress, phone)
    print(f"{name} is {age}, lives in {adress} and his phone number is {phone}")