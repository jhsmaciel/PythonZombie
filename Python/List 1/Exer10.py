quantidadeCigarros = int(input('Informe a quantidade de cigarros que fuma por dia ou fumava: '))

quantidadeAnos = int(input('Informe por quantos anos você fuma ou fumou cigarro: '))

diasTotal = quantidadeAnos * 365

cigarrosTotal = diasTotal * quantidadeCigarros

tempoPerdido = cigarrosTotal * 10

diasPerdidos = tempoPerdido/(60*24)

print('Você perdeu %.1f dias da sua vida' %diasPerdidos)
print('Você fumou %d cigarros na sua vida' %cigarrosTotal)
