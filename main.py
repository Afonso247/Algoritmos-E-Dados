import time
from script import (
    findTotalQuantia_porMes as fTQpM,
    findTotalRenda_porMes as fTRpM,
    findMediaQuantia_porMes as fMQpM,
    findMediaRenda_porMes as fMRpM,
    findFilialMaiorFaturamento as fFMF
)

print("Bem-vindo a rede de supermercados")


# Início da interface
def start():
    
    
    print("O que você deseja consultar?")
    print("Valor total das vendas: 1")
    print("Valor mediano das vendas: 2")
    print("Filial com Maior Faturamento: 3")
    print("Sair: 0")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return totalSel()
        elif(int(select) == 2):
            print("-----")
            return mediaSel()
        elif(int(select) == 3):
            print("-----")
            return totalFilial()
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




# Seleção Total
def totalSel():
    print("Selecione o tipo da consulta... (Total)")
    print("Por Quantia: 1")
    print("Por Renda: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return quantiaTotalSel()
        elif(int(select) == 2):
            print("-----")
            return rendaTotalSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return totalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return totalSel()
    
def quantiaTotalSel():
    print("Selecione o mês de início a ser consultado... (Quantia - Total)")
    print("Jan-Jun: 1-6")
    print("Consulta geral: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (Quantia - Total)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return quantiaTotalSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fTQpM(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return quantiaTotalSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return quantiaTotalSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return quantiaTotalSel()
        elif(int(select) == 7):
            fTQpM(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return totalSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return quantiaTotalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return quantiaTotalSel()
    
def rendaTotalSel():
    print("Selecione o mês de início a ser consultado... (Renda - Total)")
    print("Jan-Jun: 1-6")
    print("Consulta geral: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (Renda - Total)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return rendaTotalSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fTRpM(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return rendaTotalSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return rendaTotalSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return rendaTotalSel()
        elif(int(select) == 7):
            fTRpM(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return totalSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return rendaTotalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return rendaTotalSel()





# Seleção Média
def mediaSel():
    print("Selecione o tipo da consulta... (Média)")
    print("Por Quantia: 1")
    print("Por Renda: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return quantiaMediaSel()
        elif(int(select) == 2):
            print("-----")
            return rendaMediaSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return mediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return mediaSel()
    
def quantiaMediaSel():
    print("Selecione o mês de início a ser consultado... (Quantia - Media)")
    print("Jan-Jun: 1-6")
    print("Consulta geral: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (Quantia - Media)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return quantiaMediaSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fMQpM(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return quantiaMediaSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return quantiaMediaSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return quantiaMediaSel()
        elif(int(select) == 7):
            fMQpM(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return mediaSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return quantiaMediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return quantiaMediaSel()
    
def rendaMediaSel():
    print("Selecione o mês de início a ser consultado... (Renda - Media)")
    print("Jan-Jun: 1-6")
    print("Consulta geral: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (Renda - Media)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return rendaMediaSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fMRpM(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return rendaMediaSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return rendaMediaSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return rendaMediaSel()
        elif(int(select) == 7):
            fMRpM(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return mediaSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return rendaMediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return rendaMediaSel()
    

# Total filial
def totalFilial():
    print("Confirme sua solicitação para Filial com Maior Faturamento")
    print("Confirme: 1")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            fFMF()
            print("-----")
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
            return totalFilial()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return totalFilial()


# Início do programa
start()
