produtos = []
produtos_crescente = produtos.copy()
produtos_crescente.sort(key=lambda p: p["preco"])

produtos_decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)

print("--- Ordem Crescente de Preço ---")
for p in produtos_crescente:
    print(f"{p['nome']} - R$ {p['preco']:.2f}")

print("\n--- Ordem Decrescente de Preço ---")
for p in produtos_decrescente:
    print(f"{p['nome']} - R$ {p['preco']:.2f}")