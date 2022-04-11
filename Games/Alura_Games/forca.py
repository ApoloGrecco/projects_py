from random import randrange


def play():

    welcome_game()
    secret_word = loading_secret_word()

    correct_letters = inicialize_words_right(secret_word)
    print(f"Tente adivinhar a palavra: {correct_letters}\n")

    hanged = False
    right = False
    mistakes = 0

    print(secret_word)

    while(not hanged and not right):

        kick = give_kick()

        if(kick in secret_word):
            succes_kick(kick, correct_letters, secret_word)
        else:
            mistakes += 1
            desenha_forca(mistakes)

        hanged = mistakes == 7
        right = "_" not in correct_letters
        print(correct_letters)

    if(right):
        print_victory()
    else:
        print_defeat(secret_word)




def welcome_game():
    print("\n***********************************")
    print("****Bem-vindo ao jogo da Forca!****")
    print("***********************************\n")

def loading_secret_word():
    with open("words.txt") as archive:
        words = []
        for line in archive:
            line = line.strip()
            words.append(line)

    word_number = randrange(0, len(words))
    secret_word = words[word_number].upper()
    return secret_word

def inicialize_words_right(word):
    return ["_" for letter in word]

def give_kick():
    kick = input("Digite uma letra: ").strip().upper()
    return kick

def succes_kick(kick, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (kick.upper() == letter.upper()):
            correct_letters[index] = letter
        index += 1
    print(f"Você acertou a letra {kick}\n")

def print_victory():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_defeat(secret_word):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__== "__main__"):
    play()


