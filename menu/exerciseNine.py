from logic.exerciseNine import counterSuperPro,save_word,add_invoice, pay_invoice, show_summary, read_file, write_file

def designNineList():
    word = input("\nimput whatever word  : ").strip().lower()

    vowelsCounts = counterSuperPro(word)

    print(f"\n in the word '{word}' the vowels appear in this order ")
    for vowel, count in vowelsCounts.items():
        print(f"{vowel}: {count}")

    save_word(word)


#dict
def designNineDict():
    invoices = read_file("exerciseNineDict.json")
    while True:
        print("\n1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            invoices = add_invoice(invoices)
        elif choice == "2":
            invoices = pay_invoice(invoices)
        elif choice == "3":
            write_file(invoices, "exerciseNineDict.json")
            break
        else:
            print("Opción no válida.")
        
        show_summary(invoices)
