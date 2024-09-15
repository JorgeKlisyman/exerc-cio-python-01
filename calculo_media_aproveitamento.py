# Leitura do número de identificação e das notas
id_aluno = input("Digite o número de identificação do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
ME = float(input("Digite a média dos exercícios (ME): "))

# Cálculo da média de aproveitamento (MA)
MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7

# Determinação do conceito
if MA >= 90:
    conceito = 'A'
    status = 'Aprovado'
elif MA >= 75:
    conceito = 'B'
    status = 'Aprovado'
elif MA >= 60:
    conceito = 'C'
    status = 'Aprovado'
elif MA >= 40:
    conceito = 'D'
    status = 'Reprovado'
else:
    conceito = 'E'
    status = 'Reprovado'

# Exibição dos resultados
print(f"\nNúmero de identificação do aluno: {id_aluno}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios (ME): {ME}")
print(f"Média de aproveitamento (MA): {MA:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")
