m1 = [[0, 1, 1], [1, 0, 1]]
m2 = [[0, 1, 1], [1, 0, 1]]

def matriz_igual(matriz1, matriz2):
    cond1 = True
    cond2 = True
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            if matriz1[i][j] != matriz2[i][j]:
                cond1 = False
            elif matriz1[i][j] != 1 and matriz1[i][j] != 0:
                cond2 = False
    if cond1 is True and cond2 is True:
        print('Você possui a matriz identidade intergalática!')
    else:
        print('Você não possui a matriz identidade intergalática :(')


matriz_igual(m1, m2)