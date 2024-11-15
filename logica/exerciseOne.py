import json
def read_file():
    with open ("databases/exerciseOneList.json","r") as file :
        data =file.read()
        convertirList= json .loads(data)
        return convertirList

def write_file(data):
    with open ("databases/exerciseOneList.json","wb+") as file :
        ConvertirJson= json.dump(data, indent=4).encode("utf-8")
        file.write(ConvertirJson)
        file.close()


    def save_course(course):
        data= read_file()
        data.append(course)
        write_file(data)
        return data
