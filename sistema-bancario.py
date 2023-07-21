menu = """
    ===== MENU =====
    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [Q] SAIR
"""
saldo = 0
valor_limite_saque = 500
LIMITE_SAQUES = 3
qtde_saques = 0
extrato = ""


while True:
    opcao = input(menu).upper()

    if opcao == "D":
        valor_deposito = float(input("Informe o valor para depósito: "))
        saldo += valor_deposito
        extrato += f"Depósito: R$ {str(valor_deposito)} \n"

    elif opcao == "S":
        if qtde_saques < LIMITE_SAQUES:
            valor_saque = float(input("Informe o valor para saque: "))
            if valor_saque <= 0:
                print("Informe um valor positivo para saque")
            else:
                if valor_saque <= saldo and valor_saque > 0:
                    if valor_saque <= valor_limite_saque:
                        saldo -= valor_saque
                        extrato += f"Saque: R$ {str(valor_saque)} \n"
                        qtde_saques += 1
                        print("Retire o valor na boca do caixa!")
                    else:
                        print("O limite para saque é R$ 500.00")
                else:
                    print(f"Saldo insuficiente. Seu saldo é R$ {saldo}")
                    continue
        else:
            print("Limite de saque diário atingido.")
            

    elif opcao == "E":
        print("====Extrato==== \nNão foram realizadas transações \n") if not extrato else print(f"====Extrato====\n{extrato} \n Saldo: R$ {saldo:.2f}")

    elif opcao == "Q":
        print("Encerrando sessão...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        