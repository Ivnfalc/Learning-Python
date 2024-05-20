#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input("digite o numero em que a sequencia deve parar:"))
fib1= 1
fib2= 1
count = 0
list = [0,1,1]

for x in range (0,n):
  count = fib1 + fib2
  fib1 = count
  fib2 = (count - fib2)
  list.append(count)
print("fibonacci",list)