#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 120


while True:
    nome = input("digite nome:")
    if len(nome) <= 3:
        print("nome deve ser menor que 3 letras")
        continue
    else:
        break

while True:
    idade = int(input("digite idade:"))
    if idade > 120:
        print("nome deve ser entre 0 e 120")
        continue
    else:
        break
