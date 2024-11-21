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
