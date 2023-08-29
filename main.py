# Importar o big array do arquivo data.py
from data import arrayList as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])

for linha in al[0][0]:
    print(linha['preco_do_produto'])
for linha in al[0][1]:
    print(linha['preco_do_produto'])
    
# Calculo da média
media_col1 = round(sum(linha['preco_do_produto'] for linha in al[0][0]) / len(al[0][0]), 2)
media_col2 = round(sum(linha['preco_do_produto'] for linha in al[0][1]) / len(al[0][1]), 2)
# media_col3 = sum(linha['preco_do_produto'] for linha in al[0][2]) / len(al[0][2])

print(f'Média da coluna 1: {media_col1}')
print(f'Média da coluna 2: {media_col2}')
# print(f'Média da coluna 3: {media_col3}')

