contador = 1
n = {}
lista = []
while contador != 6:
    nv = 1
    (n[nv])= (input("Digite algo:".format(contador)))
    lista.append(n[nv]) 
    nv += 1
    contador = contador+1
lista_copia = lista.copy()
print(lista_copia)