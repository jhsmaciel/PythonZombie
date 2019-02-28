dias  =   int(input('Digite o valor de dias: '))
horas  =   int(input('Digite o valor de horas: '))
minutos  =   int(input('Digite o valor de minutos: '))
segundos  =   int(input('Digite o valor de segundos: '))

segundosTotal = (segundos+(minutos*60)+(horas*(60*60))+(dias*(60*60*24)))

print(segundosTotal)