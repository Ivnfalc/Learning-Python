#estudo sobre funçao def

#def add_num(num1,num2):
    #return num1+num2 #funciona para que seja retornado os valores

"""
o return permite salvar como variavel 
exemplo:se a entrada do usuario for add_num(10,20)
o resdultado vai ser 30.
Tambem pode ser feitocomo variavel : "soma = add_num (10,20)" o resultado vai ser o mesmo
porem agora tera uma variavel adicionada apenas chamando a variavel soma.
funçao sempre deve ser snake casing, ou seja
deve ser lowcase com Underline, nao deve ter espaços
"""
"""
def my_function(pnome):
      print(pnome + " Alcantara")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
""" 

def newf(name):
      print("Ola,"+ name + " boa tarde")

newf("ivan")

#exemplo de return com if:

def valor(num):
      

    if num >= 0:
         return num
    else:
         return -num

print (valor (2))
print (valor(-4))