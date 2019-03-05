numero = int(input("Digite um número para obter o seu número invertido: "))
numberString = ""
tamanhoNumber = len(str(numero))
numeroAux = numero
while tamanhoNumber > 0:
    rest = numeroAux % 10
    numeroAux = int(numeroAux / 10)
    numberString = numberString+str(rest)
    tamanhoNumber -= 1
invert = int(numberString)
print(invert)