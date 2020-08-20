from time import sleep


def entrada():
    print('==='*15)
    print(f'{"Bem vindo ao Chute um Número!"!s:^45s}')
    print('==='*15)
    sleep(1)


def saida():
    sleep(0.25)
    print('==='*15)
    print(f'{"Muito bem. Te vejo mais tarde!"!s:^45s}')
    print('==='*15)


def form(text=''):
    print(f'{text!s:^40s}')
