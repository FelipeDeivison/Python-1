print ("Bem Vindos ao iFood do Felipe Angelo")
print ("Para o cardápio teremos os seguintes pratos: \n")
print ("Marmitas no tamanho P, M e G: \n")
print ("No tamanho P teremos:\n \n BA - Bife Acebolado custando R$16,00\n FF - Filé de Frango custando R$15,00\n")
print ("No tamanho M teremos:\n \n BA - Bife Acebolado custando R$18,00\n FF - Filé de Frango custando R$17,00\n")
print (" No Tamanho G teremos:\n \n BA - Bife Acebolado custando R$22,00\n FF - Filé de Frango custando R$21,00\n")
print ("Caso queira zerar todos os pedidos digite LIMPAR no local do sabor do pedido.")
# Peguei a dica do professor de utilizar o \n para deixar a saida do código mais organizada

valor = 0

while True:
  sabor = input("Digite o sabor da marmita BA ou FF: ")

  if sabor == "BA":
    tamanho = input("Digite o tamanho da marmita P, M ou G: ")
    if tamanho == "P":
      valor += 16
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")
    elif tamanho == "M":
      valor += 18
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")
    elif tamanho == "G":
      valor += 22
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")

  if sabor == "FF":
    tamanho = input("Digite o tamanho da marmita P, M ou G: ")
    if tamanho == "P":
      valor += 15
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")
    elif tamanho == "M":
      valor += 17
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")
    elif tamanho == "G":
      valor += 21
      conti = input ("Deseja continuar o pedido? Digite S ou N: ")
      if conti == "N":
        print (f"O valor total a pagar é de R${valor}.")
        break
      elif conti == "S":
        print ("Continuando o pedido...")
      else:
        print ("Opção inválida! Por favor digitar somente S ou N")

  elif sabor == "LIMPAR":
    print ("Reiniciando o pedido...")
    valor = 0
    continue
  #Utilizei o continue para reiniciar o programa caso o usuário tenha errado o pedido.

  else:
    if sabor != "BA" and sabor != "FF":
      print (f"Sabor inválido! Por favor digitar somente sabores disponível\n Exemplo: BA ou FF")
    
    elif tamanho != "P" and tamanho != "M" and tamanho != "G":
      print (f"Tamanho inválido! Por favor digitar somente tamanhos disponível\n Exemplo: P, M ou G")