preco = float(input("Digite o Preço do produto: "))
percentual = float(input("Digite o Percentual de desconto do produto: "))
desconto =( percentual / 100) * preco
final = preco - desconto
print(  f"O valor do desconto é de R${desconto} aplicado ao preço do produto ficarar de R${final}")