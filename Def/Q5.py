#Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. 
#  função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    return (0.01 *taxaImposto)*custo + custo

somaImposto(10,45.00)
print(somaImposto(10,45.00))