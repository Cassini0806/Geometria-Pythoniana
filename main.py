import geometria

#círculo, triângulo, quadrado, retângulo, trapézio, paralelogramo, losango, pentágono, hexágono.

def classifica_forma_area(nome_forma: str):
    match nome_forma:
        case 'triangulo':
            altura = float(input("altura: "))
            base = float(input("base: "))
            area = geometria.area_triangulo(base, altura)
        case 'circulo':
            raio = float(input("raio: "))
            area = geometria.area_circulo(raio)
        case 'quadrado':
            lado = float(input("lado: "))
            area = geometria.area_paralelogramo(lado, lado)
        case 'retangulo':
            altura = float(input("altura: "))
            base = float(input("base: "))
            area = geometria.area_paralelogramo(base, altura)
        case 'paralelogramo':
            altura = float(input("altura: "))
            base = float(input("base: "))
            area = geometria.area_paralelogramo(base, altura)
        case 'trapezio':
            base_maior = float(input("base maior: "))
            base_menor = float(input("base menor: "))
            altura = float(input("altura: "))
            area = geometria.area_trapezio(base_maior, base_menor, altura)
        case 'losango':
            diagonal_maior = float(input("diagonal maior: "))
            diagonal_menor = float(input("diagonal menor: "))
            area = geometria.area_triangulo(diagonal_maior, diagonal_menor)
        case 'pentagono':
            lado = float(input("lado: "))
            area = geometria.area_pentagono(lado)
        case 'hexagono':
            lado = float(input("lado: "))
            area = geometria.area_hexagono(lado)
        case _:
            print("Forma não reconhecida, tente novamente.")
            print("Digite uma das seguintes formas para prosseguir: circulo, triangulo, quadrado, retangulo, trapezio, paralelogramo, losango, pentagono, hexagono.")
            area = classifica_forma_area(input("Forma geometrica: "))
    return area

def classifica_forma_perimetro(nome_forma: str):
    match nome_forma:
        case 'triangulo':
            lado_A = float(input("lado A: "))
            lado_B = float(input("lado B: "))
            lado_C = float(input("lado C: "))
            perimetro = geometria.perimetro_triangulo(lado_A, lado_B, lado_C)
        case 'circulo':
            raio = float(input("raio: "))
            perimetro = geometria.perimetro_circulo(raio)
        case 'quadrado':
            lado = float(input("lado: "))
            perimetro = geometria.perimetro_regular(lado, 4)
        case 'retangulo':
            altura = float(input("altura: "))
            base = float(input("base: "))
            perimetro = geometria.perimetro_paralelogramo(base, altura)
        case 'paralelogramo':
            altura = float(input("altura: "))
            base = float(input("base: "))
            perimetro = geometria.perimetro_paralelogramo(base, altura)
        case 'trapezio':
            base_maior = float(input("base maior: "))
            base_menor = float(input("base menor: "))
            l1 = float(input("lateral A: "))
            l2 = float(input("lateral B: "))
            perimetro = geometria.perimetro_trapezio(base_maior, base_menor, l1, l2)
        case 'losango':
            lado = float(input("lado: "))
            perimetro = geometria.perimetro_regular(lado, 4)
        case 'pentagono':
            lado = float(input("lado: "))
            perimetro = geometria.perimetro_regular(lado, 5)
        case 'hexagono':
            lado = float(input("lado: "))
            perimetro = geometria.perimetro_regular(lado, 6)
        case _:
            print("Forma não reconhecida, tente novamente.")
            print("Digite uma das seguintes formas para prosseguir: circulo, triangulo, quadrado, retangulo, trapezio, paralelogramo, losango, pentagono, hexagono.")
            classifica_forma_area(input("Forma geometrica: "))
    return perimetro

def classifica_tipo_calculo(tipo_calculo: str, nome_forma: str):
    if tipo_calculo == 'area':
        area = classifica_forma_area(nome_forma)
        texto_resultado = "A área é de " + str(area) + " unidades ao quadrado."
    elif tipo_calculo == 'apotema':
        match nome_forma:
            case 'triangulo':
                numero_lados = 3
            case 'quadrado':
                numero_lados = 4
            case 'pentagono':
                numero_lados = 5
            case 'hexagono':
                numero_lados = 6
            case _:
                return "Impossível calcular apotema desta forma."
        lados = float(input("tamanho do lado do polígono: "))
        apotema = geometria.apotema(lados, numero_lados)
        texto_resultado = "A apotema de um polígono de " + str(numero_lados) + " é de " + str(apotema) + " unidades ao quadrado."
    elif tipo_calculo == 'perimetro':
        perimetro = classifica_forma_perimetro(nome_forma)
        texto_resultado = "O perímetro é de " + str(perimetro) + " unidades."
    else:
        print("Comando não reconhecido, tente novamente.")
        classifica_tipo_calculo(input("O que você quer calcular?(area, apotema, perimetro): "), nome_forma)
    return texto_resultado
        
def main():
    print("Olá, este é um programa de calculos geometricos com Python.")
    print("Digite uma das seguintes formas para prosseguir: circulo, triangulo, quadrado, retangulo, trapezio, paralelogramo, losango, pentagono, hexagono.")
    nome_forma = input("Forma geometrica: ")
    tipo_calculo = input("O que você quer calcular?(area, apotema, perimetro): ")
    resultado = classifica_tipo_calculo(tipo_calculo, nome_forma)
    print(resultado)

main()