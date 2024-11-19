import json  

import json
def read_file():
    with open ("databases/exerciseSevendict.json", "r") as file :
        datos=file.read()
        convertirdict=json.loads(datos)
        return convertirdict

def write_file (data):
    with open ("databases/exerciseSevendict.json", "wb+") as file :
        convertirjson= json.dump(data, indent=4).encode ("utf-8")
        file.write(convertirjson)
        file.close()


def saveCourse (articule):
    data=read_file()
    data.append(articule)
    write_file(data)
    return data 








