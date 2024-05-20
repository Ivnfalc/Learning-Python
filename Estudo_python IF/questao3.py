#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo =input("digite F para feminino e M para masculino:")

if sexo == "f":
    print("sexo Feminino digitado")
elif sexo == "m":
    print("sexo digitado e masculino")
else:
    print("entrada invalida digite novamente")