nome_curso = 'Curso Python'


print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find("Curso"))
print(nome_curso.replace('Python' , 'Javascript'))
print(nome_curso.encode())

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

frase = f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}'


print(frase)