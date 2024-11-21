from logic.exercisesSeven import read_file, write_file, reset

def designSevenList():

    data = read_file("exerciseSevenlist.json")


    if not data["alphabet"]:

        data["alphabet"] = list("abcdefghijklmnopqrstuvwxyz")
        write_file(data, "exercisesSevenlist.json")
        
        print("\nAlphabet: ", data["alphabet"])
        
        everyThree = [letra for i, letra in enumerate(data["alphabet"], start=1) if i % 3 !=0]
        
        data["filTered"] = everyThree
        write_file(data, "exercisesSevenlist.json")

        print("\n\nAlphabet modified: ", everyThree)

        reset("exerciseSevenlist.json")
        print("\nthe file has been reset for next execution ")

        