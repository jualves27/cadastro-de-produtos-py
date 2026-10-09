produtos = []
categorias_unicas = {p["categoria"] for p in produtos}

print("Categorias únicas cadastradas:")
for categoria in categorias_unicas:
    print(f"- {categoria}")