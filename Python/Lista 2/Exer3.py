kiloPeixe = int(input('Digite o peso em kilos, do total de peixes: '))
excesso = 0
multa = 0

if kiloPeixe > 50:
    excesso = kiloPeixe - 50
    multa = excesso * 4

print ('Excesso de ',excesso,'kilos,  R$',multa,'de multa')