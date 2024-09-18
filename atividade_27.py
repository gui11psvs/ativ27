# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produtos = []
estoques = []

for i in range(1, 6):
    produto = input(f"Nome do produto {i}: ")
    produtos.append(produto)

for i in range(1, 6):
    estoque = int(input(f"Quantidade em estoque do produto {produtos[i-1]}: "))
    estoques.append(estoque)

produtos_zerados = [produtos[i] for i in range(5) if estoques[i] == 0]

if produtos_zerados:
    print(f"Produtos com estoque zerado: {', '.join(produtos_zerados)}")
else:
    print("Nenhum produto está com estoque zerado.")
