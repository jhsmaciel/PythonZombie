distancia  =   float(input('Digite distância do local em km: '))

velMedia =   float(input('Digite a velocidade média em km/h: '))

metrosSegundo = velMedia/3.6

distanciaMetros = distancia*1000

tempoEmSegundos = distanciaMetros/metrosSegundo
dia     = int (tempoEmSegundos/(24*60*60))
tempoEmSegundos = tempoEmSegundos - dia*(24*60*60)
hora    = int(tempoEmSegundos/(60*60))
tempoEmSegundos = tempoEmSegundos - hora*(60*60)
minutos    = int(tempoEmSegundos/60)

print (dia,' dias, ',hora,' horas e ',minutos,' minutos.')