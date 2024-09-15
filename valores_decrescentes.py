# Leitura dos três valores inteiros
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

# Coloca os valores em uma lista
valores = [A, B, C]

# Ordena a lista em ordem decrescente
valores.sort(reverse=True)

# Exibe os valores em ordem decrescente
print("Valores em ordem decrescente:", valores)
