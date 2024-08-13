with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
test = open("test.txt")
print(test.read())#para ler
print(test.readlines())#para ler em uma linha so
test = open("insere o caminho no arquivo para abrir")
test = test.close()
#exemplo de como criar um arquivo txt