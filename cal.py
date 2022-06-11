from time import sleep

print("--------------------------------")
print("------Iniciando Calculadora-----")
print("--------------------------------")
sleep(1.5)

print("Bem vindo à calculadora. O que iremos resolver hoje?")
sleep(1.5)

while True:
    print("Veja abaixo as operações disponíveis: ")
    sleep(1.5)

    print("1 - ADIÇÃO")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR")

    sleep(1)

    escolha = int(input("Qual operação deseja realizar?: "))
    # CALCULO ADIÇÃO
    if escolha == 1:
        valor1 = int(input(f'Digite o primeiro número: '))
        valor2 = int(input(f'Digite o segundo número: '))
        
        sleep(1.5)
        resultado = print(f'O resultado é: {valor1 + valor2}')
        
        sleep(1.5)
        while True:
        # CALCULO ADICAO
            print("--------------------------------")
            print("-------------Opções-------------")
            print("--------------------------------")
            sleep(1.5)

            print("1 - FAZER OUTRA ADIÇÃO.")
            print("2 - FAZER OUTRA OPERAÇÃO.")
            print("3 - SAIR.")
            opcao = int(input("Informe a opção desejada: "))
            if opcao == 1:
                valor1 = int(input(f'Digite o primeiro número: '))
                valor2 = int(input(f'Digite o segundo número: '))

                sleep(1.5)
                resultado = print(f'O resultado é: {valor1 + valor2}')
                
                print("--------------------------------")
                print("-------------Opções-------------")
                print("--------------------------------")
                sleep(1.5)

                print("1 - FAZER OUTRA ADIÇÃO.")
                print("2 - FAZER OUTRA OPERAÇÃO.")
                print("3 - SAIR.")
                opcao = int(input("Informe a opção desejada: "))
                if opcao == 2:
                    break
                elif opcao == 3:
                    sleep(1.5)
                    print("Esperamos que tenha gostado. Encerrando Calculadora...")
                    break
            elif opcao == 2:
                break
            else:
                sleep(1.5)
                print("Esperamos que tenha gostado. Encerrando Calculadora...")
                break
    elif escolha == 2:
        valor1 = int(input(f'Digite o primeiro número: '))
        valor2 = int(input(f'Digite o segundo número: '))
        
        sleep(1.5)
        resultado = print(f'O resultado é: {valor1 - valor2}')
        
        sleep(1.5)
        while True:
        # CALCULO SUBTRAÇÃO
            print("--------------------------------")
            print("-------------Opções-------------")
            print("--------------------------------")
            sleep(1.5)

            print("1 - FAZER OUTRA SUBSTRAÇÃO.")
            print("2 - FAZER OUTRA OPERAÇÃO.")
            print("3 - SAIR.")
            opcao = int(input("Informe a opção desejada: "))
            if opcao == 1:
                valor1 = int(input(f'Digite o primeiro número: '))
                valor2 = int(input(f'Digite o segundo número: '))

                sleep(1.5)
                resultado = print(f'O resultado é: {valor1 - valor2}')
                
                print("--------------------------------")
                print("-------------Opções-------------")
                print("--------------------------------")
                sleep(1.5)

                print("1 - FAZER OUTRA SUBTRAÇÃO.")
                print("2 - FAZER OUTRA OPERAÇÃO.")
                print("3 - SAIR.")
                opcao = int(input("Informe a opção desejada: "))
                if opcao == 2:
                    break
                elif opcao == 3:
                    sleep(1.5)
                    print("Esperamos que tenha gostado. Encerrando Calculadora...")
                    break
            elif opcao == 2:
                break
            else:
                sleep(1.5)
                print("Esperamos que tenha gostado. Encerrando Calculadora...")
                break
# TESTE
    elif escolha == 3:
        valor1 = int(input(f'Digite o primeiro número: '))
        valor2 = int(input(f'Digite o segundo número: '))
        
        sleep(1.5)
        resultado = print(f'O resultado é: {valor1 * valor2}')
        
        sleep(1.5)
        while True:
        # CALCULO MULTIPLICAÇÃO
            print("--------------------------------")
            print("-------------Opções-------------")
            print("--------------------------------")
            sleep(1.5)

            print("1 - FAZER OUTRA MULTIPLICAÇÃO.")
            print("2 - FAZER OUTRA OPERAÇÃO.")
            print("3 - SAIR.")
            opcao = int(input("Informe a opção desejada: "))
            if opcao == 1:
                valor1 = int(input(f'Digite o primeiro número: '))
                valor2 = int(input(f'Digite o segundo número: '))

                sleep(1.5)
                resultado = print(f'O resultado é: {valor1 * valor2}')
                
                print("--------------------------------")
                print("-------------Opções-------------")
                print("--------------------------------")
                sleep(1.5)

                print("1 - FAZER OUTRA MULTIPLICAÇÃO.")
                print("2 - FAZER OUTRA OPERAÇÃO.")
                print("3 - SAIR.")
                opcao = int(input("Informe a opção desejada: "))
                if opcao == 2:
                    break
                elif opcao == 3:
                    sleep(1.5)
                    print("Esperamos que tenha gostado. Encerrando Calculadora...")
                    break
            elif opcao == 2:
                break
            else:
                sleep(1.5)
                print("Esperamos que tenha gostado. Encerrando Calculadora...")
                break
# TESTE 2
    elif escolha == 4:
        valor1 = int(input(f'Digite o primeiro número: '))
        valor2 = int(input(f'Digite o segundo número: '))
        
        sleep(1.5)
        resultado = print(f'O resultado é: {valor1 / valor2}')
        
        sleep(1.5)
        while True:
        # CALCULO DIVISÃO
            print("--------------------------------")
            print("-------------Opções-------------")
            print("--------------------------------")
            sleep(1.5)

            print("1 - FAZER OUTRA DIVISÃO.")
            print("2 - FAZER OUTRA OPERAÇÃO.")
            print("3 - SAIR.")
            opcao = int(input("Informe a opção desejada: "))
            if opcao == 1:
                valor1 = int(input(f'Digite o primeiro número: '))
                valor2 = int(input(f'Digite o segundo número: '))

                sleep(1.5)
                resultado = print(f'O resultado é: {valor1 / valor2}')
                
                print("--------------------------------")
                print("-------------Opções-------------")
                print("--------------------------------")
                sleep(1.5)

                print("1 - FAZER OUTRA DIVISÃO.")
                print("2 - FAZER OUTRA OPERAÇÃO.")
                print("3 - SAIR.")
                opcao = int(input("Informe a opção desejada: "))
                if opcao == 2:
                    break
                elif opcao == 3:
                    sleep(1.5)
                    print("Esperamos que tenha gostado. Encerrando Calculadora...")
                    break
            elif opcao == 2:
                break
            else:
                sleep(1.5)
                print("Esperamos que tenha gostado. Encerrando Calculadora...")
                break
# Encerrar calculadora
    if escolha == 5:
        contagemRegressiva = 5
        for n in range (1,6):
            print(contagemRegressiva)
            contagemRegressiva -= 1
            sleep(1)
        print("SAINDO...")
        break
    elif escolha >= 6:
        print("Escolha inválida. Tente Novamente... Retornando ao início")
        break