import geometria

def calculo_circulo(tipo_calculo: str):
    """calculo_circulo(tipo_calculo: str)
    
    Para cálculos com círculos, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: área, perímetro."""
    try:
        raio = float(input("Raio: "))
        match tipo_calculo:
            case 'area':  
                area = geometria.area_circulo(raio)
                return "Área = %.4f" % area
            case 'perimetro':
                perimetro = geometria.perimetro_circulo(raio)
                return "Perímetro = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."

def calculo_triangulo(tipo_calculo: str):
    """calculo_triangulo(tipo_calculo: str)
    
    Para cálculos com triângulos, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: área, perímetro."""
    try:
        match tipo_calculo:
            case 'area':       
                altura = float(input("Altura: "))
                base = float(input("Base: "))
                area = geometria.area_triangulo(base, altura)
                return "Área = %.4f" % area
            case 'perimetro':
                lado_A = float(input("Lado A: "))
                lado_B = float(input("Lado B: "))
                lado_C = float(input("Lado C: "))
                perimetro = geometria.perimetro_triangulo(lado_A, lado_B, lado_C)
                return "Perímetro  = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."

def calculo_paralelogramo(tipo_calculo: str):
    """calculo_paralelogramo(tipo_calculo: str)
    
    Para cálculos com paralelogramos, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: área, perímetro."""
    try:
        altura = float(input("Altura: "))
        base = float(input("Base: "))   
        match tipo_calculo:
            case 'area':         
                area = geometria.area_paralelogramo(base, altura)
                return "Área = %.4f" % area
            case 'perimetro':
                perimetro = geometria.perimetro_paralelogramo(base, altura)     
                return "Perímetro = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."
    
def calculo_trapezio(tipo_calculo: str):
    """calcula_trapezio(tipo_calculo: str)
    
    Para cálculos com trapézios, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: área, perímetro."""
    try:
        match tipo_calculo:
            case 'area':
                base_maior = float(input("Base maior: "))
                base_menor = float(input("Base menor: "))
                altura = float(input("Altura: "))
                area = geometria.area_trapezio(base_maior, base_menor, altura)
                return "Área = %.4f" % area
            case 'perimetro':
                base_maior = float(input("Base maior: "))
                base_menor = float(input("Base menor: "))
                l1 = float(input("Lateral A: "))
                l2 = float(input("Lateral B: "))
                perimetro = geometria.perimetro_trapezio(base_maior, base_menor, l1, l2)
                return "Perímetro = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."


def calculo_losango(tipo_calculo: str):
    """calcula_losango(tipo_calculo: str)
    
    Para cálculos com losangos, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: área, perímetro."""
    try:
        match tipo_calculo:
            case 'area':
                diagonal_maior = float(input("Diagonal maior: "))
                diagonal_menor = float(input("Diagonal menor: "))
                area = geometria.area_triangulo(diagonal_maior, diagonal_menor) #A função area_triangulo() também é capaz de calcular a área de losangos se informados os valores das diagonais (ver documentação de geometria).
                return "Área = %.4f" % area
            case 'perimetro':
                lado = float(input("Lado: "))
                perimetro = geometria.perimetro_regular(lado, 4)
                return "Perímetro = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."
           
def calculo_poliRegular(tipo_calculo: str, numero_lados: int):
    """calculo_poliRegular(tipo_calculo: str, numero_lados: int)
    
    Para cálculos com polígonos regulares, recebe o tipo de cálculo, chama a função do cálculo no módulo 'geometria' correspondente e retorna o valor da operação.
    Os cálculos disponíveis são: apótema, área, perímetro."""
    try:
        lado = float(input("Lado: "))
        match tipo_calculo:
            case 'area':        
                area = geometria.area_regular(lado, numero_lados)
                return "Área = %.4f" % area
            case 'apotema':
                apotema = geometria.apotema(lado, numero_lados)
                return "Apótema = %.4f" % apotema
            case 'perimetro':
                perimetro = geometria.perimetro_regular(lado, numero_lados)
                return "Perímetro = %.4f" % perimetro
            case _:
                return "Calculo não identificado."
    except ValueError:
        return "Erro: Digite apenas números."

def classifica_forma(nome_forma: str, tipo_calculo: str):
    """classifica_forma(nome_forma: str, tipo_calculo: str)
    
    Recebe o nome da forma geométrica e o tipo de cálculo a ser efetuado, chama a função de cálculo da forma e retorna o resultado dessa função."""
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
        case 'triangulo equilatero':
            resultado = calculo_poliRegular(tipo_calculo, 3)
    return resultado        

if __name__ == '__main__':
    print("Olá, este é um programa de cálculos geometricos com Python.")
    print("Digite uma das seguintes formas para prosseguir: circulo, triangulo, triangulo equilatero, quadrado, retangulo, trapezio, paralelogramo, losango, pentagono, hexagono.")
    #lista de formas validas e formas com apótema
    formas_validas = ['circulo', 'triangulo', 'triangulo equilatero', 'quadrado', 'retangulo', 'trapezio', 'paralelogramo', 'losango', 'pentagono', 'hexagono']
    formas_com_apotema = ['triangulo equilatero', 'quadrado', 'pentagono', 'hexagono']
    
    nome_forma = input("Forma geometrica: ").lower().strip().replace("â", "a")
    if nome_forma in formas_validas:
        if nome_forma in formas_com_apotema: #verifica se a forma é um polígono regular, indicando se é possível o cálculo da apótema.
            tipo_calculo = input("O que você quer calcular?(area, apotema, perimetro): ").lower().strip().replace("á", "a")
        else:
            tipo_calculo = input("O que você quer calcular?(area, perimetro): ").lower().strip().replace("á", "a")
    else:
        print("Forma não reconhecida, tente novamente.")
        exit()   
    resultado = classifica_forma(nome_forma, tipo_calculo)
    print(resultado) 