import numpy as np
import random

def gerar_matriz_tridimensional(dimensao):
    if dimensao < 1:
        raise ValueError("A dimensão deve ser pelo menos 1")
    
    if dimensao > 100:
        raise ValueError("A dimensão não pode ser maior que 100")
    
    numeros_unicos = set()
    matriz = np.empty((dimensao, dimensao, dimensao), dtype=int)
    
    for i in range(dimensao):
        for j in range(dimensao):
            for k in range(dimensao):
                numero_unico = random.randint(0, 99)
                while numero_unico in numeros_unicos:
                    numero_unico = random.randint(0, 99)
                
                numeros_unicos.add(numero_unico)
                matriz[i, j, k] = numero_unico
    
    return matriz

# Exemplo de uso
dimensao = 3  # Altere a dimensão conforme desejado
matriz_3d = gerar_matriz_tridimensional(dimensao)
print(matriz_3d)
