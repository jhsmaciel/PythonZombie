paisA = 80000
paisB = 200000
ano = 0
while paisA < paisB:
    ano += 1
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
print("%d anos"%ano)
