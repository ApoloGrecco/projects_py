def soma (num1, num2):
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    soma_local = num1 + num2
    return print("A soma dos dois numeros sao: {}" .format(soma_local))

def subtracao (num1, num2):
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    sub_local = num1 - num2
    return print("A subtracao dos dois numeros sao: {}" .format(sub_local))

def multip (num1, num2):
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    multip_local = num1 * num2
    return print("A multiplicacao dos dois numeros sao: {}" .format(multip_local))

def divisao (num1, num2):
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    div_local = num1 / num2
    return print("A divisão dos dois numeros sao: {}".format(div_local))

n1 = 0
n2 = 0

print("******************** Python Calculator ********************\n")

print("Selecione o numero da operacao desejada: \n")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

opc = int(input("Digite sua opcao (1/2/3/4): "))
print("\n")

if opc == 1:
    soma (n1,n2)

elif opc == 2:
    subtracao (n1,n2)

elif opc == 3:
    multip(n1,n2)

elif opc == 4:
    divisao(n1,n2)

else:
    print("Opcao incorreta!")