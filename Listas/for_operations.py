word = 'abcde'

for num in range(10):
    print(num)#aqui o loop ira mostrar numeros de 0 a ate menor que o numero do in range()

print('\n')
for num2 in range(0,10,2):
    print(num2)
#aqui ele ira fazer o loop mostrar os numeros de 0 ate 9,
# porem o auxiliar 2 ira fazzer com que moster numeros pares.
print('\n')

#index counter automatico:
for item in enumerate(word):
    print(item)