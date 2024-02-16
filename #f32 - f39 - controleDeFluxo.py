# Exemplos e conceitos das aulas f032 a f039

# Exemplo de idade
idade = 15

# Exemplo de comparação
print(idade > 17)  # False

# Comentários sobre comparadores
"""
> maior 
< menor
<= menor ou igual 
>= maior ou igual 
== igual a 
!= diferente de 
"""

# Exemplo de comparação de strings
print("Rafael" == "rafael")  # False

# Exemplo de uso de True e False
# True , False   => Sempre com letra maiuscula 
print(5 == "5")  # False

# Exemplo de uso de "is"
c = 10
d = 10
print(c == d)  # True
print(c is d)  # True (mesmo objeto na memória)

# Comentário sobre o "is"
"""
is compara a identidade 
Qual é a referencia dentro da memoria do computador que cada item está preenchendo ,
dependendo do ambiente de execução podem ter resultados diferentes.
"""

print(c is None)  # False (c não é None)

# Exemplo de conversão de tipos
anos = "18"
print(int(anos) > 18)  # False (pois 18 não é maior que 18)

# Exemplo de uso da função type()
print(type(str(5)))  # <class 'str'> (exemplo de conversão para string)

e = "2.10"
print(float(e))  # 2.1 (exemplo de conversão para float)

# Exemplo de estruturas de controle
numero1 = 89
numero2 = 32
numero3 = 12

numero = int(input("Digite um número: "))

if numero == numero1:
    print(f"O número digitado é igual a {numero1}.")
elif numero == numero2:
    print(f"O número digitado é igual a {numero2}.")
elif numero == numero3:
    print(f"O número digitado é igual a {numero3}.")
elif numero < numero3:
    print(f"O número digitado é menor que {numero3}.")
elif numero3 < numero < numero2:
    print(f"O número digitado está entre {numero3} e {numero2}.")
elif numero > numero2:
    print(f"O número digitado é maior que {numero2}.")
elif numero3 < numero < numero1:
    print(f"O número digitado é maior que {numero3} e menor que {numero1}.")
elif numero > numero1:
    print(f"O número digitado é maior que {numero1}.")
else:
    print("O número digitado não corresponde a nenhum dos números fornecidos.")
