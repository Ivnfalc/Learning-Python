#Faça um Programa que verifique se uma letra digitada é vogal ou consoante
ltr = input("digite uma letra:")
letras = ["a", "e", "i", "o", "u", "A", "E", "I", "O"]
if ltr not in letras:
    print("consoante")
else:
    print("vogal")