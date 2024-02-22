nomes = ["Ana", "João", "Maria", "Pedro", "Lúcia"]

for n in nomes:
    print(n)


for numero in range(1,21,2):
    print(numero)


# Usando enumerate para obter o índice e o valor de cada elemento na lista de nomes
for indice, nome in enumerate(nomes):
    print(f"O nome na posição {indice} é {nome}")
    
"""
enumerate(nomes): A função enumerate() cria um iterador que gera tuplas contendo o índice 
e o valor correspondente de cada elemento na lista nomes.

for indice, nome in enumerate(nomes): Um loop for é utilizado para iterar sobre cada tupla retornada pela
 função enumerate(). As tuplas são desempacotadas nas variáveis indice e nome.

print(f"O nome na posição {indice} é {nome}"): Dentro do loop,
 essa linha imprime uma mensagem formatada, utilizando o índice indice e o valor nome de cada elemento na lista nomes.

"""