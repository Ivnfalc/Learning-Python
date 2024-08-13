mylist = ["one","two"]
mylist2 = ["three", "four"]

newlist = mylist + mylist2 #merging listas
print(newlist)

#substituindo
newlist [0] = 'NONE'
print (newlist)

#adicionando no final da lista
newlist.append("FIVE")
print(newlist)
#removendo itens do fina da lista
newlist.pop() #pode ser colocado a posiçao de qual item deseja retirar
print(newlist)

nlist = ["a", "x", "c", "h", "j","b" ,"d"]
numlist = [9,7,4,2,1,5,3,8]
#organizando  a lista:
nlist.sort()
numlist.sort()
print(nlist)
print(numlist)
#tambem pode ser usado da seguinte maneira:
#nlist.sort()
#sortedlist = nlist
#print(sortedlist)
#>>> revertendo
numlist.reverse()
print(numlist)