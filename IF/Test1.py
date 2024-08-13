#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0           A
#Entre 7.5 e 9.0            B
#Entre 6.0 e 7.5            C
#Entre 4.0 e 6.0            D
#Entre 4.0 e zero           E
#O algoritmo deve mostrar na tela as notas,
#a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
#ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("digite nota 1"))
nota2 = float(input("digite nota 2"))

media = (nota1 + nota2) / 2

if media >= 9.0 and media == 10.0:
    print("media:",media, "Aluno aprovado")
elif media >= 7.5 and media == 8.9:
    print("media:",media, "Aluno aprovado")

elif media >= 6.0 and media == 7.4:
    print("media:", media, "Aluno aprovado")

elif media >= 4.0 or media == 5.9:
    print("media:", media, "Aluno aprovado")
else:
    if media <= 3.99:
        print("media:",media,"Aluno reprovado")