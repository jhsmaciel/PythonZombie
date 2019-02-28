salario  =   float(input('Digite o valor do salário: '))

salarioAjuste  =   float(input('Digite a porcentagem do ajuste salarial: '))

ajuste = salario * (1 + (salarioAjuste/100))

print ('Salário atual %.2f' %ajuste)