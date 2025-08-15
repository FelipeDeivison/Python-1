import random
def valida_int (pergunta, min , max):
    x = int(input(pergunta))
    while ((x <min) or (x > max)):
        x = int(input(pergunta))
    return x



def vencedor (jogador1, jogador2):
    global v1 , v2 , empate
    if jogador1 == 1: #pedra
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2: #papel
            v2 += 1
        elif jogador2 == 3: #Tesoura
            v1 += 1
    if jogador1 == 2: 
        if jogador2 == 1:
            v1 += 1
        elif jogador2 == 2:
            empate += 1
        elif jogador2 == 3: #Tesoura
            v2 += 1
    if jogador1 == 3: 
        if jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
        elif jogador2 == 3: #Tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados
#Jogo Pedra, Papel e Tesoura
print("Escolha:\n 1 para Pedra\n 2 para Papel\n 3 para Tesoura")

#Programa principal

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int("Escolha sua jogada: ", 0 , 3)
    if not j1:
        break
    j2 = random.randint (1 , 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end = " ")
    print()

print(f"Resuldados do jogador 1: {resultados[0]}")
print(f"Resuldados do jogador 2: {resultados[1]}")
print(f"Empates: {resultados[2]}")