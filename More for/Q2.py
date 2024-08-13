#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = input("Nome do Usuario:")
    senha = input("Senha:")
    if user == senha:
        print("error")
        continue
    else:
        break