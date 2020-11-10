from time import sleep


def func_Calculando(areaEncontrada):
    sleep(1)
    print('Calculando', end='')
    for ponto in range(3):
        print('.', end='')
        sleep(0.75)
    print(f'\nO resultado encontrado foi: {areaEncontrada}')
    sleep(2)
