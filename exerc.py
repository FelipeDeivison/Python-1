#QUESTÕES DA AULA TEÓRICA 2
#• Escreva as seguintes expressões matemáticas em linguagem Python:
#a. 2 + 3 x 3
#b. 4² ÷ 3
#c. (9² + 2) x 6 - 1

print(2+(3*3))

print((4**2)/3)

print((9**2 + 2) * 6 -1)

#Douglas Adams nos ensinou que a resposta para o sentido da vida, do Universo e tudo mais é 42. Armazene, então, em uma variável, o sentidoda vida. Crie uma mensagem que imprima na tela essa variável, junto de uma frase dizendo que ela é o sentido da vida.

sentido_da_vida = 42
mensagem = f"Douglas Adams nos ensinou que a resposta para o sentido da vida, do Universo e tudo mais é {sentido_da_vida}."
print(mensagem)

#Crie uma variável que receba uma nota de um aluno. Crie outra variável que receba o resultado de uma comparação lógica entre a nota escolhida e o valor 7, que é a média para aprovação. Caso a nota seja maior ou igual a 7, o resultado deve ser verdadeiro. Imprima o resultado da comparação na tela.

nota = 8.5
aprovacao= nota >= 7
print(aprovacao)

#Imprima, na tela, uma variável do tipo string que escreva a seguinte frase:
#Linguagens de programação:
#Python ----- C ----- Java ----- PHP
#Para dar uma quebra de linha (enter), utilize \n. Para fazer uma tabulação
#(tab), use \t. Não se esqueça de usar também o multiplicador de strings.

v1 = "Linguagens de programação:"
v2 = "Python" + "-"*5
v3 = "C" + "-"*5
v4 = "Java" + "-"*5
v5 = "PHP"
print(v1 + v2 + v3 + v4 + v5)

#EXERCICIOS DA AULA PRATICA 2

print((23 + 19 + 32) / 3)

A = 3
print(A)

s1 = "ant"
s2 = "bat"
s3 = "cod"
res = s1 + " " + ((s2 + " ") * 2) + ((s3 +" ") * 3)
print(res)

resp = (s1 + " " + s2 + " ") * 7
print(resp)

respo = (s2 + s2 + s3 + " ") * 5
print(respo)






