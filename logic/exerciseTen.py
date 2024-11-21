## Ejercicio 10

# Escribir un programa que almacene en una lista los siguientes 
# precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla 
# el menor y el mayor de los precios.

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
        
def save_numbers():
    data = read_file("exerciseTenlist.json")
    write_file(data, "exerciseTenlist.json")
    return data


#dict
def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        return json.loads(data)

def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)

def add_client(database, nif, name, address, phone, email,preferent):
    database[nif] = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "preferent": preferent
    }
    write_file(database, "exerciseTenDict.json")
    print(f"Client {name} added successfully.")

def remove_client(database, nif):
    if nif in database:
        del database[nif]
        write_file(database, "exerciseTenDict.json")
        print(f"Client with NIF {nif} removed successfully.")
    else:
        print("Client not found.")
    
def show_client(database, nif):
    if nif in database:
        client = database[nif]
        print(f"Client {nif}: {client['name']}")
        print(f"Address: {client['address']}")
        print(f"Phone: {client['phone']}")
        print(f"Email: {client['email']}")
        print(f"Preferent: {'Yes' if client['preferent'] else 'No'}")
    else:
        print("Client not found.")

def list_all_clients(database):
    print("\nAll clients:")
    for nif, client in database.items():
        print(f"NIF: {nif}, Name: {client['name']}")
    
def list_preferent_clients(database):
    print("\nPreferent clients:")
    for nif, client in database.items():
        if client["preferent"]:
            print(f"NIF: {nif}, Name: {client['name']}")