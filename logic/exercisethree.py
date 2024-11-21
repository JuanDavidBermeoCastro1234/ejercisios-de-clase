
import json

def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        convertirList = json.loads(data) 
        return convertirList
    
def write_file(data, path):
    with open(f"databases/{path}", "wb+") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
        
def save_course(course, note):
    data = read_file("exercisesThreelist.json")
    data["subject"].append(course)
    data["finalNote"].append(note)

    write_file(data, "exercisesThreelist.json")
    return data

