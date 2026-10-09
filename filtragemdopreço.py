produtos = []
valor_limite = float(input("Informe o valor para filtragem: R$ "))

produtos_acima = [p for p in produtos if p["preco"] > valor_limite]


produtos_abaixo = [p for p in produtos if p["preco"] <= valor_limite]

print(f"\n--- Produtos com preço ACIMA de R$ {valor_limite:.2f} ---")
for p in produtos_acima:
    print(f"- {p['nome']}: R$ {p['preco']:.2f}")

print(f"\n--- Produtos com preço ABAIXO de R$ {valor_limite:.2f} ---")
for p in produtos_abaixo:
    print(f"- {p['nome']}: R$ {p['preco']:.2f}")