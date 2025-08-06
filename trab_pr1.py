print("Bem Vindos ao Mercadinho do Felipe Angelo")

valor = float(input("Digite o valor do produto: R$"))
qtd = int(input("Digite o total de parcelas desejada: "))

if (qtd <= 3):
    print (f"O valor do produto é de R${valor} em {qtd}x sem juros.") 
    
#Aqui optei por não colocar o calculo de juros pois a quantidade de parcelas sempre será inferior que 4, onde não haverá juros. 

elif (qtd <=5):
    parc = valor * (1 + (4/100)) / qtd
    total = parc * qtd
    print (f"O valor final ficará de R${total} em {qtd}x de R${parc} com juros")

#A partir daqui o calculo de juros já será utilizado.

elif (qtd <= 8):
    parc = valor * (1 + (8/100)) / qtd
    total = parc * qtd
    print (f"O valor final ficará de R${total} em {qtd}x de R${parc} com juros")

elif (qtd <= 12):
    parc = valor * (1 + (16/100)) / qtd
    total = parc * qtd
    print (f"O valor final ficará de R${total} em {qtd}x de R${parc} com juros")

else:
    (qtd > 13)
    parc = valor * (1 + (32/100)) / qtd
    total = parc * qtd
    print (f"O valor final ficará de R${total} em {qtd}x de R${parc} com juros")
    








