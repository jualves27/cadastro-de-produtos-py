# Demonstração da lógica independente da sintaxe avançada do Python, 
# utilizando vetores, laços simples (for), ordenação por bolha (bubble sort) 
# e simulação manual de conjuntos.

TAMANHO = 3

nomes = [""] * TAMANHO
precos = [0.0] * TAMANHO
categorias = [""] * TAMANHO

# Leitura com laço simples
for i in range(TAMANHO):
    print(f"\n Produto {i + 1} ")
    nomes[i] = input("Nome: ")
    precos[i] = float(input("Preço: R$ "))
    categorias[i] = input("Categoria: ")

#  Ordenação pelo Método da Bolha (Bubble Sort) 
for i in range(TAMANHO):
    for j in range(0, TAMANHO - i - 1):
        if precos[j] > precos[j + 1]:
            # Troca de posição dos preços
            temp_preco = precos[j]
            precos[j] = precos[j + 1]
            precos[j + 1] = temp_preco
            
            # Troca de posição dos nomes correspondentes
            temp_nome = nomes[j]
            nomes[j] = nomes[j + 1]
            nomes[j + 1] = temp_nome

print("\n Produtos Ordenados via Bubble Sort ")
for i in range(TAMANHO):
    print(f"{nomes[i]} - R$ {precos[i]:.2f}")

# Simulação Manual de Conjuntos (Filtro de Duplicadas) 
categorias_unicas_manual = []
for i in range(TAMANHO):
    cat_atual = categorias[i]
    repetida = False
    
    for j in range(len(categorias_unicas_manual)):
        if categorias_unicas_manual[j] == cat_atual:
            repetida = True
            break
            
    if not repetida:
        categorias_unicas_manual.append(cat_atual)

print("\n Categorias Únicas (Processamento Manual) ")
for i in range(len(categorias_unicas_manual)):
    print(f"- {categorias_unicas_manual[i]}")

# --- Cálculo Manual de Estatísticas ---
soma = 0.0
menor = precos[0]
maior = precos[0]

for i in range(TAMANHO):
    soma += precos[i]
    if precos[i] < menor:
        menor = precos[i]
    if precos[i] > maior:
        maior = precos[i]

media = soma / TAMANHO

print("\n Estatísticas (Cálculo Manual)")
print(f"Menor Preço: R$ {menor:.2f}")
print(f"Maior Preço: R$ {maior:.2f}")
print(f"Média: R$ {media:.2f}")