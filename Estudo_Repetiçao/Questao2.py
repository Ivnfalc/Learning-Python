#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user == input("usuario:")
    senha == input("senha:")
    if user == senha:
        print("Usuario nao deve ser identico à senha, digite novamente:")
        continue
    else:
        break