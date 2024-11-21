from logic.exerciseEight import save_word, read_file, write_file, palindrome

def designEightList():
    word = input("\nimput whatever word  : ").strip()

    if palindrome(word):
        print(f"\nThe word '{word}' is a palindrome. ")
    else:
        print(f"\nThe word '{word}' is NOT a palindrome. ")
    save_word(word)
