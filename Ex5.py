contador = 1
n = {}
elementos = []

while contador != 6:
    nv = 1
    (n[nv])=(input("Digite um elemento:"))
    elementos.append(n[nv]) 
    nv += 1
    contador = contador+1   
verificação = input("O que você quer pesquisar?")
if verificação in elementos:
    print("O item esta na lista")
else:
    print("O item nao esta na lista")
