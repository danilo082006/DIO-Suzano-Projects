# sistema bancário 2, atualizado para o desafio de projeto desse módulo
# atualizações:
# operações por funções
# função saque recebe argumentos por nome
# função depósito recebe os argumentos por posição
# função extrato recebe os argumentos por posição e nome
# novas funções: criar usuário (nome, data de nascimento, cpf e endereço(logradouro, nro, bairro, cidade/sigla estado)) e criar conta corrente (lista com agência(0001), número da conta(sequencial, iniciando em 1) e usuário (usuário pode ter mais de uma conta))
#Obs: essa versão ainda não possui senha
from datetime import datetime
hora_formatada = datetime.now().strftime('%d/%m/%Y %H:%M %S')
usuarios_cpf = []
usuarios = []
agencia = "0001"
numero_conta = 0
contas = [

]



def menu_principal():
    print("MENU PRINCIPAL".center(40, "*"))
    print("""Olá, qual operação você gostaria de realizar?
          (1): Depósito
          (2): Saque
          (3): Extrato
          (4): Novo usuário
          (5): Nova conta 
    
""")
    return input(" ")



def criar_usuario(usuarios):
    cpf = input("Insira seu CPF(apenas números): ")
    if cpf in usuarios_cpf:
        print("Já existe um usuário com esse cpf.")
        return
    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Insira sua data de nascimento (Formato DD/MM/AAAA): ")
    endereco = input("Insira seu endereço (Formato: Logradouro, Número, Bairro, Cidade/Sigla Estado): ")
    usuarios_cpf.append(cpf)
    usuarios.append({'nome': nome, 'data de nascimento': data_nascimento, 'endereço': endereco, 'cpf': cpf})
    print("Usuário criado com sucesso!")
    return nome

def criar_conta_corrente(usuarios, agencia, numero_conta, contas):
    verificar_cpf = input("Informe CPF do usuário: ")
    if verificar_cpf not in usuarios_cpf:
        print("Esse CPF não está cadastrado, você precisa criar um usuário primeiro. ")
    else:
        numero_conta = numero_conta + 1
        contas.append([(f'usuário: {usuarios}, número da conta: {numero_conta}, Número da agencia: {agencia} \n')])
        print("Conta criada com sucesso!")


def saque(numero_saques, limite_saques, limite_transacoes, saldo, valor, extrato):
    excedeu_saldo = valor>saldo
    excedeu_limite_saques = numero_saques > limite_saques
    excedeu_limite_transacoes = limite_transacoes<1

    if excedeu_saldo:
        print("Operação falhou! O seu saldo é insuficiente para esse saque.")
    elif excedeu_limite_saques:
        print("Operação falhou! O seu número de saques por hoje já foi atingido.")
    elif excedeu_limite_transacoes:
        print("Operação falhou! O seu limite de transções por hoje já foi atingido.")
    elif valor>0:
        saldo = saldo - valor
        extrato = extrato + (f"Saque de {valor} realizado em {hora_formatada} \n")
        numero_saques = numero_saques + 1
        limite_transacoes = limite_transacoes - 1
        print("Operação realizada com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato):
    if valor>0:
        saldo = saldo + valor
        extrato = extrato + (f"Saque de {valor} realizado em {hora_formatada} \n")
        print("Operação realizada com sucessO!")
    else:
        print("Operação falhou! O número informado é inválido.")
    return saldo, extrato

def extrato(saldo, extrato):
        print("EXTRATO".center(30, "*"))
        print("Não houve movimentação nessa conta ainda" if not extrato else extrato)
        print(f"Saldo atual: {saldo: .2f}")
        print("FIM DO EXTRATO".center(30, "*"))

def main():
    numero_conta = 0
    limite_transacoes = 10
    numero_saques = 0
    saldo = 1500
    extrato_bancario = " "
    while True:
        limite_saques = 3
        opcao = menu_principal()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato_bancario = deposito(saldo, valor, extrato_bancario)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato_bancario = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato_bancario,
                limite_saques = limite_saques,
                numero_saques= numero_saques,
                limite_transacoes= limite_transacoes,

            )
        elif opcao == "3":
            extrato(saldo, extrato=extrato_bancario)
        
        elif  opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            criar_conta_corrente(usuarios, agencia, numero_conta, contas)
            numero_conta = len(contas) + 1

main()
