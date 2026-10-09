# Impressão do relatório utilizando obrigatoriamente f-strings
produtos =[]
print("=" * 45)
print("RELATÓRIO FINAL DE PRODUTOS")
print("=" * 45)

print("\n Lista Completa de Produtos")
for p in produtos:
    print(
        f"Nome: {p['nome']:<15} | "
        f"Categoria: {p['categoria']:<12} | "
        f"Preço: R$ {p['preco']:.2f}"
    )

print(f"\n Categorias Identificadas ({len(categorias_unicas)})")
for cat in categorias_unicas:
    print(f"- {cat}")

print("\n--- Estatísticas de Preços ---")
print(f"Menor valor encontrado: R$ {tupla_estatisticas[0]:.2f}")
print(f"Maior valor encontrado: R$ {tupla_estatisticas[1]:.2f}")
print(f"Média de valor geral:   R$ {tupla_estatisticas[2]:.2f}")

print("=" * 45)