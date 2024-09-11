from datetime import datetime
import time

def depositar_dinheiro():
    print('depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Depositando reais')

    depositando_dolar()
    depositando_reais()


depositar_dinheiro()

def pai(numero):
    
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero ==1:
        return filho_1
    

resultado = pai(1)
resultado()

#Decorators 

def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

def parabenizar():
    print('Parabens!!!!!')

resultado = meu_decorator(parabenizar)
resultado()

#Desafio 1 




def print_hora_atual():
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    print("Data atual:", data_formatada)





def soma_registro(funcHora):

    a = int(input("Primeiro tempo de delay :"))
    b = int(input("Segundo tempo de delay :"))
    print('Inicio da tarefa ')
    funcHora()
    print(f'Delay de {a+b} segundos')
    time.sleep(a+b)
    print('Fim da tarefa ')
    funcHora()

soma_registro(print_hora_atual)