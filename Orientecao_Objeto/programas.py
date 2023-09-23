from entidades import Conta

# Mensagem de boas-vindas
print("########## Bem-vindo ao Banco do Povo ################")
print("########################################################")

contas = {}  # Dicionário para armazenar as contas

while True:
    print("\nEscolha uma opção:")
    print("Opção 1: Abrir uma conta")
    print("Opção 2: Conferir Saldo")
    print("Opção 3: Efetuar um depósito")
    print("Opção 4: Efetuar um saque")
    print("Opção 5: Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do titular da conta: ")
        cpf = input("Digite o CPF do titular da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        limite = float(input("Digite o limite da conta: "))

        nova_conta = Conta(nome, cpf, saldo_inicial, limite)
        contas[cpf] = nova_conta
        print("Conta criada com sucesso!")

    elif opcao == "2":
        cpf = input("Digite o CPF da conta para consultar o saldo: ")
        if cpf in contas:
            contas[cpf].consultar_saldo()
        else:
            print("Conta não encontrada.")

    elif opcao == "3":
        cpf = input("Digite o CPF da conta para fazer um depósito: ")
        if cpf in contas:
            valor_deposito = float(input("Digite o valor do depósito: "))
            contas[cpf].depositar(valor_deposito)
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        cpf = input("Digite o CPF da conta para fazer um saque: ")
        if cpf in contas:
            valor_saque = float(input("Digite o valor do saque: "))
            contas[cpf].sacar(valor_saque)
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        print("Saindo do Banco do Povo. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


    
