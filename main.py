import geometria

def calculo_circulo(tipo_calculo: str):
     raio = float(input("Raio: "))     
     match tipo_calculo:
        case 'area':  
            area = geometria.area_circulo(raio)
            return area
        case 'perimetro':
            perimetro = geometria.perimetro_circulo(raio)
            return perimetro
        case _:
            return "Calculo não identificado."
            
def calculo_triangulo(tipo_calculo: str):
     match tipo_calculo:
        case 'area':       
            altura = float(input("Altura: "))
            base = float(input("Base: "))
            area = geometria.area_triangulo(base, altura)
            return area
        case 'perimetro':
            lado_A = float(input("Lado A: "))
            lado_B = float(input("Lado B: "))
            lado_C = float(input("Lado C: "))
            perimetro = geometria.perimetro_triangulo(lado_A, lado_B, lado_C)
            return perimetro
        case 'apotema':
            lado = float(input("Tamanho do lado do triângulo equilátero: "))
            apotema = geometria.apotema(lado, 3)
            return apotema
        case _:
            return "Calculo não identificado."
         
def calculo_paralelogramo(tipo_calculo: str):
    altura = float(input("Altura: "))
    base = float(input("Base: "))   
    match tipo_calculo:
        case 'area':         
            area = geometria.area_paralelogramo(base, altura)
            return area
        case 'perimetro':
            perimetro = geometria.perimetro_paralelogramo(base, altura)     
            return perimetro
        case _:
            return "Calculo não identificado."
                        
def calcula_trapezio(tipo_calculo: str):
    match tipo_calculo:
        case 'area':
            base_maior = float(input("Base maior: "))
            base_menor = float(input("Base menor: "))
            altura = float(input("Altura: "))
            area = geometria.area_trapezio(base_maior, base_menor, altura)
            return area
        case 'perimetro':
            base_maior = float(input("Base maior: "))
            base_menor = float(input("Base menor: "))
            l1 = float(input("Lateral A: "))
            l2 = float(input("Lateral B: "))
            perimetro = geometria.perimetro_trapezio(base_maior, base_menor, l1, l2)
            return perimetro
        case _:
            return "Calculo não identificado."

def calcula_losango(tipo_calculo: str):
    match tipo_calculo:
        case 'area':
            diagonal_maior = float(input("Diagonal maior: "))
            diagonal_menor = float(input("Diagonal menor: "))
            area = geometria.area_triangulo(diagonal_maior, diagonal_menor) #A função area_triangulo() também é capaz de calcular a área de losangos se informados os valores das diagonais (ver documentação de geometria).
            return area
        case 'perimetro':
            lado = float(input("Lado: "))
            perimetro = geometria.perimetro_regular(lado, 4)
            return perimetro
        case _:
            return "Calculo não identificado."
            
def calculo_poliRegular(tipo_calculo: str, numero_lados: int):
    lado = float(input("Lado: "))
    match tipo_calculo:
        case 'area':        
            area = geometria.area_regular(lado, numero_lados)
            return area
        case 'apotema':
            apotema = geometria.apotema(lado, numero_lados)
            return apotema
        case 'perimetro':
            perimetro = geometria.perimetro_regular(lado, numero_lados)
            return perimetro
        case _:
            return "Calculo não identificado."
            
def classifica_forma(nome_forma: str, tipo_calculo: str):
    match nome_forma:
        case 'triangulo':
            resultado = calculo_triangulo(tipo_calculo)
        case 'circulo':
            resultado = calculo_circulo(tipo_calculo)
        case 'quadrado':
            resultado = calculo_poliRegular(tipo_calculo, 4)
        case 'retangulo':
            resultado = calculo_paralelogramo(tipo_calculo)
        case 'paralelogramo':
            resultado = calculo_paralelogramo(tipo_calculo)
        case 'trapezio':
            resultado = calculo_trapezio(tipo_calculo)
        case 'losango':
            resultado = calculo_losango(tipo_calculo)
        case 'pentagono':
            resultado = calculo_poliRegular(tipo_calculo, 5)
        case 'hexagono':
            resultado = calculo_poliRegular(tipo_calculo, 6)
        case _:
            resultado = "Forma não reconhecida, tente novamente."
    return resultado        
        
if __name__ == '__main__':
    print("Olá, este é um programa de calculos geometricos com Python.")
    print("Digite uma das seguintes formas para prosseguir: circulo, triangulo, quadrado, retangulo, trapezio, paralelogramo, losango, pentagono, hexagono.")
    nome_forma = input("Forma geometrica: ")
    if nome_forma == 'triangulo' or nome_forma == 'quadrado' or nome_forma == 'pentagono' or nome_forma == 'hexagono': #verifica se a forma é um polígono regular, indicando se é possível o cálculo da apótema.
        tipo_calculo = input("O que você quer calcular?(area, apotema, perimetro): ")
    else:
        tipo_calculo = input("O que você quer calcular?(area, perimetro): ")
    resultado = classifica_forma(nome_forma, tipo_calculo)
    print(resultado)
