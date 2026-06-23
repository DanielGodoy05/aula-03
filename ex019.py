# Desafio: Crie um programa que leia o nome de 4 alunos e sorteie
# um deles para realizar uma tarefa. Use random.choice().

from random import choice

aluno1 = str(input("Digite o nome do 1° aluno: "))
aluno2 = str(input("Digite o nome do 2° aluno: "))
aluno3 = str(input("Digite o nome do 3° aluno: "))
aluno4 = str(input("Digite o nome do 4° aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)

print(f"O aluno escolhido foi: {escolhido}")