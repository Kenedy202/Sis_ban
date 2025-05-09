menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
 
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito R${valor:.2f}\n"
        
        else: 
            print("A operação falhou! O valor informado é inválido.")


    elif opcao == "s":

        valor = float (input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saque = numero_saque > LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("O valor informado excede o limie para realização da operação.")

        elif excedeu_saque:        
            print("Limite de saque diário atingido.")

        elif valor > 0:    
            saldo -= valor 
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1

        else:
            print("O valor informado é invalido para realização da operação.")    

    elif opcao == "e":
        
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================")


    elif opcao == "q":
        print("Obrigado por usar nosso Sistema Bancário!!")
        break    

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")