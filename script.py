# Importar o big array do arquivo data.py
from datatemp import vendas as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])


# 10mil funções sobre a análise do array por Tipo de Produto

# -------- por Quantia Vendida --------
def findMediaQuantia_geral():
    # Dicionário para armazenar os preços de cada tipo de produto
    valores_por_produto = {}

    # Loop sobre a primeira dimensão (rede de supermercados)
    for market in al:
        # Loop sobre a segunda dimensão (meses de registros)
        for mes in market:
            # Loop sobre a terceira dimensão (informações dos produtos)
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']
                valor = produto['quantidade_vendida']

                # Se o tipo do produto não estiver no dicionário, crie uma lista vazia
                if tipo_produto not in valores_por_produto:
                    valores_por_produto[tipo_produto] = []

                # Adicione o preço à lista de preços para esse tipo de produto
                valores_por_produto[tipo_produto].append(valor)

    # Calcule a média de preço para cada tipo de produto e imprima
    for tipo_produto, lista_valores in valores_por_produto.items():
        media_valor = sum(lista_valores) / len(lista_valores)
        print(f'Média de quantia vendida para {tipo_produto}: {media_valor:.2f}')
        
    return "Fim!"

def findTotalQuantia_geral():
    # Dicionário para armazenar os preços de cada tipo de produto
    valores_por_produto = {}

    # Loop sobre a primeira dimensão (rede de supermercados)
    for market in al:
        # Loop sobre a segunda dimensão (meses de registros)
        for mes in market:
            # Loop sobre a terceira dimensão (informações dos produtos)
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']
                valor = produto['quantidade_vendida']

                # Atualiza o valor total do tipo de produto no dicionário
                if tipo_produto in valores_por_produto:
                    valores_por_produto[tipo_produto] += valor
                else:
                    valores_por_produto[tipo_produto] = valor

    # Calcule a média de preço para cada tipo de produto e imprima
    for tipo_produto, total_valores in valores_por_produto.items():
        print(f'Total de quantia vendida para {tipo_produto}: {total_valores:.2f}')
        
    return "Fim!"

    
# -------- por Renda Arrecadada --------
def findTotalRenda_geral():
    total_vendas = {}
    
    for market in al:
        for mes in market:
            for venda in mes:
                produto = venda["tipo_do_produto"]
                quantidade = venda["quantidade_vendida"]
                preco = venda["preco_do_produto"]
                total = quantidade * preco
                if produto in total_vendas:
                    total_vendas[produto] += total
                else:
                    total_vendas[produto] = total
                    
    for produto, total in total_vendas.items():
        print(f"Total de Renda arrecadada para {produto}: R${total:.2f}")
        
    return "Fim!"
    
def findMediaRenda_geral():
    total_renda = {}  # Um dicionário para armazenar os resultados


    for market in al:
        for mes in market:
            for produto in mes:
                tipo_produto = produto['tipo_do_produto'] 
                quantidade_vendida = produto['quantidade_vendida'] 
                preco = produto['preco_do_produto']  

                # Calcula o total vendido para este produto neste mês
                total_vendido = quantidade_vendida * preco

                # Atualiza o resultado para este produto
                if tipo_produto in total_renda:
                    total_renda[tipo_produto].append(total_vendido)
                else:
                    total_renda[tipo_produto] = [total_vendido]

    # Calcula a média para cada produto
    for produto, vendas in total_renda.items():
        media = sum(vendas) / len(vendas)
        print(f'Média de Renda arrecadada para {produto}: R${media:.2f}')
        
    return "Fim!"
    




totalzinho = findTotalQuantia_geral()
mediazinha = findTotalRenda_geral()
what = findMediaQuantia_geral()
whut = findMediaRenda_geral()

    
# Calculo da média
total_col1 = round(sum(linha['quantidade_vendida'] for linha in al[0][0]), 2)
media_col1 = round(sum(linha['quantidade_vendida'] for linha in al[0][0]) / len(al[0][0]), 2)
total_col2 = round(sum(linha['quantidade_vendida'] for linha in al[0][1]), 2)
media_col2 = round(sum(linha['quantidade_vendida'] for linha in al[0][1]) / len(al[0][1]), 2)
# media_col3 = sum(linha['preco_do_produto'] for linha in al[0][2]) / len(al[0][2])

# print(f'Total de vendas em Janeiro: R${total_col1}')
# print(f'Média de vendas em Janeiro: R${media_col1}')
# print(f'Total de vendas em Fevereiro: R${total_col2}')
# print(f'Média de vendas em Fevereiro: R${media_col2}')
# print(f'Média da coluna 3: {media_col3}')

# print(mediazinha)
# print(totalzinho)

