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
        extrato += f"Depósito: {str(valor_deposito)} \n"

    elif opcao == "S":
        print("saque")

    elif opcao == "E":
        print("extrato")
        print(f"---Extrato---\n{extrato} \n Saldo: {saldo:.2f}")
    elif opcao == "Q":
        print("Encerrando sessão...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        