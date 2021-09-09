contador = 1
n = {}
elementos = []

while contador != 6:
    nv = 1
    (n[nv])=(input("Digite um elemento:"))
    elementos.append(n[nv]) 
    nv += 1
    contador = contador+1   

verificacao = input("O que você quer pesquisar?")
v = elementos.index(verificacao)
if verificacao in elementos:
    print("A posição do elemento pesquisado é: {}".format(v))
else:
    print("O item nao esta na lista")
