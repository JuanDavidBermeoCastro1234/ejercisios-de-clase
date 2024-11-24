from tabulate import tabulate
from logic.exerciseSix  import fail_course, read_file,  save_file,user_data, display_data

def designSixList():
    
    failed= []  # Lista para almacenar las asignaturas fallidas

    subject = input(f" name of the Subject? : ")
    note = float(input(f"final Score of {subject}? : "))
    
    if note < 60:
        failed.append({"subject": subject, "note": note})
        fail_course(subject, note)
    data = read_file("exerciseSixlist.json")
    
    if "subject" in data and "finalNote" in data:
        for subject, note in zip(data["subject"], data["finalNote"]):
            if note <60:
                failed.append({"subject" :subject, "note": note})
    
    if failed:
        headers = ["SUBJECT", "NOTE"]
        table_notes = [(epicfail['subject'], epicfail['note']) for epicfail in failed]
        print( "\n You must retake these subjects :")
        print(tabulate(table_notes, headers=headers, tablefmt="grid"))
    else:
        print("no failed Subjects.")

#dict
def designSixDict():
    person_data = read_file("exerciseSixDict.json")
    while True:
        key = input("Enter the type of data (name, age, gender, etc.) or 'exit' to finish: ").lower()
        if key == "exit":
            print("Leaving and saving data")
            save_file(person_data)
            break
        value = input(f"Enter the value for {key}: ").strip()
        person_data = user_data(person_data, key, value)
        display_data(person_data)
