# Definindo os nomes das filiais, meses e tipos de produtos
filiais = ['PE', 'PB', 'CE']
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul']
tipos_de_produtos = ['hortfruit', 'bebidas', 'lacticinios']

# Criando o array tridimensional com valores
vendas = [
    # Filial PE
    [
        # Janeiro
        [15000, 10000, 12000],  # hortfruit, bebidas, lacticinios
        # Fevereiro
        [13000, 11000, 11500],
        # Março
        [16000, 10500, 12500],
        # Abril
        [14000, 12000, 13000],
        # Maio
        [15500, 11500, 12800],
        # Junho
        [14500, 10500, 13200],
        # Julho
        [15000, 10000, 12000]
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
        [11800, 9200, 11000],
        # Julho
        [12000, 9800, 11200]
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
        [16800, 13200, 14200],
        # Julho
        [17000, 13000, 14100]
    ]
]