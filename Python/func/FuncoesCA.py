from time import sleep


def Calculando(area):
    sleep(0.25)
    print('Calculando', end='')
    for ponto in range(3):
        print('.', end='')
        sleep(0.5)
    print(f'\nA área encontrada foi: {area}')
    sleep(1)


def Tchau():
    print('Até mais! Obrigado por usar o calculador.')
    sleep(1)


def Menu():
    print('Qual área deseja calcular:',
          '\n1 - Triângulo qualquer',
          '\n2 - Quadrado',
          '\n3 - Círculo',
          '\n4 - Losango',
          '\n5 - Trapézio',
          '\n6 - Cubo',
          '\n7 - Esfera',
          '\n0 - Sair do calculador')
