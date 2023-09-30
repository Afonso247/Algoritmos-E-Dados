import random, time

def bucket_sort(arr):
    # Definir o número de baldes
    num_buckets = 10  # Neste caso, usaremos 10 baldes

    # Criar baldes vazios
    buckets = [[] for _ in range(num_buckets)]

    # Distribuir os elementos nos baldes
    for num in arr:
        index = num // 10  # Determinar qual balde o elemento deve ir
        buckets[index].append(num)
        time.sleep(1)
        print(f"Adicionando {num} ao balde {index} => {buckets}")

    # Ordenar cada balde e juntar os resultados
    sorted_arr = []
    for bucket in buckets:
        bucket.sort()
        sorted_arr.extend(bucket)
        time.sleep(1)
        print(f"Ordenando o balde {bucket} => {sorted_arr}")

    time.sleep(1)
    return sorted_arr

# Gerar uma lista aleatória de 30 números no intervalo de 0 a 99
random.seed(42)  # Defina uma semente para reprodutibilidade
random_numbers = [random.randint(0, 99) for _ in range(30)]

print("Lista não ordenada:")
print(random_numbers)

# Chame a função bucket_sort para ordenar a lista
sorted_numbers = bucket_sort(random_numbers)

print("Lista ordenada:")
print(sorted_numbers)
