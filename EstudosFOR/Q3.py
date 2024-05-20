#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


while True:
    nome = input("digite seu nome:")
    idade = int(input("digite a idade:"))
    salario = int(input("digite salario:"))
    sexo = str(input("Sexo m ou f?"))
    estado = input("Estado Civil: 's', 'c', 'v', 'd'?:")
    if idade <= 150:
        print("idade: ", idade)
    else:
        print("idade invalida")
        break
    if salario > 0 :
        print("salario:",salario)
    else:
        print("salario digitado e menor que o esperado,digite novamente")
        break
    if sexo == "m" or sexo == "f":
        print("sexo:",sexo )
    else:
        print("sexo invalido")
        break
    if estado == "s" or"c" or "v" or "d":
        print("estado:",estado)
