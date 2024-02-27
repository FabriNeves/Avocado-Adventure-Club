#continue, ignorar/pular

for numero in range(100):
    if numero % 2 ==0:
        print(numero)
    else:
        continue

    #break, para interromper a iteração

for numero in range(100):
    if numero % 2 == 0:
            print(numero)
    else:
        break


estilos = ["Hip-Hop", "Rock" , "Rap" , "Pop"]

for estilo in estilos:
    if estilo =="Rap":
        break
    print(estilo)