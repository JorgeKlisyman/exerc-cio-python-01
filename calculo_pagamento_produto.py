# Leitura do preço do produto
preco_etiqueta = float(input("Digite o preço do produto: "))

# Leitura da condição de pagamento
print("Escolha a condição de pagamento:")
print("1 - À vista em dinheiro ou cheque (10% de desconto)")
print("2 - À vista no cartão de crédito (15% de desconto)")
print("3 - Em duas vezes, sem juros")
print("4 - Em duas vezes, com 10% de juros")
condicao = int(input("Digite o código da condição de pagamento: "))

# Cálculo do valor a ser pago conforme a condição de pagamento
if condicao == 1:
    valor_final = preco_etiqueta * 0.90  # 10% de desconto
    print(f"O valor a ser pago à vista em dinheiro ou cheque é R${valor_final:.2f}.")
elif condicao == 2:
    valor_final = preco_etiqueta * 0.85  # 15% de desconto
    print(f"O valor a ser pago à vista no cartão de crédito é R${valor_final:.2f}.")
elif condicao == 3:
    valor_final = preco_etiqueta  # Sem juros
    print(f"O valor a ser pago em duas vezes, sem juros, é R${valor_final:.2f}.")
elif condicao == 4:
    valor_final = preco_etiqueta * 1.10  # 10% de juros
    print(f"O valor a ser pago em duas vezes, com 10% de juros, é R${valor_final:.2f}.")
else:
    print("Condição de pagamento inválida.")
