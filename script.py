# Importar o big array do arquivo data.py
import plotly.graph_objects as go
from data import vendas as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])


# 10mil funções sobre a análise do array por Tipo de Produto

# -------- por Quantia Vendida --------
def findTotalQuantia_porMes(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    total_armazenado = {}  # Dicionário para armazenar os totais

    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes_index, mes in enumerate(market):
            # Verifica se o mês está dentro do intervalo desejado
            if mes_inicial <= mes_index < mes_final:
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
        
    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Total de quantidade vendida - Categorias e Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Total de quantidade vendida - Categorias e Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )

    fig.show()

    return total_armazenado

def findMediaQuantia_porMes(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    media_armazenada = {}  # Dicionário para armazenar as médias

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]

        for mes_index, mes in enumerate(filial):
            if mes_inicial <= mes_index < mes_final:
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

    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Média de quantidade vendida - Categorias e Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Média de quantidade vendida - Categorias e Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Quantidade Vendida'),
        barmode='group'
        )

    fig.show()

    return media_armazenada

    
# -------- por Renda Arrecadada --------
def findTotalRenda_porMes(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    total_vendas = {}
    
    for filial_index, market in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        for mes_index, mes in enumerate(market):
            # Verifica se o mês está dentro do intervalo desejado
            if mes_inicial <= mes_index < mes_final:
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
        
    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Total de renda acumulada - Categorias e Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Total de renda acumulada - Categorias e Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )

    fig.show()
    
    return total_vendas

def findMediaRenda_porMes(mes_inicial, mes_final):
    if mes_inicial >= mes_final:
        raise ValueError("O mês inicial deve ser menor que o mês final.")
    
    media_vendas = {}  # Dicionário para armazenar os resultados

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        
        for mes_index, mes in enumerate(filial):
            if mes_inicial <= mes_index < mes_final:
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

    if(mes_final == mes_inicial+1):
        fig.update_layout(
        title=f'Média de renda acumulada - Categorias e Filiais (Mês {mes_inicial + 1})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )
    else:
        fig.update_layout(
        title=f'Média de renda acumulada - Categorias e Filiais (Mês {mes_inicial + 1} até {mes_final})',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Renda Acumulada (R$)'),
        barmode='group'
        )

    fig.show()

    return media_vendas

def findFilialMaiorFaturamento():
    total_vendas = {}  # Dicionário para armazenar os resultados

    for filial_index, filial in enumerate(al):
        filial_nome = ["PE", "PB", "CE"][filial_index]
        filial_total_vendas = 0  # Inicializa o total de vendas da filial

        for mes_index, mes in enumerate(filial):
            for produto in mes:
                preco_produto = produto['preco_do_produto']
                quantidade_vendida = produto['quantidade_vendida']

                # Calcula o total de vendas da filial para o mês
                total_mes = quantidade_vendida * preco_produto
                filial_total_vendas += total_mes

        # Calcula a média de vendas da filial e arredonda para 2 casas decimais
        total_vendas[filial_nome] = round(filial_total_vendas / (mes_index + 1), 2)
                
    estados = list(total_vendas.keys())
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=estados,
        y=list(total_vendas.values()),
        name='Média de Valores'
    ))

    fig.update_layout(
        title='Filial com Maior Faturamento (Mês 1 - 6)',
        xaxis=dict(title='Filiais'),
        yaxis=dict(title='Média de Valores (R$)'),
        barmode='group'
    )

    fig.show()

    return total_vendas





# totalzinho = findTotalQuantia_porMes(0,6)
# print(totalzinho)
# totalzao = findTotalRenda_porMes(1,4)
# print(totalzao)
# mediazinha = findMediaQuantia_porMes(0,4)
# print(mediazinha)
# mediazao = findMediaRenda_porMes(1,4)
# print(mediazao)

