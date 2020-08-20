import corpo as en
from random import randint
from time import sleep

en.entrada()
sleep(1)
en.form('\n=Para desistir digite -1 em seu chute=')
sleep(1)
comp = randint(1, 100)
en.form('\nO computador já escolheu! Agora é a sua vez.')
sleep(0.5)
while True:
    try:
        pessoa = int(input('Chute um número inteiro entre 1 e 100: '))
    except (ValueError, TypeError):
        sleep(0.5)
        en.form('Erro! Digite seu chute novamente.')
    else:
        sleep(0.5)
        if pessoa == comp:
            en.form('Você acertou!')
            sleep(0.5)
            break
        if pessoa > comp:
            en.form('Chute um valor mais baixo!')
        if -1 < pessoa < comp:
            en.form('Chute um valor mais alto!')
        if pessoa == -1:
            en.form('Ah que pena...')
            break
en.saida()
