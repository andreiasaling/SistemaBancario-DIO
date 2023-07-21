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
        print("deposito")
    elif opcao == "S":
        print("saque")
    elif opcao == "E":
        print("extrato")
    elif opcao == "Q":
        print("Encerrando sessão...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        