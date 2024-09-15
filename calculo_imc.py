# Leitura do peso e altura
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Determinação da condição com base no IMC
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Condição: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Condição: Peso normal")
elif 25 <= imc < 30:
    print("Condição: Acima do peso")
else:
    print("Condição: Obeso")
