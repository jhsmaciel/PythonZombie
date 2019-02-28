numberUm = float(input('Digite o primeiro valor: '))
numberDois = float(input('Digite o segundo valor: '))
numberTres = float(input('Digite o terceiro valor: '))

if numberUm >= numberDois and numberUm >= numberTres:
    print ('O número maior é: %.2f' %numberUm)
if numberDois >= numberUm and numberDois >= numberTres:
    print ('O número maior é: %.2f' %numberDois)
if numberTres >= numberUm and numberTres >= numberDois:
    print ('O número maior é: %.2f' %numberTres)
