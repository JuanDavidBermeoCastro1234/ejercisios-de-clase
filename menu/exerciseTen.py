from logic.exerciseTen import save_numbers,read_file, add_client, remove_client, show_client, list_all_clients, list_preferent_clients

def designTenList():

    result = save_numbers()
    
    result.sort()

    print(f"el numero menor es: {result[-1]}")
    print(f"el numero mayor es: {result[0]}")


#dict
def designTenDict():
    database = read_file("exerciseTenDict.json")
    while True:
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")

        option = input("Elija una opción: ")

        if option == "1":
            nif = input("Introduce el NIF del cliente: ")
            name = input("Introduce el nombre del cliente: ")
            address = input("Introduce la dirección del cliente: ")
            phone = input("Introduce el teléfono del cliente: ")
            email = input("Introduce el correo electrónico del cliente: ")
            preferent = input("¿Es un cliente preferente? (si/no): ").lower() == "si"
            add_client(database, nif, name, address, phone, email, preferent)

        elif option == "2":
            nif = input("Introduce el NIF del cliente a eliminar: ")
            remove_client(database, nif)

        elif option == "3":
            nif = input("Introduce el NIF del cliente a mostrar: ")
            show_client(database, nif)

        elif option == "4":
            list_all_clients(database)

        elif option == "5":
            list_preferent_clients(database)

        elif option == "6":
            break

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 6.")
