# Desafio: Crie um programa que leia um ângulo em graus e exiba o valor do seno, cosseno e tangente. Lembre-se: as
# funções da biblioteca math trabalham em radianos — converta antes com math.radians().
# Exemplo de saída para 30°:
# O ângulo de 30° tem:
# Seno: 0.50 | Cosseno: 0.87 | Tangente: 0.58

from math import radians, sin, cos, tan

angulo = int(input("Digite um ângulo: "))
rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print(f"O ângulo {angulo: .2f}° tem Seno:{seno: .2f}° Cosseno:{cosseno: .2f}° Tangente:{tangente: .2f}°")