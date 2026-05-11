#calcular a área e o perímetro das seguintes figuras geométricas planas: círculo, triângulo, quadrado, retângulo, trapézio, paralelogramo, losango, pentágono, hexágono.
#Defina um plano para resolução disso, contemplando:
#Como calcular o perímetro de cada figura geométrica plana?
#Como calcular a área de cada figura geométrica plana?
#Crie exemplos para cada um desses cálculos
#Identifique que funções você precisa criar para este módulo.
#Para cada fórmula, talvez você crie uma respectiva função.
#Quais serão os parâmetros de cada função?
#Qual será o valor retornado por cada função?
#Existem figuras que "compartilham" a fórmula e podem ser calculadas pela mesma função?
#Crie cada função e as documente (descrição e casos de teste).
#Crie um trecho de código que permita a execução automática dos casos de teste caso o módulo seja executado (ver aula sobre Doctest).

import math

def apotema(lado: float, numero_lados: int):
    """apotema(lado: float, numero_lados: int)

    Retorna o apótema de um polígono regular em função da medida de seu lado e o número de lados (a = lado / (2 * tan(180⁰/ numero_lados)))."""
    angulo_rad = math.radians(180 / numero_lados) #converte o ângulo de graus pra radianos
    apotema = lado / (2 * math.tan(angulo_rad))
    return float(apotema)

#perimetros
def perimetro_regular(lado: float, numero_lados: int):
    """perimetro_regular(lado: float, numero_lados: int)
    
    Retorna o perímetro de um polígono regular em função do seu número de lados e o comprimento destes (P = lado * número_lados)."""
    perimetro = lado * numero_lados
    return float(perimetro)

def perimetro_paralelogramo(lado_a: float, lado_b: float):
    """perimetro_paralelogramo(lado_a: float, lado_b: float)
    
    Retorna o perímetro de um paralelogramo qualquer em função de seu lado A e lado B (P = 2 (lado_A + lado_B))."""
    perimetro = 2 * (lado_a + lado_b)
    return float(perimetro)

def perimetro_circulo(raio: float):
    """perimetro_circulo(raio: float)
    
    Retorna o perímetro de um círculo em função de seu raio (P = 2 * raio * pi)."""
    perimetro = 2 * raio * math.pi
    return float(perimetro)

def perimetro_triangulo(lado_a: float, lado_b: float, lado_c:  float):
    """perimetro_triangulo(lado_a: float, lado_b: float, lado_c:  float)
    
    Retorna o perímetro de um triângulo em função de seus lados (P = lado_A + lado_B + lado_C)."""
    perimetro = lado_a + lado_b + lado_c
    return float(perimetro)

#areas
def area_circulo(raio: float):
    """area_circulo(raio: float)

    Retorna a área de um círculo em função de seu raio (A = pi * raio^2)."""
    area = math.pi * math.pow(raio, 2)
    return float(area)

def area_paralelogramo(base: float, altura: float):
    """area_paralelogramo(base: float, altura: float)

    Retorna a área de um paralelogramo qualquer (losango, quadrado, retângulo, etc) em função de sua base e sua altura (A = base * altura).
    Obs: no caso de um losango, informar a medidade de suas diagonais maior e menor."""
    area = base * altura
    return float(area)

def area_triangulo(base: float, altura: float):
    """area_triangulo(base: float, altura: float)

    Retorna a área de um triângulo em função de sua base e sua altura (A = base * altura / 2)."""
    area = area_paralelogramo(base, altura) / 2
    return float(area)    

def area_triangulo_equilatero(lado: float):
    """area_triangulo_equilatero(lado: float)

    Retorna a área de um triângulo equilátero em função de seu lado (A = lado^2 * 3^0.5 / 4)."""
    area = math.pow(lado, 2) * math.sqrt(3) / 4
    return float(area)
    
def area_trapezio(base_maior: float, base_menor: float, altura: float):
    """area_trapezio(base_maior: float, base_menor: float, altura: float)
    
    Retorna a área de um trapézio em função de sua bases maior, sua base menor e sua altura (A = (base maior + base menor) * altura / 2)."""
    area = (base_maior + base_menor) * altura / 2
    return float(area)
    
def area_pentagono(lado: float):
    """area_pentagono(lado: float)
    
    Retorna a área de um pentagono regular em função de seu lado, através da medida de seu perímetro e seu apotema (A = perimetro * apotema / 2)."""
    apotema_pent = apotema(lado, 5)
    perimetro_pent = perimetro_regular(lado, 5)
    area = perimetro_pent * apotema_pent / 2 
    return float(area)

def area_hexagono(lado: float):
    """area_hexagono(lado: float)

    Retorna a área de um hexagono regular em função de seu lado (A = 6 * lado^2 * 3^0.5) / 4)."""
    area =  area_triangulo_equilatero(lado) * 6
    return float(area)       
