# Definindo os nomes das filiais, meses e tipos de produtos
filiais = ['PE', 'PB', 'CE']
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul']
tipos_de_produtos = ['hortifruit', 'bebidas', 'lacticinios']

# Criando o array tridimensional com valores
vendas = [
    # Filial PE
    [
        # Janeiro
            # hortifruit, bebidas, e lacticinios, nesta ordem
        [
            {
                'ID': 0,
                'tipo_do_produto': "hortifruit",
                'quantidade_vendida': 1250,
                'valor_total': 15000
            },
            {
                'ID': 1,
                'tipo_do_produto': "bebidas",
                'quantidade_vendida': 1020,
                'valor_total': 10000
            },
            {
                'ID': 2,
                'tipo_do_produto': "lacticinios",
                'quantidade_vendida': 1450,
                'valor_total': 12000
            }
        ],
        # Fevereiro
        [
            {
                'ID': 3,
                'tipo_do_produto': "hortifruit",
                'quantidade_vendida': 1190,
                'valor_total': 13000
            },
            {
                'ID': 4,
                'tipo_do_produto': "bebidas",
                'quantidade_vendida': 1000,
                'valor_total': 11000
            },
            {
                'ID': 5,
                'tipo_do_produto': "lacticinios",
                'quantidade_vendida': 960,
                'valor_total': 11500
            }
        ],
        # Março
        [
            {
                'ID': 6,
                'tipo_do_produto': "hortifruit",
                'quantidade_vendida': 1300,
                'valor_total': 16000
            },
            {
                'ID': 7,
                'tipo_do_produto': "bebidas",
                'quantidade_vendida': 1080,
                'valor_total': 10500
            },
            {
                'ID': 8,
                'tipo_do_produto': "lacticinios",
                'quantidade_vendida': 1420,
                'valor_total': 12500
            }
        ],
        # Abril
        [14000, 12000, 13000],
        # Maio
        [15500, 11500, 12800],
        # Junho
        [14500, 10500, 13200]
    ],

    # Filial PB
    [
        # Janeiro
        [12000, 9500, 11000],
        # Fevereiro
        [11000, 9000, 10500],
        # Março
        [12500, 10000, 12000],
        # Abril
        [13000, 10500, 12500],
        # Maio
        [11500, 9500, 11500],
        # Junho
        [11800, 9200, 11000]
    ],

    # Filial CE
    [
        # Janeiro
        [17000, 13000, 14000],
        # Fevereiro
        [18000, 13500, 15000],
        # Março
        [16000, 12500, 13500],
        # Abril
        [17500, 13000, 14200],
        # Maio
        [16500, 12800, 13800],
        # Junho
        [16800, 13200, 14200]
    ]
]
