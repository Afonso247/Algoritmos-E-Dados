import time
from script import (
    findTotalQuantia_porMes as fTQpM,
    findTotalRenda_porMes as fTRpM,
    findMediaQuantia_porMes as fMQpM,
    findMediaRenda_porMes as fMRpM
)
from scriptgeral import (
    findTotalQuantia_geral as fTQg,
    findTotalRenda_geral as fTRg,
    findMediaQuantia_geral as fMQg,
    findMediaRenda_geral as fMRg
)

print("Bem-vindo a rede de supermercados")


# Início da interface
def start():
    
    
    print("Selecione o tipo de consulta:")
    print("Categorias e filiais: 1")
    print("Somente filiais: 2")
    print("Sair: 0")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return chooseCategoria()
        elif(int(select) == 2):
            print("-----")
            return chooseFilial()
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
    
    
    
# ----- Somente filial -----
def chooseFilial():
    
    
    print("Em que formato você deseja consultar? (SF)")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    print("Voltar: 0")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return ftotalSel()
        elif(int(select) == 2):
            print("-----")
            return fmediaSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return chooseFilial()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return chooseFilial()
    
    
# Seleção total
def ftotalSel():
    print("Selecione o tipo da consulta... (SF - Total)")
    print("Por Quantia: 1")
    print("Por Renda: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return fquantiaTotalSel()
        elif(int(select) == 2):
            print("-----")
            return frendaTotalSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return chooseFilial()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return ftotalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return ftotalSel()
    
def fquantiaTotalSel():
    print("Selecione o mês de início a ser consultado... (SF - Quantia - Total)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (SF - Quantia - Total)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return fquantiaTotalSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fTQg(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return fquantiaTotalSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return fquantiaTotalSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return fquantiaTotalSel()
        elif(int(select) == 7):
            fTQg(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return ftotalSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return fquantiaTotalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return fquantiaTotalSel()
    
def frendaTotalSel():
    print("Selecione o mês de início a ser consultado... (SF - Renda - Total)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (SF - Renda - Total)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return frendaTotalSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fTRg(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return frendaTotalSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return frendaTotalSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return frendaTotalSel()
        elif(int(select) == 7):
            fTRg(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return ftotalSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return frendaTotalSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return frendaTotalSel()





# Seleção Média
def fmediaSel():
    print("Selecione o tipo da consulta... (SF - Média)")
    print("Por Quantia: 1")
    print("Por Renda: 2")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return fquantiaMediaSel()
        elif(int(select) == 2):
            print("-----")
            return frendaMediaSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return chooseFilial()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return fmediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return fmediaSel()
    
def fquantiaMediaSel():
    print("Selecione o mês de início a ser consultado... (SF - Quantia - Media)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (SF - Quantia - Media)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return fquantiaMediaSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fMQg(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return fquantiaMediaSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return fquantiaMediaSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return fquantiaMediaSel()
        elif(int(select) == 7):
            fMQg(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return fmediaSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return fquantiaMediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return fquantiaMediaSel()
    
def frendaMediaSel():
    print("Selecione o mês de início a ser consultado... (SF - Renda - Media)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (SF - Renda - Media)")
            print("Jan-Jun: 1-6")
            print("Voltar: 0")
            
            selector = input("Digite aqui: ")
            
            if(int(selector) != 0 and int(selector) < int(select)):
                print("Mês final é menor do que o mês inicial. Tente novamente.")
                print("-----")
                time.sleep(1)
                return frendaMediaSel()
            
            try:
                if(1 <= int(selector) <= 6):
                    fMRg(int(select)-1, int(selector))
                    print("-----")
                    return start()
                elif(int(selector) == 0):
                    print("Voltando...")
                    print("-----")
                    time.sleep(1)
                    return frendaMediaSel()
                else:
                    print("Houve um erro! Provavelmente você digitou uma opção inválida...")
                    print("-----")
                    time.sleep(1)
                    return frendaMediaSel()
            except ValueError:
                print("Houve um erro de valor! Tente novamente.")
                print("-----")
                time.sleep(1)
                return frendaMediaSel()
        elif(int(select) == 7):
            fMRg(0, 6)
            print("-----")
            return start()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return fmediaSel()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return frendaMediaSel()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return frendaMediaSel()




# ----- Filiais e Categorias -----
def chooseCategoria():
    
    
    print("Em que formato você deseja consultar? (C&F)")
    print("Por valor total: 1")
    print("Por valor mediano: 2")
    print("Voltar: 0")

    select = input("Digite aqui: ")
    
    
    try:
        if(int(select) == 1):
            print("-----")
            return totalSel()
        elif(int(select) == 2):
            print("-----")
            return mediaSel()
        elif(int(select) == 0):
            print("Voltando...")
            print("-----")
            time.sleep(1)
            return start()
        else:
            print("Houve um erro! Provavelmente você digitou uma opção inválida...")
            print("-----")
            time.sleep(1)
            return chooseCategoria()
    except ValueError:
        print("Houve um erro de valor! Tente novamente.")
        print("-----")
        time.sleep(1)
        return chooseCategoria()




# Seleção Total
def totalSel():
    print("Selecione o tipo da consulta... (C&F - Total)")
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
            return chooseCategoria()
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
    print("Selecione o mês de início a ser consultado... (C&F - Quantia - Total)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (C&F - Quantia - Total)")
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
    print("Selecione o mês de início a ser consultado... (C&F - Renda - Total)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (C&F - Renda - Total)")
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
    print("Selecione o tipo da consulta... (C&F - Média)")
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
            return chooseCategoria()
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
    print("Selecione o mês de início a ser consultado... (C&F - Quantia - Media)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (C&F - Quantia - Media)")
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
    print("Selecione o mês de início a ser consultado... (C&F - Renda - Media)")
    print("Jan-Jun: 1-6")
    print("Todos os meses: 7")
    print("Voltar: 0")
    
    select = input("Digite aqui: ")
    
    
    try:
        if(1 <= int(select) <= 6):
            print("Selecione o mes final a ser consultado... (C&F - Renda - Media)")
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
    




# Início do programa
start()
