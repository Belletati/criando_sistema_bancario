menu = '''
 =========== MENU INICIAL ===========                             
|                                    |
|          [d] Depositar             | 
|          [s] Sacar                 |  
|          [e] Extrato               | 
|          [q] Sair                  | 
|                                    |
*====================================*

=>  '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"\nSaldo: R$ {saldo:.2f}")

        else:    
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("\nNão é possível realizar esta operação. Você excedeu o número de saques permitidos no dia.")
        
        elif valor > saldo:
            print("\nNão é possível realizar esta operação. Saldo insuficiente.")

        elif valor > limite:
            print(f"\nNão é possível realizar esta operação. Limite de saque permitido = R$ {limite:.2f}")    

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
            print(f"\nSaldo: R$ {saldo:.2f}")

        else:
            print("\nNão é possível realizar esta operação. O valor informado é inválido.")
  
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("\n\nNão foram realizadas movimentações." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=====================================")   

    elif opcao == "q":
        print("\nObrigada por ultilizar nosso sistema. Volte Sempre!\n\n")
        break

    else:
        print("\nOpcao inválida. Por favor selecione novamente a operação desejada.")
           
