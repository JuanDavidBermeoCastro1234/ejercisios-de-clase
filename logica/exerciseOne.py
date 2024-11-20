from tabulate import tabulate 
import json 

def read_file(path):
    with open (f"databases/{path}","r") as file :
        datos =file.read()
        convertirList= json.loads(datos)
        return convertirList

def write_file(datos,path):
    with open (f"databases/{path}","w+") as file :
        ConvertirJson= json.dump(datos, indent=4).encode("utf-8")
        file.write(ConvertirJson)
        file.close()


def saveCourse(course, grade ):
    data=read_file("exerciseOnelist.json")
    data["signature"].append(course)
    data["grade"].append(grade)
    write_file(data,"exerciseOnelist.json")
    return data
