# Definindo os nomes das filiais, meses e tipos de produtos
filiais = ['PE', 'PB', 'CE']
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']
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
                'preco_do_produto': 10.99,
                'quantidade_vendida': 130
            },
            {
                'ID': 1,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1020
            },
            {
                'ID': 2,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1450
                
            }
        ],
        # Fevereiro
        [
            {
                'ID': 3,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1190
            },
            {
                'ID': 4,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 5,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 960
            }
        ],
        # Março
        [
            {
                'ID': 6,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1300
            },
            {
                'ID': 7,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1080
            },
            {
                'ID': 8,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1420
            }
        ],
        # Abril
        [
            {
                'ID': 9,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 10,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 11,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 450
            }
        ],
        # Maio
        [ 
            {
                'ID': 12,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 500
            },
            {
                'ID': 13,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 930
            },
            {
                'ID': 14,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 350
            }
        ],
        # Junho
        [   
            {
                'ID': 15,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1100
            },
            {
                'ID': 16,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1005
            },
            {
                'ID': 17,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 500
            }
        ]
    ],

    # Filial PB
    [
        # Janeiro
        [
            {
                'ID': 18,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 19,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 20,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 450
            }            
        ],
        # Fevereiro
        [
            {
                'ID': 21,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1130
            },
            {
                'ID': 22,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1020
            },
            {
                'ID': 23,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 550
            }
        ],
        # Março
        [
            {
                'ID': 24,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 25,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1200
            },
            {
                'ID': 26,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 700
            }
        ],
        # Abril
        [
            {
                'ID': 27,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1350
            },
            {
                'ID': 28,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1530
            },
            {
                'ID': 29,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 850
            }
        ],
        # Maio
        [
            {
                'ID': 30,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1200
            },
            {
                'ID': 31,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1040
            },
            {
                'ID': 32,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 750
            }
        ],
        # Junho
        [
            {
                'ID': 33,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1500
            },
            {
                'ID': 34,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 990
            },
            {
                'ID': 35,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 550
            }
        ]
    ],

    # Filial CE
    [
        # Janeiro
        [
            {
                'ID': 36,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1150
            },
            {
                'ID': 37,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1005
            },
            {
                'ID': 38,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 850
            }
        ],
        # Fevereiro
        [
            {
                'ID': 39,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1250
            },
            {
                'ID': 40,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1055
            },
            {
                'ID': 41,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 367
            }
        ],
        # Março
        [
            {
                'ID': 42,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 43,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 920
            },
            {
                'ID': 44,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 720
            }
        ],
        # Abril
        [
            {
                'ID': 45,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1350
            },
            {
                'ID': 46,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1130
            },
            {
                'ID': 47,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 780
            }
        ],
        # Maio
        [
            {
                'ID': 48,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1230
            },
            {
                'ID': 49,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1510
            },
            {
                'ID': 50,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 900
            }
        ],
        # Junho
        [
            {
                'ID': 51,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 52,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 53,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 650
            }
        ]
    ]
]
