def pedagio():
    from menu import opcao_invalida, voltar_ao_menu_principal

    print("""
        \nFernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida, que deve ser acima de 0 km.
    """)

    try:
        km = int(input('Informe a distância que Fernanda vai percorrer (em km): '))

        # Verifica a validade da entrada
        if km < 0:
            print(f'\nA distância não pode ser negativa. Informe um valor válido.')
        elif km == 0:
            print(f'\nFernanda ainda não foi viajar.')
        elif 1 <= km <= 100:
            print(f'\nTerá que pagar R$ 10,00 de pedágio!')
        elif 101 <= km <= 200:
            print(f'\nTerá que pagar R$ 20,00 de pedágio!')
        elif km >= 201:
            print(f'\nTerá que pagar R$ 30,00 de pedágio!')
        else:
            print(f'\nOpção inválida!')

    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
