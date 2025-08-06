print("Lanchonete")
print("1 Coxinha - R$5,00")
print("2 Pastel - R$7,00")
print("3 Café - R$4,00")
print("4 Suco - R$6,00")
print(" 5 SAIR")

total = 0
while True:
 op = int(input("Qual item gostaria de comprar? "))
 qts = int(input("Quantas unidades quer comprar? "))

 if (op == 1):
  total = total + qts * 5
 
 elif (op == 2):
  total = total + qts * 7
 
 elif (op == 3):
  total = total + qts * 4
 
 elif (op == 4):
  total = total + qts * 6
 
 elif (op == 5):
   break
else:
  print("Produto inválido!")

print(f"O Total a pagar é de R${total}")
