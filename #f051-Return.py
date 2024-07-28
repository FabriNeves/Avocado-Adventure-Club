
def exibir_preco(nome_produto, preco) :
    print(f'{nome_produto} está no valor de: {preco}')

# Argumentos posicionais
exibir_preco( 'IPhone' ,5000)
exibir_preco(nome_produto = 'IPhone' , preco=5000)