# Leitura dos dados da pessoa
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil (SOLTEIRA/CASADA): ").upper()

# Verifica se o sexo é "F" e o estado civil é "CASADA"
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Há quantos anos você está casada? "))
    print(f"{nome}, você está casada há {tempo_casada} anos.")
else:
    print(f"{nome}, não há informações adicionais necessárias.")

