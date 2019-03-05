valor = int(input("Entre com um valor, para definir a quantidade de notas: "))
rest0 = 0
nota50, nota20, nota10, nota5, nota2, moeda1 = 0,0,0,0,0,0
if valor>=50:
    rest0 = valor % 50
    nota50 = (valor - rest0) / 50
    valor = rest0
    print(valor)
if valor >= 20:
    rest0 = valor % 20
    nota20 = (valor - rest0) / 20
    valor = rest0
if valor >=10:
    rest0 = valor % 10
    nota10 = (valor - rest0) / 10
    valor = rest0
if valor >=5:
    rest0 = valor % 5
    nota5 = (valor - rest0) / 5
    valor = rest0
if valor >=2:
    rest0 = valor % 2
    nota2 = (valor - rest0) / 2
    valor = rest0
if valor == 1:
    moeda1 = valor  
print("%.0f notas de 50"%nota50)
print("%.0f notas de 20"%nota20)
print("%.0f notas de 10"%nota10)
print("%.0f notas de 5"%nota5)
print("%.0f notas de 2"%nota2)
print("%.0f moedas de 1"%moeda1)
