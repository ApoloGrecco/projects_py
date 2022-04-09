from random import randrange

print("***********************************")
print("*Bem-vindo ao jogo de Adivinhação!*")
print("***********************************")

total_attempts = 0
number_secret = randrange(1, 101)
points = 1000

print("Tente adivinhar o número entre 1 á 100!")
print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

while (nivel > 3):
    print ("Nível inválido!")
    nivel = int(input("Define o nível: "))
    continue

if (nivel == 1):
        total_attempts = 20
elif (nivel == 2):
        total_attempts = 10
elif (nivel == 3):
        total_attempts = 5

print("Começando o jogo digite o número!\n")

for attempt in range(1, total_attempts + 1):
    print(f"Tentativa {attempt} de {total_attempts}")
    kick = int(input("Digite seu número: "))

    if(kick < 1 or kick > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    right = kick == number_secret
    bigger = kick > number_secret
    smaller = kick < number_secret

    if(right):
        print(f"Parabéns você acertou o número e fez {points} pontos!")
        break
    else:
        if(bigger):
            print(f"Você errou! O seu chute foi maior que o número!")
        elif (smaller):
            print(f"Você errou! O seu chute foi menor que o número!")
        lost_points = abs(number_secret - kick)
        points = points - lost_points


print("Fim de jogo!")
