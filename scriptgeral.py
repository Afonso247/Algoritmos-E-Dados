# Importar o big array do arquivo data.py
import plotly.graph_objects as go
from data import vendas as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])


# Análise geral do array

# -------- por Quantia Vendida --------
def findMediaQuantia_geral():
    media_armazenada = {}  # Dicionário para armazenar as médias

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes in filial:
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']
                quantidade_vendida = produto['quantidade_vendida']

                if filial_nome not in media_armazenada:
                    media_armazenada[filial_nome] = {}

                if tipo_produto not in media_armazenada[filial_nome]:
                    media_armazenada[filial_nome][tipo_produto] = []

                media_armazenada[filial_nome][tipo_produto].append(quantidade_vendida)

    for filial in media_armazenada:
        for tipo_produto in media_armazenada[filial]:
            media_armazenada[filial][tipo_produto] = round(
                sum(media_armazenada[filial][tipo_produto]) / 
                len(media_armazenada[filial][tipo_produto])
                , 0)
            
    estados = list(media_armazenada.keys())
    categorias = list(media_armazenada['PE'].keys())
    valores = [[media_armazenada[estado][categoria] for estado in estados] for categoria in categorias]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            name=categoria
        ))

    fig.update_layout(
        title='Média de quantidade vendida - Categorias e Filiais (Mês 1 - 6)',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
    )

    fig.show()

    return media_armazenada

def findTotalQuantia_geral():
    total_armazenado = {}  # Dicionário para armazenar os totais

    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes in market:
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']
                quantidade_vendida = produto['quantidade_vendida']

                if filial_nome not in total_armazenado:
                    total_armazenado[filial_nome] = {}

                if tipo_produto not in total_armazenado[filial_nome]:
                    total_armazenado[filial_nome][tipo_produto] = 0

                total_armazenado[filial_nome][tipo_produto] += quantidade_vendida
                
    estados = list(total_armazenado.keys())
    categorias = list(total_armazenado['PE'].keys())
    valores = [[total_armazenado[estado][categoria] for estado in estados] for categoria in categorias]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            name=categoria
        ))

    fig.update_layout(
        title='Total de quantidade vendida - Categorias e Filiais (Mês 1 - 6)',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
    )

    fig.show()

    return total_armazenado

    
# -------- por Renda Arrecadada --------
def findTotalRenda_geral():
    total_vendas = {}
    
    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        for mes in market:
            for venda in mes:
                
                produto = venda["tipo_do_produto"]
                quantidade = venda["quantidade_vendida"]
                preco = venda["preco_do_produto"]
                total = quantidade * preco
                total = round(total, 2)
                
                if filial_nome not in total_vendas:
                    total_vendas[filial_nome] = {}
                
                if produto in total_vendas:
                    total_vendas[filial_nome][produto] += total
                else:
                    total_vendas[filial_nome][produto] = total
                    
    estados = list(total_vendas.keys())
    categorias = list(total_vendas['PE'].keys())
    valores = [[total_vendas[estado][categoria] for estado in estados] for categoria in categorias]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            name=categoria
        ))

    fig.update_layout(
        title='Total de renda acumulada - Categorias e Filiais (Mês 1 - 6)',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
    )

    fig.show()
    
    return total_vendas
    
def findMediaRenda_geral():
    media_vendas = {}  # Dicionário para armazenar os resultados

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        for mes_index, mes in enumerate(filial):
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']
                preco_produto = produto['preco_do_produto']
                quantidade_vendida = produto['quantidade_vendida']

                # Se o tipo de produto não estiver no dicionário, crie uma entrada para ele
                if filial_nome not in media_vendas:
                    media_vendas[filial_nome] = {}
                
                if tipo_produto not in media_vendas[filial_nome]:
                    media_vendas[filial_nome][tipo_produto] = []

                media_vendas[filial_nome][tipo_produto].append(quantidade_vendida * preco_produto)
                
    for filial in media_vendas:
        for tipo_produto in media_vendas[filial]:
            media_vendas[filial][tipo_produto] = round(
                sum(media_vendas[filial][tipo_produto]) / 
                len(media_vendas[filial][tipo_produto])
                , 2)
            
    estados = list(media_vendas.keys())
    categorias = list(media_vendas['PE'].keys())
    valores = [[media_vendas[estado][categoria] for estado in estados] for categoria in categorias]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            name=categoria
        ))

    fig.update_layout(
        title='Média de renda acumulada - Categorias e Filiais (Mês 1 - 6)',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
    )

    fig.show()

    return media_vendas


    




# totalzinho = findTotalQuantia_geral()
# mediazinha = findTotalRenda_geral()
# what = findMediaQuantia_geral()
# whut = findMediaRenda_geral()

    
# Calculo da média
# total_col1 = round(sum(linha['quantidade_vendida'] for linha in al[0][0]), 2)
# media_col1 = round(sum(linha['quantidade_vendida'] for linha in al[0][0]) / len(al[0][0]), 2)
# total_col2 = round(sum(linha['quantidade_vendida'] for linha in al[0][1]), 2)
# media_col2 = round(sum(linha['quantidade_vendida'] for linha in al[0][1]) / len(al[0][1]), 2)

# print(f'Total de vendas em Janeiro: R${total_col1}')
# print(f'Média de vendas em Janeiro: R${media_col1}')
# print(f'Total de vendas em Fevereiro: R${total_col2}')
# print(f'Média de vendas em Fevereiro: R${media_col2}')

# print(mediazinha)
# print(whut)
