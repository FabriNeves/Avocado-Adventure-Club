# Como tratar erros  
try:
    valor = int(input('Digite o valor em dolares'))
    print(valor * 5.25)
except:
    print('Formato Inválido.')