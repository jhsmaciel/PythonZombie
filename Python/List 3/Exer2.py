nome = input("Digite o nome de usuário: ")
senha = input("Digite a sua senha: ")
x = -1
while x != 0:
    if nome == senha:
        print("Usuário e senha não podem ser iguais!")
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a sua senha: ")
    else:
        x = 0
print("Usuário e senha estão aceitos!")

    