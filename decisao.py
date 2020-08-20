from random import choice
from time import sleep

print('Bem-Vindo ao Decida por Mim!\n')

decisoes = ['Sim, com certeza.', 'Será?', 'Talvez hoje não.',
            'E se você não fizer isso?', 'Ah... sei lá!',
            'Claro, o que pode dar de errado?', 'Óbvio!',
            'Você nunca mais deveria fazer isso.', 'Você tá louco?',
            'Siga o seu coração!', 'Se jogue!', 'Sim, mas mais tarde.']

sleep(1)
pergunta = str(input('Pergunta:'))
sleep(0.5)
resposta = choice(decisoes)
print(f'Resposta: {resposta}')
sleep(0.5)
print('\nDeseja fazer mais perguntas?')
while True:
    try:
        esc = int(input('[1 - Sim / 2 - Não]:'))
    except (ValueError, TypeError):
        print('Não entendi, poderia escolher de novo?')
    else:
        if esc == 1:
            sleep(0.5)
            pergunta = str(input('Pergunta:'))
            sleep(0.5)
            resposta = choice(decisoes)
            print(f'Resposta: {resposta}')
            sleep(0.5)
            print('\nDeseja fazer mais perguntas?')
        if esc == 2:
            sleep(0.5)
            print('Obrigado por perguntar!')
            sleep(1)
            break
