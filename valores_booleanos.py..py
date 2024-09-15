# Leitura dos valores booleanos
A = input("Digite o primeiro valor booleano (True/False): ").capitalize() == "True"
B = input("Digite o segundo valor booleano (True/False): ").capitalize() == "True"

# Verifica se ambos são verdadeiros ou ambos são falsos
if A and B:
    print("Ambos são verdadeiros.")
elif not A and not B:
    print("Ambos são falsos.")
else:
    print("Os valores são diferentes.")
