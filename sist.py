menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do déposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito R$ {valor: .2f}'

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falou! O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Operação falhou! Excedeu número de sques!")

        elif valor > 0:
            saldo +=  valor
            extrato += (f"Saque : R$ {valor: .2f}")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "e":
        print ("EXTRATO")
        print ("Não foram realizadas movimentações!" if not extrato else extrato)
        print (f"Saldo: R$ {valor: .2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Selecione a operação desejada")
