cartas = []


def maior(vetor):
    valor = 1
    while valor >= 0:
        valor = int(input('Digite o valor da carta: '))
        cartas.append(valor)

    print(f'A carta mais valiosa desse vetor é {max(vetor)}')


maior(cartas)
