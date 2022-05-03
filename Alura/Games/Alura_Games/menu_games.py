import forca
import adivinhacao

def choose_game():
    print("\n***********************************")
    print("********Escolha o seu jogo!********")
    print("***********************************\n")

    print("(1) Forca (2) Adivinhação")

    game = int(input("Escolha seu jogo: "))

    while (game <= 0 or game >= 3):
        print("Jogo inválido!")
        game = int(input("Escolha novamente seu jogo: "))
        continue

    if (game == 1):
        print("Jogando forca")
        forca.play()
    elif (game == 2):
        print("Jogando advinhança")
        adivinhacao.play()

if(__name__== "__main__"):
    choose_game()