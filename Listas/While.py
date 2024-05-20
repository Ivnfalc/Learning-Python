num = 0
x = [1,2,3]
y = 'hello'
z = 'world'
while num <= 5:
    print(f'numero atual:{num}')
    num += 1
print('\n')

#usando pass;
for item in x:
    #comentario
    pass # o pass é um paceholder , para que seu codigo nao de erro , pois nao existe nada apos o for
            #o python sendo idented like, iria dar erro se nao tivesse nada apos o for.

#usando continue,vai para o topo do loop
print('usando continue:')
for letra in y:
    if letra == 'e':
        continue
    print(letra) #basicamente ele irá pular a letra ou  objeto escolhido.
print('\n')
#usando break:
print('usando break:')
for let in z:
    if let == 'o':
        break
    print(let) #aqui ele vai  parar quando a letra for 'o' e isso para o loop.
