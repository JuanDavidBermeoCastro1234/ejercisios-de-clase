from logic.exercisesOne import save_course

def designOneList():
    course = input("whats the name of the course?")
    result = save_course(course)
    print(result)
    
def designOneDict():
    currency=input("whats the currency name? ")
    print(search_currency(currency))