
def gerar_nome_completo(firstname,secondname):
    print(f'Bem-vindo {firstname} {secondname}')

nome = []

nome.append(input("Qual nome da pessoa ?"))

nome.append(input("Qual o sobrenome ?"))

gerar_nome_completo(nome[0],nome[1])


