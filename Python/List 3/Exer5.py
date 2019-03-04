valorUm = int(input("Digite o primeiro valor para fazer o MDC: "))
valorDois = int(input("Digite o segundo valor para fazer o MDC: "))
valorBaixo = -1
MDC = 1
if valorUm > valorDois:
    valorBaixo = valorDois
else:
    valorBaixo = valorUm

valorDiv = 1
while valorDiv < valorBaixo:
    print(valorDiv)
    if valorUm % valorDiv == 0 and valorDois % valorDiv  == 0:
        MDC = valorDiv
    valorDiv += 1
print("O máximo divisor comum é %d"%MDC)

