import random

def gerar_lista_aleatoria():
    random_numbers = [random.randint(0, 99) for _ in range(30)]
    return random_numbers

# Chame a função para gerar a lista aleatória
lista_aleatoria = gerar_lista_aleatoria()

print("Lista aleatória gerada:")
print(lista_aleatoria)