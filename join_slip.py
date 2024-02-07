

frase1 = "Desafio manipulação de strings"
frase2 = "Fabricio,Carol,Rafael,Camilla"

palavras1 = frase1.split()

palavras2 = frase2.split(",")

print(palavras2)

palavras1 = ",".join(palavras1)
palavras2 = "&".join(palavras2)


print(palavras1,palavras2)
