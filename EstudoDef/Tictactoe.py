def verificar_vencedor(lista_jogo):
    linhas = [lista_jogo[i:i+3] for i in range(0, 9, 3)]
    colunas = [lista_jogo[i::3] for i in range(3)]
    diagonais = [[lista_jogo[0], lista_jogo[4], lista_jogo[8]], [lista_jogo[2], lista_jogo[4], lista_jogo[6]]]

    sequencias = linhas + colunas + diagonais

    for sequencia in sequencias:
        if len(set(sequencia)) == 1 and sequencia[0] != ' ':
            return True
    return False

def mostrar_jogo(lista_jogo):
    for i in range(0, 9, 3):
        print(" | ".join(map(str, lista_jogo[i:i+3])))
        if i < 6:
            print("---------")

def escolha_posicao():
    escolha = input("Escolha uma posição (0-8): ")
    while not escolha.isdigit() or int(escolha) not in range(9):
        escolha = input("Escolha inválida. Escolha uma posição (0-8): ")
    return int(escolha)

def substituir(lista_jogo, posicao, jogador):
    if lista_jogo[posicao] == ' ':
        lista_jogo[posicao] = jogador
        return lista_jogo, True  # Retorna a lista alterada e True indicando sucesso
    else:
        print("Posição já ocupada. Escolha outra posição.")
        return lista_jogo, False  # Retorna a lista sem alterações e False indicando falha

def main():
    lista_jogo = [' ' for _ in range(9)]
    jogadores = ['X', 'O']
    
    while True:
        turno = 0
        while True:
            mostrar_jogo(lista_jogo)
            jogador = jogadores[turno % 2]
            posicao = escolha_posicao()
            lista_jogo, sucesso = substituir(lista_jogo, posicao, jogador)
            if sucesso:
                if verificar_vencedor(lista_jogo):
                    print(f"O jogador {jogador} venceu!")
                    break
                if ' ' not in lista_jogo:
                    print("Empate!")
                    break
                turno += 1
        
        if not escolha_continuar():
            break
        lista_jogo = [' ' for _ in range(9)]

if __name__ == "__main__":
    main()