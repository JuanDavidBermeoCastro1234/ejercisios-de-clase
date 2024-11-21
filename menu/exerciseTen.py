from logic.exerciseTen import save_numbers

def designTenList():

    result = save_numbers()
    
    result.sort()

    print(f"el numero menor es: {result[-1]}")
    print(f"el numero mayor es: {result[0]}")
    