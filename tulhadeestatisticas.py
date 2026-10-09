
produtos = [
    {"nome": "Teclado", "preco": 150.0, "categoria": "Eletrônicos"},
    {"nome": "Mouse", "preco": 80.0, "categoria": "Eletrônicos"},
    {"nome": "Caderno", "preco": 20.0, "categoria": "Papelaria"}
]


precos = [p["preco"] for p in produtos]

tupla_estatisticas = (
    min(precos),
    max(precos),
    sum(precos) / len(precos)
)


print(f"Menor Preço: R$ {tupla_estatisticas[0]:.2f}")
print(f"Maior Preço: R$ {tupla_estatisticas[1]:.2f}")
print(f"Média dos Preços: R$ {tupla_estatisticas[2]:.2f}")