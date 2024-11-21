from logic.exerciseEight import save_word, read_file, write_file, palindrome,create_translation_dict, translate_sentence

def designEightList():
    word = input("\nimput whatever word  : ").strip()

    if palindrome(word):
        print(f"\nThe word '{word}' is a palindrome. ")
    else:
        print(f"\nThe word '{word}' is NOT a palindrome. ")
    save_word(word)

#dict
def designEightDict():
    diccionario = create_translation_dict()
    traduccion = translate_sentence(diccionario)
    print(traduccion)
