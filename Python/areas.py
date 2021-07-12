from time import sleep
import area_func1 as af

print('Bem-vindx ao calculador de áreas')
sleep(0.5)
while True:
    af.menu()
    sleep(1)

    try:
        escolha = af.escolha_figura()
        sleep(0.5)

    except (TypeError, SyntaxError, ValueError):
        print('Digite novamente.')
        sleep(0.5)

    else:
        # Triâgulo
        if escolha == 1:
            areaT = af.triangulo()
            af.func_Calculando(areaT)

        # Quadrado
        if escolha == 2:
            areaQ = af.quadrado()
            af.func_Calculando(areaQ)

        # Círculo
        if escolha == 3:
            af.circulo()

        # Losango
        if escolha == 4:
            areaL = af.losango()
            af.func_Calculando(areaL)

        # Trapézio
        if escolha == 5:
            areaTrap = af.trapezio()
            af.func_Calculando(areaTrap)

        # Cubo
        if escolha == 6:
            areaCubo = af.cubo()
            af.func_Calculando(areaCubo)

        # Esfera
        if escolha == 7:
            af.esfera()

        # Sair
        if escolha == 0:
            af.func_tchau()
            break
