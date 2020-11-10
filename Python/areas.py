from time import sleep
from area_func import func_Calculando

print('Bem-vindx ao calculador de áreas')
sleep(1)
while True:
    print('Qual área deseja calcular:',
          '\n1 - Triângulo qualquer',
          '\n2 - Quadrado',
          '\n3 - Círculo',
          '\n4 - Losango',
          '\n5 - Trapézio',
          '\n6 - Cubo',
          '\n7 - Esfera',
          '\n0 - Sair do calculador')
    sleep(1)
    try:
        escolha = int(input('Escolha: '))
        if (escolha > 7) or (escolha < 0):
            print('Digite novamente.')
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
            func_Calculando(areaT)
        # Quadrado
        if escolha == 2:
            lado = float(input('Lado:'))
            if lado <= 0:
                print('Digite o lado novamente',
                      'O lado de um quadrado não pode ser zero ou negativo.')
            else:
                areaQ = (lado * lado)
                func_Calculando(areaQ)
        # Círculo
        if escolha == 3:
            raio = float(input('Raio:'))
            print('Deseja arredondar pi (3,14) para 3?')
            pi_conversao = str(input('[S / N]: ')).strip()[0]
            if pi_conversao in 'Ss':
                areaC1 = 3 * (raio * raio)
                func_Calculando(areaC1)
            if pi_conversao in 'Nn':
                areaC2 = 3.14 * (raio ** 2)
                func_Calculando(areaC2)
            if pi_conversao not in 'SsNn':
                print('Escolha novamente')
        # Losango
        if escolha == 4:
            Dzao = float(input('Digite o valor da diagonal maior: '))
            Dzinho = float(input('Digite o valor da diagonal menor: '))
            areaLosango = (Dzao * Dzinho) / 2
            func_Calculando(areaLosango)
        # Trapézio
        if escolha == 5:
            Bzao = float(input('Digite o valor da base maior: '))
            Bzinho = float(input('Digite o valor da base menor: '))
            altura = float(input('Digite o valor da altura: '))
            areaTrap = ((Bzao + Bzinho) * altura) / 2
            func_Calculando(areaTrap)
        # Cubo
        if escolha == 6:
            lado = float(input('Lado:'))
            areaCubo = (lado * lado) * 6
            func_Calculando(areaCubo)
        # Esfera
        if escolha == 7:
            raio = float(input('Raio:'))
            print('Deseja arredondar pi (3,14) para 3?')
            pi_conversao = str(input('[S / N]: ')).strip()[0]
            if pi_conversao in 'Ss':
                areaEsf1 = 4 * 3 * (raio ** 2)
                func_Calculando(areaEsf1)
            if pi_conversao in 'Nn':
                areaEsf2 = 4 * 3.14 * (raio ** 2)
                func_Calculando(areaEsf2)
            if pi_conversao not in 'SsNn':
                print('Escolha novamente')
        # Sair
        if escolha == 0:
            print('Até mais! Obrigado por usar o calculador.')
            sleep(1)
            break
