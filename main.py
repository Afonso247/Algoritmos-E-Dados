import time
from script import (
    findTotalQuantia_geral as fTQg,
    findMediaQuantia_geral as fMQg,
    findTotalRenda_geral as fTRg,
    findMediaRenda_geral as fMRg
)

print("Bem-vindo a rede de supermercados")
print("-----")

def start():
    

    print("Como você deseja consultar?")
    print("Por Quantia: 1")
    print("Por Renda: 2")
    print("Sair: 0")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            return quantiaSel()
        elif(int(select) == 2):
            return rendaSel()
        elif(int(select) == 0):
            print("Até mais!")
            return None
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return start()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return start()

def quantiaSel():
    print("De que forma (Quantia)?")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            fTQg()
            return start()
        elif(int(select) == 2):
            fMQg()
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return quantiaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return quantiaSel()
    
def rendaSel():
    print("De que forma (Renda)?")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")

    
    try:
        if(int(select) == 1):
            fTRg()
            return start()
        elif(int(select) == 2):
            fMRg()
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return rendaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return rendaSel()
    



# Início do programa
start()
