from logic.exercisesSeven import read_file, write_file, reset,save_product
from tabulate import tabulate

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


#dict
def designSevenDict():
    while True:
        product = input("What is the product name?: ")
        cost = float(input("And whats the cost?: "))
        result = save_product(product, cost)
        product_list = result["PRODUCT"] 
        cost_list = result["COST"]
        table_data = [(product_list[i], cost_list[i]) for i in range(len(product_list))]   
        total_cost = sum(cost_list)
        table_data.append(("Total", total_cost))
        headers = ["Buying list", "Cost"]
        print(tabulate(table_data, headers=headers, tablefmt="grid", numalign="right"))
        again = input("Do you want to add another product? (yes/no): ")
        if again.lower() != "yes":
            break 
        