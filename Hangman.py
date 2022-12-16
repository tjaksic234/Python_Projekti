import random
word_list=['grlica','predsjednik','gospa','jelka','stolica','zavjesa']

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Igrajmo vješala!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Pogodi slovo ili rijec:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Vec si pogodio slovo", guess)
            elif guess not in word:
                print(guess,"nije u rijeci!!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Pogodio si slovo", guess, "je slovo koje se trazi!!!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index  in indices:
                    word_as_list[index] = guess
                    word_completion = ''.join(word_as_list)
                if  '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Vec si pogodio rijec", guess)
            elif guess != word:
                print(guess,"nije rijec koja se trazi")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Ne prihvaca se pokusaj")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Cestitam pogodio si rijec :D !!!")
    else:
        print("Zao mi je ostao si bez pokusaja trazila se rijec",word)
def display_hangman(tries):
    stages = [  # glava, trup, obe ruke i noge
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # glava, trup, obe ruke i jedna noga
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # glava, trup i obe ruke
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # glava, trup i jedna ruka
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # glava i trup
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # samo glava
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # prazno
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while input("Zelite li igrati opet? (Y/N)").upper() == 'Y':
        word = get_word()
        play(word)
main()