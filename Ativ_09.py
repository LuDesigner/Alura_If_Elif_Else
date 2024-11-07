def jogo():
    from menu import opcao_invalida, voltar_ao_menu_principal

    print("""
        \nLucas quer jogar um jogo de par ou ímpar.
    """)

    try:
        number = int(input('Informe um número positivo para Lucas: '))

        # Verifica se o número é negativo
        if number < 0:
            print(f'\nO {number} é negativo. Escolha outro número positivo.')
        elif number == 0:
            print('\nZero é um número neutro.')
        else:
            # Verifica se o número é par ou ímpar
            if number % 2 == 0:
                print(f'\nO {number} é Par.')
            else:
                print(f'\nO {number} é Ímpar.')

    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()