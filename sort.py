import random


def bucket_sort(arr):
    # Encontre o valor máximo e mínimo na lista de entrada
    max_val = max(arr)
    min_val = min(arr)

    # Calcule o intervalo de cada balde
    bucket_range = 10  # Cada balde abrange 10 números

    # Crie baldes vazios
    num_buckets = (max_val - min_val) // bucket_range + 1 if (max_val - min_val) % bucket_range != 0 else (max_val - min_val) // bucket_range
    buckets = [[] for _ in range(num_buckets)]

    # Adicione cada elemento ao balde apropriado
    for num in arr:
        index = (num - min_val) // bucket_range
        buckets[index].append(num)

    # Ordena cada balde (usando Insertion Sort neste exemplo) e imprime os baldes
    for i in range(num_buckets):
        insertion_sort(buckets[i])
        print(f"Balde {i+1}: {buckets[i]}")

    # Concatena os baldes ordenados em uma lista final
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_start():
    # Inicialize um conjunto vazio para garantir números únicos
    unique_numbers = set()

    # Gere números aleatórios únicos até que tenhamos 50 deles
    while len(unique_numbers) < 30:
        random_num = random.randint(0, 99)
        unique_numbers.add(random_num)

    # Converta o conjunto em uma lista
    unique_numbers_list = list(unique_numbers)

    # A lista resultante terá 50 números únicos aleatórios entre 0 e 99
    return bucket_sort(unique_numbers_list)


# Iniciando o código:
bucket_start()
