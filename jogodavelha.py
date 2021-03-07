def verifica():
    '''Verifica a vitória ou empate do jogador.'''
    #Condições de vitória
    global vitória
    global empate
    #Condições nas diagonais
    if matrix[0][0] == player1 and matrix[1][1] == player1 and matrix[2][2] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[0][0] == player2 and matrix[1][1] == player2 and matrix[2][2] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    if matrix[0][2] == player1 and matrix[1][1] == player1 and matrix[2][0] == player1:
        print("Jogador 1 venceu!")
        vitória = True
    elif matrix[0][2] == player2 and matrix[1][1] == player2 and matrix[2][0] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    #Condições de cima pra baixo
    if matrix[0][1] == player1 and matrix[1][1] == player1 and matrix[2][1] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[0][1] == player2 and matrix[1][1] == player2 and matrix[2][1] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    if matrix[0][0] == player1 and matrix[1][0] == player1 and matrix[2][0] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[0][0] == player2 and matrix[1][0] == player2 and matrix[2][0] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    if matrix[0][2] == player1 and matrix[1][2] == player1 and matrix[2][2] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[0][2] == player2 and matrix[1][2] == player2 and matrix[2][2] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    #condições na horizontal
    if matrix[0][0] == player1 and matrix[0][1] == player1 and matrix[0][2] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[0][0] == player2 and matrix[0][1] == player2 and matrix[0][2] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    if matrix[1][0] == player1 and matrix[1][1] == player1 and matrix[1][2] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[1][0] == player2 and matrix[1][1] == player2 and matrix[1][2] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    if matrix[2][0] == player1 and matrix[2][1] == player1 and matrix[2][2] == player1:
        print('Jogador 1 venceu!')
        vitória = True
    elif matrix[2][0] == player2 and matrix[2][1] == player2 and matrix[2][2] == player2:
        print('Jogador 2 venceu!')
        vitória = True
    #empate
    if vitória == False:
        empate = True
        for linha in range(0,3):
            for coluna in range(0,3):
                if type(matrix[linha][coluna]) == int:
                    empate = False


digitados = list()
vitória = False
matrix = [[1,2,3],[4,5,6],[7,8,9]]
esc = 0
player1 = str(input('Escolha um: [O/X]')).strip().upper()[0]
while player1 != 'O' and player1 != 'X':
    player1 = str(input('Escolha um: [O/X]')).strip().upper()[0]
if player1 == "X": 
    player2 = "O"
elif player1 == "O":
    player2 = 'X'
jogar = str(input('Deseja jogar contra quem? [Amigo/PC]')).strip().upper()[0]
while jogar != 'A' and jogar != 'P':
    jogar = str(input('Deseja jogar contra quem? [Amigo/PC]')).strip().upper()[0]
vez = 2
if jogar == "A":
    while True:
        for linha in range(0,3):
            if linha != 0:
                print('--+---+---')
            else: 
                print()
            for coluna in range(0,3):
                if coluna <= 1:
                    print(matrix[linha][coluna], end = ' | ')
                else:
                    print(matrix[linha][coluna])
        print()
        esc = int(input('Escolha uma posição: '))
        while esc in digitados:
            esc = int(input('Escolha uma posição: '))
        digitados.append(esc)
        if vez % 2 == 0:
            for pos, num in enumerate(matrix):
                for p, valor in enumerate(num):
                    if valor == esc:
                        matrix[pos][p] = player1
        elif vez % 2 == 1: 
            for pos, num in enumerate(matrix):
                for p, valor in enumerate(num):
                    if valor == esc:
                        matrix[pos][p] = player2   
        verifica()
        if empate == True:
            break    
        if vitória == True:
            print('Posição final: ')
            for linha in range(0,3):
                if linha != 0:
                    print('--+---+---')
                else:
                    print()
                for coluna in range(0,3):
                    if coluna <= 1:
                        print(matrix[linha][coluna], end = ' | ')
                    else:
                        print(matrix[linha][coluna])
            break
        vez += 1
elif jogar == 'P':
    from random import randint
    while True:
        if vez % 2 == 0:
            for linha in range(0,3):
                if linha != 0:
                    print('--+---+---')
                else: 
                    print()
                for coluna in range(0,3):
                    if coluna <= 1:
                        print(matrix[linha][coluna], end = ' | ')
                    else:
                        print(matrix[linha][coluna])
        print()
        if vez % 2 == 0:
            esc = int(input('Escolha uma posição: '))
            while esc in digitados:
                esc = int(input('Escolha uma posição: '))
            digitados.append(esc)
            for linha in range(0,3):
                for coluna in range(0,3):
                    if esc == matrix[linha][coluna]:
                        matrix[linha][coluna] = player1
        elif vez % 2 == 1:
            esc = randint(1,9)
            while esc in digitados:
                esc = randint(1,9)
            digitados.append(esc)
            for linha in range(0,3):
                for coluna in range(0,3):
                    if esc == matrix[linha][coluna]:
                        matrix[linha][coluna] = player2
        verifica()
        if empate == True:
            print('Posição final: ')
            for linha in range(0,3):
                if linha != 0:
                    print('--+---+---')
                else: 
                    print()
                for coluna in range(0,3):
                    if coluna <= 1:
                        print(matrix[linha][coluna], end = ' | ')
                    else:
                        print(matrix[linha][coluna])
            break        
        if vitória == True:
            print('Posição final: ')
            for linha in range(0,3):
                if linha != 0:
                    print('--+---+---')
                else: 
                    print()
                for coluna in range(0,3):
                    if coluna <= 1:
                        print(matrix[linha][coluna], end = ' | ')
                    else:
                        print(matrix[linha][coluna])
            break
        vez += 1
print('\nGame over, obrigado por jogar!')
