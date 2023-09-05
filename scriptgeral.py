# Importar o big array do arquivo data.py
import plotly.graph_objects as go
from data import vendas as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])


# 10mil funções sobre a análise do array por Tipo de Produto

# -------- por Quantia Vendida --------
def findTotalQuantia_geral(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    total_armazenado = {}  # Dicionário para armazenar os totais
    cores = {'PE': 'blue', 'PB': 'green', 'CE': 'red'}

    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes_index, mes in enumerate(market):
            # Verifica se o mês está dentro do intervalo desejado
            if mes_inicial <= mes_index < mes_final:
                for produto in mes:
                    quantidade_vendida = produto['quantidade_vendida']

                    if filial_nome not in total_armazenado:
                        total_armazenado[filial_nome] = 0

                    total_armazenado[filial_nome] += quantidade_vendida
                
    estados = list(total_armazenado.keys())
    valores = [total_armazenado[estado] for estado in estados]
    cores_filiais = [cores[estado] for estado in estados]
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=estados,
        y=valores,
        marker_color=cores_filiais,
        name='Total de Quantidade Vendida'
    ))
    
    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Total de quantidade vendida - Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Total de quantidade vendida - Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )

    fig.show()

    return total_armazenado

def findMediaQuantia_geral(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    media_armazenada = {}  # Dicionário para armazenar as médias
    cores = {'PE': 'blue', 'PB': 'green', 'CE': 'red'}

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes_index, mes in enumerate(filial):
            if mes_inicial <= mes_index < mes_final:
                for produto in mes:
                    quantidade_vendida = produto['quantidade_vendida']

                    if filial_nome not in media_armazenada:
                        media_armazenada[filial_nome] = {}

                    if 'Total' not in media_armazenada[filial_nome]:
                        media_armazenada[filial_nome]['Total'] = []

                    media_armazenada[filial_nome]['Total'].append(quantidade_vendida)

    for filial in media_armazenada:
        for total in media_armazenada[filial]:
            media_armazenada[filial][total] = round(
                sum(media_armazenada[filial][total]) / 
                len(media_armazenada[filial][total])
                , 0)
            
    estados = list(media_armazenada.keys())
    categorias = list(media_armazenada['PE'].keys())
    valores = [[media_armazenada[estado][categoria] for estado in estados] for categoria in categorias]
    cores_filiais = [cores[estado] for estado in estados]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            marker_color=cores_filiais,
            name=categoria
        ))

    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Média de quantidade vendida - Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Média de quantidade vendida - Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )

    fig.show()

    return media_armazenada

    
# -------- por Renda Arrecadada --------
def findTotalRenda_geral(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    total_vendas = {}
    cores = {'PE': 'blue', 'PB': 'green', 'CE': 'red'}
    
    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        total_filial = 0  # Inicializa o total da filial
        
        for mes_index, mes in enumerate(market):
            # Verifica se o mês está dentro do intervalo desejado
            if mes_inicial <= mes_index < mes_final:
                for venda in mes:
                    quantidade = venda["quantidade_vendida"]
                    preco = venda["preco_do_produto"]
                    total = quantidade * preco
                    total = round(total, 2)
                    total_filial += total  # Acumula o total da filial
        
        if filial_nome not in total_vendas:
            total_vendas[filial_nome] = {}
        
        total_vendas[filial_nome]['Total'] = total_filial  # Armazena o total da filial
    
    estados = list(total_vendas.keys())
    valores = [total_vendas[estado]['Total'] for estado in estados]
    cores_filiais = [cores[estado] for estado in estados]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=estados,
        y=valores,
        marker_color=cores_filiais,
        name='Total'
    ))
    
    if mes_final == mes_inicial + 1:
        fig.update_layout(
            title=f'Total de renda acumulada - Filiais (Mês {mes_inicial + 1})',
            xaxis=dict(title='Filiais'),
            yaxis=dict(title='Renda Acumulada (R$)'),
            barmode='group'
        )
    else:
        fig.update_layout(
            title=f'Total de renda acumulada - Filiais (Mês {mes_inicial + 1} até {mes_final})',
            xaxis=dict(title='Filiais'),
            yaxis=dict(title='Renda Acumulada (R$)'),
            barmode='group'
        )

    fig.show()
    
    return total_vendas

def findMediaRenda_geral(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    media_vendas = {}  # Dicionário para armazenar os resultados
    cores = {'PE': 'blue', 'PB': 'green', 'CE': 'red'}

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        for mes_index, mes in enumerate(filial):
            if mes_inicial <= mes_index < mes_final:
                for produto in mes:
                    preco_produto = produto['preco_do_produto']
                    quantidade_vendida = produto['quantidade_vendida']

                    # Se o tipo de produto não estiver no dicionário, crie uma entrada para ele
                    if filial_nome not in media_vendas:
                        media_vendas[filial_nome] = {}
                    
                    if 'Total' not in media_vendas[filial_nome]:
                        media_vendas[filial_nome]['Total'] = []

                    media_vendas[filial_nome]['Total'].append(quantidade_vendida * preco_produto)
                
    for filial in media_vendas:
        for tipo_produto in media_vendas[filial]:
            media_vendas[filial][tipo_produto] = round(
                sum(media_vendas[filial][tipo_produto]) / 
                len(media_vendas[filial][tipo_produto])
                , 2)
            
    estados = list(media_vendas.keys())
    categorias = list(media_vendas['PE'].keys())
    valores = [[media_vendas[estado][categoria] for estado in estados] for categoria in categorias]
    cores_filiais = [cores[estado] for estado in estados]
    
    fig = go.Figure()

    for i, categoria in enumerate(categorias):
        fig.add_trace(go.Bar(
            x=estados,
            y=valores[i],
            marker_color=cores_filiais,
            name=categoria
        ))

    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Média de renda acumulada - Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Média de renda acumulada - Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )

    fig.show()

    return media_vendas





# totalzinho = findTotalQuantia_geral(0,1)
# print(totalzinho)
# totalzao = findTotalRenda_geral(0,1)
# print(totalzao)
# mediazinha = findMediaQuantia_geral(0,1)
# print(mediazinha)
# mediazao = findMediaRenda_geral(0,1)
# print(mediazao)
