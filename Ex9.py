contador = 1
n = {}
numeros = []

while contador != 6:
    nv = 1
    (n[nv])=int(input("Digite o {}º numero:".format(contador)))
    numeros.append(n[nv]) 
    nv += 1
    contador = contador+1   
 
print("Lista ordenada em ordem crescente:", sorted(numeros))