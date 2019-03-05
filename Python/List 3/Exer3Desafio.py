numero = int(input("Digite um número para verificar se ele é primo: "))
result = True
i = 2
while i < numero:
    if numero % i == 0:
        result = False
    i += 1
if result:
    print("É primo")
else:
    print("Não é primo")