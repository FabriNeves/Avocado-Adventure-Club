from datetime import datetime


print(datetime.now())

print(datetime.now().year)


#Criar uma data  

dataCriada =  datetime(2024,12,2)

print(dataCriada)



# gerado pelo chatGPT
while True:
    data_de_lancamento = input("Qual o dia de lançamento do programa? (formato: YYYY/MM/DD): ")

    try:
        # Tenta converter a entrada para um objeto datetime
        data_formatada = datetime.strptime(data_de_lancamento, "%d/%m/%Y") # y maiusculo representa 4 digitos. 

        # Se a conversão for bem-sucedida, imprime a data formatada e encerra o loop
        print("Data de lançamento formatada:", data_formatada)

        dataCriada = data_formatada
        break

    except ValueError:
        # Se houver um erro ao converter, imprime uma mensagem de erro
        print("Formato inválido. Por favor, insira a data no formato correto (DD/MM/YYYY).")


dataAtual  = datetime.now()

prazo =  dataCriada - dataAtual

print(f'Prazo para entrega do programa é de : {prazo}' )
