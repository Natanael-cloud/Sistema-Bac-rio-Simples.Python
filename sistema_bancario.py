# Variáveis de controle
saldo = 0  # Saldo inicial
limite = 500  # Limite de saque
extrato = ""  # Extrato de transações
numero_saques = 0  # Contador de saques
LIMITE_SAQUES = 3  # Limite de saques diários

# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    # Exibe o menu e lê a opção escolhida
    opcao = input(menu)

    if opcao == "d":  # Depósito
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:  # Verifica se o valor é positivo
            saldo += valor  # Atualiza saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("Valor inválido!")

    elif opcao == "s":  # Saque
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo  # Verifica saldo
        excedeu_limite = valor > limite  # Verifica limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica limite de saques

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Saque excede o limite de R$ 500.")
        elif excedeu_saques:
            print("Limite de saques diários atingido.")
        elif valor > 0:  # Verifica se o valor é positivo
            saldo -= valor  # Atualiza saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa o contador de saques
            print(f"Saque de R$ {valor:.2f} realizado!")
        else:
            print("Valor inválido!")

    elif opcao == "e":  # Extrato
        print("\n================ EXTRATO ================")
        print("Não houve movimentações." if not extrato else extrato)  # Exibe transações
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":  # Sair
        break  # Encerra o programa

    else:
        print("Opção inválida! Tente novamente.")  # Se a opção for inválida


print("Obrigado por usar nosso sistema bancário!")

