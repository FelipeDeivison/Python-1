print("Bem-Vindos ao varejo de camisetas do Felipe Angelo\n") 
print("Operamos com as seguintes opções:\n") #Adicionei um menu por estetica
print("Camisetas Manga Curta Simples (MCS)\n O valor unitário é de R$1,80.\n")
print("Manga Longa Camiseta Simples (MLS)\n O valor unitário é de R$2,10.\n")
print("Camiseta Manga Curta Com Estampa (MCE)\n O valor unitário é de R$2,90.\n")
print("Camiseta Manga Longa Com Estampa (MLE)\n O valor unitário é de R$3,20.\n")

def escolha_modelo(): #Função criada para escolher os modelos das camisetas e informar o valor no calculo final.
   while True:
      try:
         modelo = (input("Escolha a opção desejada das camisetas: "))

         if modelo == "MCS":
            preco = 1.80
         elif modelo == "MLS":
            preco = 2.10
  
         elif modelo == "MCE":
            preco = 2.90

         elif modelo == "MLE":
            preco = 3.20
         
         return preco
           
      except:
         print("Opção inválida, informar modelos disponiveis!")
         continue


def num_camisetas(): #Função que calcula o desconto de acordo com a quantidade escolhida.
   while True:
      try:
         quantidade = float(input("Escolha a quantidade desejada: "))
     
         if quantidade <= 0:
            print("Número inválido, digite pelo menos uma unidade!")
            continue
         elif quantidade < 20:
            desconto = 0
         elif quantidade <= 200:
           desconto = 0.05

         elif quantidade <= 2000:
           desconto = 0.07
         elif quantidade <= 20000:
           desconto = 0.12
         elif quantidade > 20000:
           print("Não é aceito pedidos nessa quantidade! (Maximo 20000 unidades)")
         
         qtd_descontada = quantidade * (1 - desconto)
         
         return qtd_descontada, quantidade , desconto
      except:
         print("Informe novamente a quantidade de camisetas que deseja!")
         continue
      
      
def frete(): #Calcula o valor do frete e retorna o valor para o calculo final.
   while True:
      try:
         print("Serviço adicionais de  frete:")
         print("0 - Retirada na fábrica (Opção gratuita);")
         print("1 - Por transportadora,será cobrado um valor extra de R$100;")
         print("2 - Por Sedex, será cobrado um valor extra de R$200;")
   
         frete = float(input("Escolha uma das opções de frete: "))

         if frete == 0:
            valor_frete = 0
         elif frete == 1:
            valor_frete = 100
         elif frete == 2:
            valor_frete = 200
         return valor_frete
      except:
         print("Desculpe opção inválida, tente novamente!")
         continue

if __name__ == "__main__":
   try:
      valor_unitario= escolha_modelo()
      qtd_descontada, quantidade, desconto = num_camisetas()
      valor_frete = frete()
       
      total = (valor_unitario * qtd_descontada + valor_frete)

      print("Resumo do pedido\n")
        # Mostra modelo, quantidade, desconto e frete
      print(f"Valor unitário: R${valor_unitario}")
      print(f"Quantidade informada: {quantidade} unidades")
      print(f"Desconto aplicado: {desconto * 100}% OFF")
      print(f"Frete: R$ {valor_frete}")
      print(f"Total a pagar: R$ {total}")
   except:
      print("Ocorreu um erro inesperado:")