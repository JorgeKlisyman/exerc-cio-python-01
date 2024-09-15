# Leitura do número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo e calcula o resultado
if numero >= 0:
    resultado = numero * 2
    print(f"O número é positivo. O dobro de {numero} é {resultado}.")
else:
    resultado = numero * 3
    print(f"O número é negativo. O triplo de {numero} é {resultado}.")
