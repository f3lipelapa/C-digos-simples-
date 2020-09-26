from time import sleep

print('Bem-vindx ao calculador de áreas')
sleep(1)
while True:
    print('Qual área deseja calcular:',
          '\n1 - Trângulo',
          '\n2 - Quadrado',
          '\n3 - Círculo',
          '\n4 - Cubo',
          '\n0 - Sair do calculador')
    sleep(1)
    try:
        escolha = int(input('Escolha: '))
        sleep(1)
    except (TypeError, SyntaxError, ValueError):
        print('Digite novamente.')
        sleep(1)
    else:
        # Triâgulo
        if escolha == 1:
            base = float(input('Base:'))
            altura = float(input('Altura:'))
            areaT = (base * altura) / 2
            sleep(1)
            print('Claculando', end='')
            for ponto in range(3):
                print('.', end='')
                sleep(0.75)
            print(f'\nO resultado encontrado foi: {areaT}')
            sleep(2)
        # Quadrado
        if escolha == 2:
            lado = float(input('Lado:'))
            if lado <= 0:
                print('Digite o lado novamente',
                      'O lado de um quadrado não pode ser zero ou negativo.')
            else:
                areaQ = (lado * lado)
                sleep(1)
                print('Claculando', end='')
                for ponto in range(3):
                    print('.', end='')
                    sleep(0.75)
                print(f'\nO resultado encontrado foi: {areaQ}')
                sleep(2)
        # Círculo
        if escolha == 3:
            raio = float(input('Raio:'))
            print('Deseja arredondar pi (3,14) para 3?')
            pi_conversao = str(input('[S / N]: ')).strip()[0]
            if pi_conversao in 'Ss':
                areaC1 = 3 * (raio * raio)
                sleep(1)
                print('Claculando', end='')
                for ponto in range(3):
                    print('.', end='')
                    sleep(0.75)
                print(f'\nO resultado encontrado foi: {areaC1}')
                sleep(2)
            if pi_conversao in 'Nn':
                areaC2 = 3.14 * (raio ** 2)
                sleep(1)
                print('Claculando', end='')
                for ponto in range(3):
                    print('.', end='')
                    sleep(0.75)
                print(f'\nO resultado encontrado foi: {areaC2}')
                sleep(2)
            if pi_conversao not in 'SsNn':
                print('Escolha novamente')
        # Cubo
        if escolha == 4:
            lado = float(input('Lado:'))
            areaCubo = (lado * lado) * 6
            sleep(1)
            print('Claculando', end='')
            for ponto in range(3):
                print('.', end='')
                sleep(0.75)
            print(f'\nO resultado encontrado foi: {areaCubo}')
            sleep(2)
        # Sair
        if escolha == 0:
            print('Até mais! Obrigado por usar o calculador.')
            sleep(1)
            break
