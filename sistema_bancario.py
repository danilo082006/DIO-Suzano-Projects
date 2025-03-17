#projeto bancário - Sintaxe Básica
#depósito, saque e extrato
#apenas um usuário, sem identificação
#todos os depósitos devem ser armazenados em extrato
#pode ser feito apenas 3 saques diários, com 500 reais cada
#caso o usuário nao tenha, uma mensagem informando que nao é possivel sacar mais que o saque deve ser mostrada
#todos os saques devem aparecer em extrato
#o extrato deve listar todos os depoistos e saques e o saldo atual da conta
#Formato R$ xxxx.xx

operacoes_possiveis = """ 

(1) Depósito

(2) Saque

(3) Extrato


"""
extrato = []
limites_saques = 3
saldo_atual = 1500.00

while True:
    operacao_escolhida = input("\n" + f'Olá, qual operação você gostaria de realizar hoje? {operacoes_possiveis}')
    if operacao_escolhida == "1":
        deposito = float(input("\n" + "Quanto você gostaria de depositar? \n"))
        saldo_atual = saldo_atual + deposito
        extrato.append(f"Depósito de R${deposito:.2f} reais realizado. \n")
        print(f"Depósito de R${deposito:.2f} realizado com sucesso.")
    elif operacao_escolhida == "2":
        if limites_saques == 0:
            print("Você atingiu seu limite máximo de saques por hoje.")
            continue
        saque = float(input("\n" + "Quanto você gostaria de sacar? "))
        if saque>500:
            print("O seu limite é de R$500.00 por saque.")
            continue
        elif saque>saldo_atual:
            print("Você não pode sacar um valor maior que o seu saldo atual.")
            continue
        saldo_atual = saldo_atual - saque
        extrato.append(f"Saque de R${saque:.2f} realizado. \n")
        print(f"Saque de R${saque:.2f} realizado com sucesso.")
        limites_saques = limites_saques - 1
    elif operacao_escolhida == "3":
        print("\n" + f"Seu saldo atual é de R${saldo_atual}" + "\n" + "EXTRATO - MAIS ANTIGOS".center(40, "*"))
        for item in extrato:
            print(item)
        print("EXTRATO - MAIS RECENTES".center(40, "*"))
    else:
        print("\n" + "Selecione uma opção válida, por favor.")