#Arquivo JSON 

import json 
from pathlib import Path
carros = [ 
    {"Marca":"Nissan","Preço":45.000,"Cor":"Azul"},
    {"Marca":"Ford","Preço":75.000,"Cor":"Verde"},
    {"Marca":"BMW","Preço":117.000,"Cor":"Amarelo"}
]


carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json) 

arquivos_carros_json = Path('carros.json').read_text()
arquivos_carro = json.loads(arquivos_carros_json)

print(arquivos_carro[0]['Marca']+' '+str(arquivos_carro[0]['Preço']))
print(arquivos_carro[1]['Marca']+' '+str(arquivos_carro[1]['Preço']))


arquivo_pikachu_json = Path('pikachu.json').read_text()

arquivo_pikachu = json.loads(arquivo_pikachu_json)

print(arquivo_pikachu[0]['abilities'][1]['ability']['name'])