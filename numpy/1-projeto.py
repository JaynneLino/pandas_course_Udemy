import numpy as np

# Mapa 5 x 5
mapa = np.random.randint(1, 10, size=(5, 5))

# Posiciona o tesouro em uma posição aleatória, mas não na posição (0, 0)
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

# Função para imprimir o mapa com a posição do jogador
def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1  # -1 será usado para marcar o jogador
    # Substitui o valor -1 pelo símbolo do jogador ('P') para o marcador visual
    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador)  # Converte a matriz para string
    mapa_com_jogador_str[mapa_com_jogador == '-1'] = 'P'  # Marca a posição do jogador com 'P'
    
    print("\nMapa Atual:")
    for linha in mapa_com_jogador_str:
        print(' '.join(linha))

# Ciclo principal
while True:
    mostrar_mapa(mapa, posicao_jogador)
    
    # Movimentação do jogador
    direcao = input("Informe a direção que deseja mover (cima, baixo, esquerda, direita): ").strip().lower()
    
    movimentos = {
        'cima': (-1, 0),
        'baixo': (1, 0),
        'esquerda': (0, -1),
        'direita': (0, 1),
        'c': (-1, 0),  # Alias para 'cima'
        'b': (1, 0),   # Alias para 'baixo'
        'e': (0, -1),  # Alias para 'esquerda'
        'd': (0, 1),   # Alias para 'direita'
    }
    
    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao][0], 
                        posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("Direção inválida! Tente novamente.")
        continue
    
    # Verifica se a nova posição é válida
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] 
            < mapa.shape[1]):
        print("Movimento fora dos limites! Tente novamente.")
        continue
    
    # Atualiza a posição do jogador
    posicao_jogador = nova_posicao
    pontuacao += 1
    
    # Verifica se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n ======= Parabéns! Você encontrou o tesouro! =======")
        print(f"Pontuação Final: {pontuacao}")
        print(f"O tesouro estava na posição {(tesouro_linha, tesouro_coluna)}")
        break
