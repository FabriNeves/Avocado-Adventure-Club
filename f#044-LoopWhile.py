#Contador de 0 a 120 

count1 = 0

while count1 <=119:
    print(count1)
    count1 +=1 

#Contador decrescente de 120 a 0
    

while count1 >=0:
    print(count1)
    count1 -=1 



tentativas = 0 

Senha = "ABX942"

verificaSenha  = False

while (tentativas < 10 and not verificaSenha):    
    print(f'Você tem {10-tentativas} tentativas restantes')
    senha_digitada = input("Digite sua senha... ")
    verificaSenha =  senha_digitada == Senha
    print(verificaSenha)
    tentativas += 1
    

if(verificaSenha):
    print("Bem vindo!")
else:
    print("Tente Outro dia!")