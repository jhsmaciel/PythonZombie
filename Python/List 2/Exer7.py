metrosQuad = float(input('Digite a área da parede: '))

litros = int(metrosQuad / 3)
qtdLatas = 0

if(litros % 18 != 0):
    restLitro = litros % 18
    litros = litros - restLitro
    litros += 18
    
qtdLatas = (litros / 18) + qtdLatas
print('Comprar %d latas'%qtdLatas)
print('Custará R$%.2f'%(qtdLatas*80))