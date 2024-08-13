mystring ='hello'


mylist = []
for letter in mystring:
    mylist.append(letter)
    print(letter)

print('\n')

print('Outra maneira de fazer:')

mylist = [letter for letter in mystring]
print(mylist)

mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [num for num in range(0,11) if num% 2==0]
print(mylist)