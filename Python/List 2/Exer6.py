ganhoHora = float(input('Digite o valor q ganha por hora: '))

horaMes = float(input('Digite o valor de horas trabalhadas por mês: ')) 


salarioBruto = ganhoHora * horaMes
salarioLiquido = salarioBruto - (salarioBruto * 0.11) - (salarioBruto*0.08) - (salarioBruto*0.05) 

print('Seu salário é: %0.2f' %salarioLiquido)