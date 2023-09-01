from script import (
    findTotalQuantia_geral as fTQg,
    findMediaQuantia_geral as fMQg,
    findTotalRenda_geral as fTRg,
    findMediaRenda_geral as fMRg
)

def start():
    
    print("Bem-vindo a rede de supermercados")
    print("-----")
    print("Como você deseja consultar?")
    print("Por Quantia: 1")
    print("Por Renda: 2")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            return quantiaSel()
        elif(int(select) == 2):
            return rendaSel()
        else:
            return "Houve um erro! Provavelmente você digitou uma opção inválida..."
    except ValueError:
        return "Houve um erro de valor! Tente novamente."

def quantiaSel():
    print("De que forma (Quantia)?")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            return fTQg()
        elif(int(select) == 2):
            return fMQg()
        else:
            return "Houve um erro! Provavelmente você digitou uma opção inválida..."
    except ValueError:
        return "Houve um erro de valor! Tente novamente."
    
def rendaSel():
    print("De que forma (Renda)?")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    
    select = input("Digite aqui: ")

    
    try:
        if(int(select) == 1):
            return fTRg()
        elif(int(select) == 2):
            return fMRg()
        else:
            return "Houve um erro! Provavelmente você digitou uma opção inválida..."
    except ValueError:
        return "Houve um erro de valor! Tente novamente."
    
    



# Início do programa
print(start())
