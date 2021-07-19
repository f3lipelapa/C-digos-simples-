from time import sleep
import ClassesCA as ca
import FuncoesCA as fa

print('Bem-vindx ao calculador de áreas')
sleep(0.5)
while True:
    fa.Menu()
    sleep(1)

    try:
        escolha = int(input('Escolha: '))
        if (escolha > 7) or (escolha < 0):
            print('Digite novamente.')

    except (TypeError, SyntaxError, ValueError):
        print('Digite novamente.')
        sleep(0.5)

    else:
        # Triâgulo
        if escolha == 1:
            base = float(input('Base:'))
            altura = float(input('Altura:'))
            triangulo = ca.FiguraPlana(base=base, altura=altura)
            area = triangulo.Triangulo()
            fa.Calculando(area)

        if escolha == 2:
            lado = float(input('Lado:'))
            if lado <= 0:
                print('Digite o lado novamente',
                      'O lado de um quadrado não pode ser zero ou negativo.')
            else:
                quadrado = ca.FiguraPlana(base=lado)
                area = quadrado.Quadrado()
                fa.Calculando(area)

        # Círculo
        if escolha == 3:
            raio = float(input('Raio:'))
            circulo = ca.FiguraPlana(raio=raio)
            area = circulo.Circulo(pi=3.14)
            fa.Calculando(area)

        # Losango
        if escolha == 4:
            Dzao = float(input('Digite o valor da diagonal maior: '))
            Dzinho = float(input('Digite o valor da diagonal menor: '))
            trapezio = ca.FiguraPlana(Dzao=Dzao, Dzinho=Dzinho)
            area = trapezio.Losango()
            fa.Calculando(area)

        # Trapézio
        if escolha == 5:
            Bzao = float(input('Digite o valor da base maior: '))
            Bzinho = float(input('Digite o valor da base menor: '))
            altura = float(input('Digite o valor da altura: '))
            trapezio = ca.FiguraPlana(Bzao=Bzao, Bzinho=Bzinho, altura=altura)
            area = trapezio.Trapezio()
            fa.Calculando(area)

        # Cubo
        if escolha == 6:
            lado = float(input('Lado:'))
            cubo = ca.FiguraEspacial(base=lado)
            area = cubo.Cubo()
            fa.Calculando(area)

        # Esfera
        if escolha == 7:
            raio = float(input('Raio:'))
            esfera = ca.FiguraEspacial(raio=raio)
            area = esfera.Esfera(pi=3.14)
            fa.Calculando(area)

        # Sair
        if escolha == 0:
            fa.Tchau()
            break
