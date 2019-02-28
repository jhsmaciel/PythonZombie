numberUm = float(input('Digite o primeiro valor: '))
numberDois = float(input('Digite o segundo valor: '))
numberTres = float(input('Digite o terceiro valor: '))

if numberUm <= numberDois and numberUm <= numberTres:
    print ('O número menor é: %.2f' %numberUm)
elif numberDois <= numberUm and numberDois <= numberTres:
    print ('O número menor é: %.2f' %numberDois)
elif numberTres <= numberUm and numberTres <= numberDois:
    print ('O número menor é: %.2f' %numberTres)
