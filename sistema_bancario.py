menu = """
==============================   MENU  =============================
                        [d] - Depositar
                        [s] - Sacar
                        [e] - Extrato
                        [q] - Sair
===================================================================
Escolha uma opção valida: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
SAQUES_LIMITE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depósitado: "))
        if valor > 0:
            print(f"Depósito realizado com sucesso! R$ {valor:.2f}\n")
            saldo+= valor
            extrato += f"Depósito realizado: {valor:.2f}\n"
        else :
            print("Operação de depósito falhou : O valor informado é invalido")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print(f"Operação falhou! valor R$ {valor:.2f} informado é maior que seu saldo R$ {saldo:.2f}")
        elif valor > limite:
            print(f"Operação falou valor R$ {valor:.2f} informado é maior que o limite diario de R$ 500,00")
        elif numero_saques > SAQUES_LIMITE:
            print(f"Operação de saque falou devido a quantidade diária, que é de 3 saques por dia")
        elif valor > 0:
            saldo -= valor
            print(f"Saque realizado com sucesso!")
            extrato += f"Saque realizado: R$ {valor:.2f}"
            numero_saques +=1
        else:
            print("Operação falhou: O valor informado é inválido.")
    elif opcao == "e":
        print("============================== EXTRATO ==============================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, porfavor selecione um comando válido.")