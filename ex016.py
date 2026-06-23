# Desafio: Crie um programa que leia um número real pelo teclado e mostre na tela somente sua porção inteira. Use a biblioteca
# math com trunc() e também resolva com a função nativa int().
# Exemplo de saída:
# Digite o valor: 98.756
# O valor digitado foi 98.756 e sua porção inteira 

from math import trunc 

numero = float(input("Digite um numero real: "))
inteiro = trunc(numero)
print(f"A porção inteira do número digitado é {inteiro}")