menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
'''
saldo = 0
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3
extrato = ""

while True:

    print(menu)
    opcao = input("Escolha a opção desejada: ")

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operaçao invalida! O valor deve ser maior que 0.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada, verifique o saldo em conta.")
        
        elif excedeu_limite:
            print("Operação não realizada, O valor do saque excede o limite.")

        elif excedeu_saques:
            print('Operação não realizada, O número de saques excede o permitido.')
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        
        else:
            print("Operação não realizada. O valor informado é inválido.")

    elif opcao == "e":
        print("\n------------EXTRATO------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("-------------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, Insira novamente a opção desejada.")