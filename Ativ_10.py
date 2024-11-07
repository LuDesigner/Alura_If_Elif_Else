def emprestimo():
    from menu import opcao_invalida, voltar_ao_menu_principal

    print("""
        \nPedro quer solicitar um empréstimo, mas a aprovação depende de duas condições. Informe ao banco as condições de Pedro:
    """)

    try:
        renda = float(input('Informe o valor da renda mensal de Pedro: '))
        parcela = float(input('Informe o valor da parcela de Pedro: '))
        
        # Calcular 30% da renda mensal
        calculo_renda = renda * 0.3

        # Verificar condições para aprovação do empréstimo
        if renda > 2000 and 0 < parcela <= calculo_renda:
            print('\nAprovado')
        else:
            print('\nReprovado')

    except ValueError:
        print("Entrada inválida! Por favor, insira valores numéricos.")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
