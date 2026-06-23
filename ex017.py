# Desafio: Crie um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo e calcule
# a hipotenusa. Resolva de duas formas: com a fórmula matemática
# e com math.hypot().

from math import hypot 

CO = float(input("Digite o cateto oposto: "))
CA = float(input("Digite o cateto adjacente: "))
HP = hypot(CO, CA)

print(f"A hipotenusa do triângulo é: {HP: .2f}")