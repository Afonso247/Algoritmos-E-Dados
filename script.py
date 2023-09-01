# Importar o big array do arquivo data.py
import tkinter as tk
from datatemp import vendas as al

# [número do supermercado], [número do mês], [número do produto]
# print(al[0][1][2]['data_de_compra'].day)
# print(al[0][0][0]['nome_do_produto'])


# 10mil funções sobre a análise do array por Tipo de Produto

# -------- por Quantia Vendida --------
def findMediaQuantia_geral():
    # Dicionário para armazenar o resultado para cada tipo de produto
    resultado = {}
    
    # Iterar sobre o array tridimensional
    for market in al:
        for mes in market:
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']  # Suponhamos que 'nome' é a chave que armazena o nome do produto
                quantidade_vendida = produto['quantidade_vendida']  # Suponhamos que 'quantidade' é a chave que armazena a quantidade vendida
                preco = produto['preco_do_produto']  # Suponhamos que 'valor' é a chave que armazena o valor unitário
                
                # Atualizar o resultado para o tipo de produto atual
                if tipo_produto in resultado:
                    resultado[tipo_produto]['total'] += quantidade_vendida
                    resultado[tipo_produto]['count'] += 1
                else:
                    resultado[tipo_produto] = {'total': quantidade_vendida, 'count': 1}
    
    # Calcular a média para cada tipo de produto
    for tipo_produto, total in resultado.items():
        resultado[tipo_produto]['media'] = total['total'] / total['count']
        
    janela = tk.Tk()
    janela.title("Média de Vendas por Produto")
    
    # Criar um rótulo para cada tipo de produto e sua média
    for produto, total in resultado.items():
        label = tk.Label(janela, text=f"Produto {produto}: Média de {total['media']:.0f} unidades vendidas")
        label.pack()
    
    janela.mainloop()
    
    return "Fim!"

def findTotalQuantia_geral():
    # Dicionário para armazenar o total de vendas de cada produto
    valores_por_produto = {}

    # Itere sobre a rede de supermercados
    for market in al:
        # Itere sobre os meses
        for mes in market:
            # Itere sobre as informações de produto em cada lista
            for produto in mes:
                # Obtenha o nome do produto e a quantidade vendida
                nome_produto = produto['tipo_do_produto']
                quantidade_vendida = produto['quantidade_vendida']

                # Atualize o total de vendas para o produto
                if nome_produto in valores_por_produto:
                    valores_por_produto[nome_produto] += quantidade_vendida
                else:
                    valores_por_produto[nome_produto] = quantidade_vendida
                          
    # Crie uma janela tkinter
    janela = tk.Tk()
    janela.title("Total de Vendas por Produto")

    # Crie e exiba rótulos para cada produto e seu total de vendas
    for produto, total in valores_por_produto.items():
        label = tk.Label(janela, text=f"Produto {produto}: Total de {total} unidades vendidas")
        label.pack()

    # Inicie o loop de eventos da interface gráfica
    janela.mainloop()

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
                    
    # Crie uma janela Tkinter
    janela = tk.Tk()
    janela.title("Relatório de Vendas")

    # Crie um rótulo para cada produto e seu total de vendas
    for produto, total in total_vendas.items():
        label = tk.Label(janela, text=f"Produto {produto}: Total de Renda: R${total:.2f}")
        label.pack()

    # Inicie o loop de eventos da interface gráfica
    janela.mainloop()
    return "Fim!"
    
def findMediaRenda_geral():
    # Dicionário para armazenar o resultado para cada tipo de produto
    resultado = {}
    
    # Iterar sobre o array tridimensional
    for market in al:
        for mes in market:
            for produto in mes:
                tipo_produto = produto['tipo_do_produto']  # Suponhamos que 'nome' é a chave que armazena o nome do produto
                quantidade_vendida = produto['quantidade_vendida']  # Suponhamos que 'quantidade' é a chave que armazena a quantidade vendida
                preco = produto['preco_do_produto']  # Suponhamos que 'valor' é a chave que armazena o valor unitário
                
                # Atualizar o resultado para o tipo de produto atual
                if tipo_produto in resultado:
                    resultado[tipo_produto]['total'] += quantidade_vendida * preco
                    resultado[tipo_produto]['count'] += 1
                else:
                    resultado[tipo_produto] = {'total': quantidade_vendida * preco, 'count': 1}
    
    # Calcular a média para cada tipo de produto
    for tipo_produto, total in resultado.items():
        resultado[tipo_produto]['media'] = total['total'] / total['count']
        
    janela = tk.Tk()
    janela.title("Média de Vendas por Produto")
    
    # Criar um rótulo para cada tipo de produto e sua média
    for produto, total in resultado.items():
        label = tk.Label(janela, text=f"Produto {produto}: Média de Renda: R${total['media']:.2f}")
        label.pack()
    
    janela.mainloop()
    
    return "Fim!"




# totalzinho = findMediaQuantia_geral()
# mediazinha = findTotalRenda_geral()
# what = findMediaQuantia_geral()
# whut = findMediaRenda_geral()

    
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
