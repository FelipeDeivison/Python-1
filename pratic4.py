
km = float(input("Quantos KM foram percorridos pelo carro alugado?"))
dias = float(input("Por quantos dias o carro foi alugado?"))
preco_por_dias = dias * 60
preco_por_km = km * 0.15
preco_final = preco_por_dias + preco_por_km

print(f"O valor total por dias alugados é de R${preco_por_dias}")
print(f"O valor por KM's percorridos é de R${preco_por_km}")
print(f"O valor total a pagar será de {preco_final}")