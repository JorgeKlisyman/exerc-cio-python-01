# Leitura dos valores inteiros A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verifica se os valores são iguais
if A == B:
    C = A + B
    print(f"Os valores são iguais. Soma: C = {C}")
else:
    C = A * B
    print(f"Os valores são diferentes. Multiplicação: C = {C}")
