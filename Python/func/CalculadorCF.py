from time import sleep

def func_Calculando(areaEncontrada):
    sleep(0.25)
    print('Calculando', end='')
    for ponto in range(3):
        print('.', end='')
        sleep(0.5)
    print(f'\nA área encontrada foi: {areaEncontrada}')
    sleep(1)

def escolha_figura():
    escolha = int(input('Escolha: '))
    if (escolha > 7) or (escolha < 0):
        print('Digite novamente.')
    else:
        return escolha

def triangulo():
    base = float(input('Base:'))
    altura = float(input('Altura:'))
    areaT = (base * altura) / 2
    return areaT

def quadrado():
    lado = float(input('Lado:'))
    if lado <= 0:
        print('Digite o lado novamente',
              'O lado de um quadrado não pode ser zero ou negativo.')
    else:
        areaQ = (lado * lado)
        return areaQ

def circulo():
    raio = float(input('Raio:'))
    print('Deseja arredondar pi (3,14) para 3?')
    pi_conversao = str(input('[S / N]: ')).strip()[0]
    if pi_conversao in 'Ss':
        areaC1 = 3 * (raio * raio)
        return func_Calculando(areaC1)
    if pi_conversao in 'Nn':
        areaC2 = 3.14 * (raio ** 2)
        return func_Calculando(areaC2)
    if pi_conversao not in 'SsNn':
        print('Escolha novamente')

def losango():
    Dzao = float(input('Digite o valor da diagonal maior: '))
    Dzinho = float(input('Digite o valor da diagonal menor: '))
    areaL = (Dzao * Dzinho) / 2
    return areaL

def trapezio():
    Bzao = float(input('Digite o valor da base maior: '))
    Bzinho = float(input('Digite o valor da base menor: '))
    altura = float(input('Digite o valor da altura: '))
    areaTrap = ((Bzao + Bzinho) * altura) / 2
    return areaTrap

def cubo():
    lado = float(input('Lado:'))
    areaCubo = (lado * lado) * 6
    return areaCubo

def esfera():
    raio = float(input('Raio:'))
    print('Deseja arredondar pi (3,14) para 3?')
    pi_conversao = str(input('[S / N]: ')).strip()[0]
    if pi_conversao in 'Ss':
        areaEsf1 = 4 * 3 * (raio ** 2)
        return func_Calculando(areaEsf1)
    if pi_conversao in 'Nn':
        areaEsf2 = 4 * 3.14 * (raio ** 2)
        return func_Calculando(areaEsf2)
    if pi_conversao not in 'SsNn':
        print('Escolha novamente')

def func_tchau():
    print('Até mais! Obrigado por usar o calculador.')
    sleep(1)

def menu():
    print('Qual área deseja calcular:',
          '\n1 - Triângulo qualquer',
          '\n2 - Quadrado',
          '\n3 - Círculo',
          '\n4 - Losango',
          '\n5 - Trapézio',
          '\n6 - Cubo',
          '\n7 - Esfera',
          '\n0 - Sair do calculador')
