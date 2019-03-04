n = int(input("Digite um número para exibir a sequência de fibonacci até o valor digitado: "))

a,b=0,1

while b < n:
    print(b)
    a,b = b,a+b