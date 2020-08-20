from random import randint
from time import sleep

print(
    '==='*10,
    '\n{:^30}'.format('Bem-Vindx ao Dado Virtual!')
)

print(
    '==='*10,
    '\n{:^30}'.format('Gostaria de jogar?')
)
while True:
    sleep(1)
    try:
        esc = int(input('  [1- SIM / 2 - NÃO]:'))
    except (ValueError, TypeError):
        print('\n  Desculpe, não entendi.')
    else:
        sleep(0.25)
        if esc == 1:
            print('\n  Então vamos lá!')
            num = randint(1, 6)
            sleep(0.75)
            print('  SORTEANDO...')
            sleep(1)
            print(f'  O número sorteado foi: {num}')
            sleep(0.75)
            print('\n  Gostaria de ir novamente?')
        if esc == 2:
            print('\n  Ok! Te vejo mais tarde.')
            sleep(1.25)
            break
