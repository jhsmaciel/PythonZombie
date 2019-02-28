ladoUm = float(input('Digite o valor do primeiro lado:'))
ladoDois = float(input('Digite o valor do segundo lado:'))
ladoTres = float(input('Digite o valor do terceiro lado:'))

if ladoUm == ladoDois and ladoDois == ladoTres:
    print ('Triângulo Equilátero')
elif ladoUm == ladoDois or ladoDois == ladoTres or ladoUm == ladoTres:
    print ('Triângulo Isósceles')
elif ladoUm != ladoDois and ladoDois != ladoTres or ladoUm != ladoTres:
    print ('Triângulo Escaleno')