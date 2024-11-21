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
        
def counterSuperPro(word):
    vowels = 'aeiou'
    counter = {vowel: word.count(vowel) for vowel in vowels}
    return counter

def save_word(word): 
        data = read_file("exerciseNinelist.json")
        data.append(word)
        write_file(data, "exerciseNinelist.json")


#dict
def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        return json.loads(data)

def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)
        file.close()

def add_invoice(invoices):
    num_factura = input("Introduce el número de factura: ")
    costo = float(input("Introduce el coste de la factura: "))
    invoices[num_factura] = costo
    return invoices

def pay_invoice(invoices):
    num_factura = input("Introduce el número de factura a pagar: ")
    if num_factura in invoices:
        del invoices[num_factura]
        print(f"Factura {num_factura} pagada y eliminada.")
    else:
        print(f"Factura {num_factura} no encontrada.")
    return invoices

def show_summary(invoices):
    total_pending = sum(invoices.values())
    total_paid = 0 
    print(f"Total cobrado hasta el momento: {total_paid}")
    print(f"Total pendiente de cobro: {total_pending}")
