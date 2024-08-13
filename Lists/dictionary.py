preço = {'madeira':30.99, 'cadeira':50.00, 'mesa':200.00, 'piso':25.00} #exemplo de dicionario,
#onde armazena nome + preço.
print(preço[input("digite o item:")])# aqui o usuario digita o que deseja pesquisar e retorna o preço.
#o dicionario comporta tambem listas e dicionario, como o exemplo abaixo
d = {'key1': {'numero1': 1}, 'key2': [0,1,2]}
#para chamar o item da lista dentro  do dicionario, o mesmo funciona pra dicionario dentro de dicionario:
print(d['key2'] [1:])
