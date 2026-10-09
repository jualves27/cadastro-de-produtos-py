produtos = []

qtd = int(input("Quantos produtos deseja cadastrar?"))

for i in range(qtd):
    print(f"\nProduto {i + 1}")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    categoria = input("Categoria do produto: ")
    
    produtos.append({
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    })