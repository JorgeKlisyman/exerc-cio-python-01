# Leitura da altura e do sexo
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

# Cálculo do peso ideal
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura}m é {peso_ideal:.2f} kg.")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura}m é {peso_ideal:.2f} kg.")
else:
    print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")
