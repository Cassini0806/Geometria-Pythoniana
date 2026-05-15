#Crie cada função e as documente (descrição e casos de teste).
#Crie um trecho de código que permita a execução automática dos casos de teste caso o módulo seja executado (ver aula sobre Doctest).

import math

#apotema
def apotema(lado: float, numero_lados: int):
    """apotema(lado: float, numero_lados: int)
    
    Retorna o apótema de um polígono regular em função da medida de seu lado e o número de lados (a = lado / (2 * tan(180⁰/ numero_lados))).
    Exemplo:
    >>> apotema(2, 4)
    1.0000000000000002
    >>> apotema(2, 3)
    0.577350269189626"""
    angulo_rad = math.radians(180 / numero_lados) #converte o ângulo de graus pra radianos
    apotema = lado / (2 * math.tan(angulo_rad))
    return float(apotema)

#perimetros
def perimetro_regular(lado: float, numero_lados: int):
    """perimetro_regular(lado: float, numero_lados: int)
    
    Retorna o perímetro de um polígono regular em função do seu número de lados e o comprimento destes (P = lado * número_lados).
    Exemplo:
    >>> perimetro_regular(2, 6)
    12.0
    >>> perimetro_regular(3, 5)
    15.0"""
    perimetro = lado * numero_lados
    return float(perimetro)

def perimetro_paralelogramo(lado_a: float, lado_b: float):
    """perimetro_paralelogramo(lado_a: float, lado_b: float)
    
    Retorna o perímetro de um paralelogramo qualquer em função de seu lado A e lado B (P = 2 (lado_A + lado_B)).
    Exemplo:
    >>> perimetro_paralelogramo(2, 2)
    8.0
    >>> perimetro_paralelogramo(3, 7)
    20.0"""
    perimetro = 2 * (lado_a + lado_b)
    return float(perimetro)

def perimetro_circulo(raio: float):
    """perimetro_circulo(raio: float)
    
    Retorna o perímetro de um círculo em função de seu raio (P = 2 * raio * pi).
    Exemplo:
    >>> perimetro_circulo(1)
    6.283185307179586
    >>> perimetro_circulo(2)
    12.566370614359172"""
    perimetro = 2 * raio * math.pi
    return float(perimetro)

def perimetro_triangulo(lado_a: float, lado_b: float, lado_c:  float):
    """perimetro_triangulo(lado_a: float, lado_b: float, lado_c:  float)
    
    Retorna o perímetro de um triângulo em função de seus lados (P = lado_A + lado_B + lado_C).
    Exemplo:
    >>> perimetro_triangulo(4, 4, 2)
    10.0
    >>> perimetro_triangulo(3, 4, 5)
    12.0"""
    perimetro = lado_a + lado_b + lado_c
    return float(perimetro)

def perimetro_trapezio(base_maior: float, base_menor: float, l1: float, l2: float):
    """perimetro_trapezio(base_maior: float, base_menor: float, l1: float, l2: float)
    
    Retorna o perímetro de um trapezio em função de seus lados (P = base_maior + base_menor + lado_1 + lado_2).
    Exemplo:
    >>> perimetro_trapezio(4, 3, 2, 2)
    11.0
    >>> perimetro_trapezio(7, 8, 5, 5)
    25.0"""
    perimetro = base_maior + base_menor + l1 + l2
    return float(perimetro)

#areas
def area_regular(lado: float, numero_lados: int):
    apot = apotema(lado, numero_lados)
    semiper = perimetro_regular(lado, numero_lados) / 2
    area = semiper * apot
    return area

def area_circulo(raio: float):
    """area_circulo(raio: float)

    Retorna a área de um círculo em função de seu raio (A = pi * raio^2).
    Exemplo:
    >>> area_circulo(2)
    12.566370614359172
    >>> area_circulo(5)
    78.53981633974483"""
    area = math.pi * math.pow(raio, 2)
    return float(area)

def area_paralelogramo(base: float, altura: float):
    """area_paralelogramo(base: float, altura: float)

    Retorna a área de um paralelogramo qualquer (quadrado, retângulo, etc) em função de sua base e sua altura (A = base * altura).
    Obs: esta função não se aplica a losangos, nesse caso, utilize a função area_triangulo(), informando os valores das diagonais menor e maior nos parâmetros.
    Exemplo:
    >>> area_paralelogramo(2, 2)
    4.0
    >>> area_paralelogramo(2,5)
    10.0"""
    area = base * altura
    return float(area)

def area_triangulo(base: float, altura: float):
    """area_triangulo(base: float, altura: float)

    Retorna a área de um triângulo em função de sua base e sua altura (A = base * altura / 2).
    Obs: é possível calcular a área de um losango com esta função, basta informar os valores das diagonais nos parâmetros.
    Exemplo:
    >>> area_triangulo(3, 4)
    6.0
    >>> area_triangulo(3, 5)
    7.5"""
    area = area_paralelogramo(base, altura) / 2
    return float(area)    

def area_trapezio(base_maior: float, base_menor: float, altura: float):
    """area_trapezio(base_maior: float, base_menor: float, altura: float)
    
    Retorna a área de um trapézio em função de sua bases maior, sua base menor e sua altura (A = (base maior + base menor) * altura / 2).
    Exemplo:
    >>> area_trapezio(5, 3, 2)
    8.0
    >>> area_trapezio(8, 4, 3)
    18.0"""
    area = (base_maior + base_menor) * altura / 2
    return float(area)      

if __name__ == '__main__':
    import doctest
    doctest.testmod()