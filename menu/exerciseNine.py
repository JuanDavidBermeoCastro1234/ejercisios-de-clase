from logic.exerciseNine import counterSuperPro,save_word

def designNineList():
    word = input("\nimput whatever word  : ").strip().lower()

    vowelsCounts = counterSuperPro(word)

    print(f"\n in the word '{word}' the vowels appear in this order ")
    for vowel, count in vowelsCounts.items():
        print(f"{vowel}: {count}")

    save_word(word)
