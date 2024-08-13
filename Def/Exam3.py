def verifica_numero(numero, limite):
    for i in range(limite + 1):
        if i == numero:
            return True
    return False

numero_verificar = int(input("Digite o número a ser verificado: "))
limite = int(input("Digite o limite da sequência: "))

if verifica_numero(numero_verificar, limite):
    print(f"O número {numero_verificar} está na sequência.")
else:
    print(f"O número {numero_verificar} não está na sequência.")