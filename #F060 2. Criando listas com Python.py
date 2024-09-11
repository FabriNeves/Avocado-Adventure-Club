valores = [1,2 ,3 ,4 ,2,5,6,7,9,10]


anos = [2020,2030,2024,2050]

valores.append(11)

print(valores)

valores.extend(anos)

print(valores)


nova_lista = valores + anos 

print(nova_lista)