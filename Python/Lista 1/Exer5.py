precoProduto  =   float(input('Digite o valor do produto: '))

precoAjuste  =   float(input('Digite a porcentagem de desconto: '))

ajuste = precoProduto * (1-(precoAjuste/100))

print ('Salário atual %.2f' %ajuste)