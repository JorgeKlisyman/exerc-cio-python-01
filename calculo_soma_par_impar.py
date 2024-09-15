# Leitura do número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar e realiza a operação
if numero % 2 == 0:
    resultado = numero + 5
    print(f"O número é par. Resultado após somar 5: {resultado}")
else:
    resultado = numero + 8
    print(f"O número é ímpar. Resultado após somar 8: {resultado}")
