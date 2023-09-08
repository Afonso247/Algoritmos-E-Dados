# Definindo os nomes das filiais, meses e tipos de produtos
filiais = ['PE', 'PB', 'CE']
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
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
        ],
        # Julho
        [   
            {
                'ID': 18,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1520
            },
            {
                'ID': 19,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1105
            },
            {
                'ID': 20,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 980
            }
        ],
        # Agosto
        [   
            {
                'ID': 21,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1200
            },
            {
                'ID': 22,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1650
            },
            {
                'ID': 23,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ],
        # Setembro
        [   
            {
                'ID': 24,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1300
            },
            {
                'ID': 25,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1105
            },
            {
                'ID': 26,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 800
            }
        ],
        # Outubro
        [   
            {
                'ID': 27,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 28,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1205
            },
            {
                'ID': 29,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 984
            }
        ],
        # Novembro
        [   
            {
                'ID': 30,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1110
            },
            {
                'ID': 31,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1055
            },
            {
                'ID': 32,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 908
            }
        ],
        # Dezembro
        [   
            {
                'ID': 33,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1400
            },
            {
                'ID': 34,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1205
            },
            {
                'ID': 35,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1500
            }
        ]
    ],

    # Filial PB
    [
        # Janeiro
        [
            {
                'ID': 36,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 37,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 38,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 450
            }            
        ],
        # Fevereiro
        [
            {
                'ID': 39,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1130
            },
            {
                'ID': 40,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1020
            },
            {
                'ID': 41,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 550
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
                'quantidade_vendida': 1200
            },
            {
                'ID': 44,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 700
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
                'quantidade_vendida': 1530
            },
            {
                'ID': 47,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 850
            }
        ],
        # Maio
        [
            {
                'ID': 48,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1200
            },
            {
                'ID': 49,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1040
            },
            {
                'ID': 50,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 750
            }
        ],
        # Junho
        [
            {
                'ID': 51,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1500
            },
            {
                'ID': 52,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 990
            },
            {
                'ID': 53,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 550
            }
        ],
        # Julho
        [   
            {
                'ID': 54,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1350
            },
            {
                'ID': 55,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1515
            },
            {
                'ID': 56,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 750
            }
        ],
        # Agosto
        [   
            {
                'ID': 57,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1300
            },
            {
                'ID': 58,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1205
            },
            {
                'ID': 59,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ],
        # Setembro
        [   
            {
                'ID': 60,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1150
            },
            {
                'ID': 61,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 985
            },
            {
                'ID': 62,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 800
            }
        ],
        # Outubro
        [   
            {
                'ID': 63,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1500
            },
            {
                'ID': 64,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1305
            },
            {
                'ID': 65,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ],
        # Novembro
        [   
            {
                'ID': 66,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1250
            },
            {
                'ID': 67,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1025
            },
            {
                'ID': 68,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 950
            }
        ],
        # Dezembro
        [   
            {
                'ID': 69,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1300
            },
            {
                'ID': 70,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1105
            },
            {
                'ID': 71,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ]
    ],

    # Filial CE
    [
        # Janeiro
        [
            {
                'ID': 72,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1150
            },
            {
                'ID': 73,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1005
            },
            {
                'ID': 74,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 850
            }
        ],
        # Fevereiro
        [
            {
                'ID': 75,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1250
            },
            {
                'ID': 76,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1055
            },
            {
                'ID': 77,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 367
            }
        ],
        # Março
        [
            {
                'ID': 78,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 79,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 920
            },
            {
                'ID': 80,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 720
            }
        ],
        # Abril
        [
            {
                'ID': 81,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1350
            },
            {
                'ID': 82,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1130
            },
            {
                'ID': 83,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 780
            }
        ],
        # Maio
        [
            {
                'ID': 84,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1230
            },
            {
                'ID': 85,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1510
            },
            {
                'ID': 86,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 900
            }
        ],
        # Junho
        [
            {
                'ID': 87,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 88,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 89,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 650
            }
        ],
        # Julho
        [   
            {
                'ID': 90,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1150
            },
            {
                'ID': 91,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1105
            },
            {
                'ID': 92,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 850
            }
        ],
        # Agosto
        [   
            {
                'ID': 93,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1200
            },
            {
                'ID': 94,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 905
            },
            {
                'ID': 95,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 750
            }
        ],
        # Setembro
        [   
            {
                'ID': 96,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1500
            },
            {
                'ID': 97,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1255
            },
            {
                'ID': 98,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ],
        # Outubro
        [   
            {
                'ID': 99,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 100,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1000
            },
            {
                'ID': 101,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1000
            }
        ],
        # Novembro
        [   
            {
                'ID': 102,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1150
            },
            {
                'ID': 103,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1050
            },
            {
                'ID': 104,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 630
            }
        ],
        # Dezembro
        [   
            {
                'ID': 105,
                'tipo_do_produto': "hortifruit",
                'preco_do_produto': 10.99,
                'quantidade_vendida': 1500
            },
            {
                'ID': 106,
                'tipo_do_produto': "bebidas",
                'preco_do_produto': 24.99,
                'quantidade_vendida': 1605
            },
            {
                'ID': 107,
                'tipo_do_produto': "lacticinios",
                'preco_do_produto': 10.49,
                'quantidade_vendida': 1200
            }
        ]
    ]
]
