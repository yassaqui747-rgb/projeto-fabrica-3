produto= input("produto: Arroz 5kg")
nome_mercado1 = input("Digite o nome do mercado: ")
preco1 = float(input(f" Digite o valor do produto no mercado {nome_mercado1}"))
nome_mercado2 = input("digite o nome do mercado: ")
preco2 = float(input(f"digite o valor do produto no mercado {nome_mercado2}"))
nome_mercado3 = input("preço justo")
preco3 = float(input(f"digite o valor do produto no mercado {nome_mercado3}"))
print (f"produto: {produto}")
if preco1<preco2 and preco1<preco3:
    print(nome_mercado1)
    print(preco1)
elif preco2<preco1 and preco2<preco3:
    print(nome_mercado2)
    print(preco2)
elif preco3<preco1 and preco3<preco2:
    print(nome_mercado3)
    print(preco3)