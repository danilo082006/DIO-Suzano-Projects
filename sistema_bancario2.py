#mesmo sistema bancário anterior, mas melhorado
#1. limite de 10 transações diárias
#2. se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele atingiu esse
#3. mostre, no extrato, a data e hora de todas as transações

from datetime import datetime

operacoes_possiveis = """ 

(1) Depósito

(2) Saque

(3) Extrato


"""
extrato = []
limites_saques = 3
saldo_atual = 1500.00
limites_transacoes = 10
hora_formatada = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

while True:
    operacao_escolhida = input("\n" + f'Olá, qual operação você gostaria de realizar hoje? {operacoes_possiveis}')
    if limites_transacoes == 0 and (operacao_escolhida== "1" or operacao_escolhida=="2"):
        print("Você atingiu o número máximo de transações por hoje.")
        continue
    if operacao_escolhida == "1":
        deposito = float(input("\n" + "Quanto você gostaria de depositar? \n"))
        saldo_atual = saldo_atual + deposito
        extrato.append(f"Depósito de R${deposito:.2f} reais realizado em {hora_formatada} \n")
        limites_transacoes = limites_transacoes - 1
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
        extrato.append(f"Saque de R${saque:.2f} realizado em {hora_formatada} \n")
        limites_transacoes = limites_transacoes - 1
        print(f"Saque de R${saque:.2f} realizado com sucesso.")
        limites_saques = limites_saques - 1
    elif operacao_escolhida == "3":
        print("\n" + f"Seu saldo atual é de R${saldo_atual}" + "\n" + "EXTRATO - MAIS ANTIGOS".center(40, "*"))
        for item in extrato:
            print(item)
        print("EXTRATO - MAIS RECENTES".center(40, "*"))
    else:
        print("\n" + "Selecione uma opção válida, por favor.")