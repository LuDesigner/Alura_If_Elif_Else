def orcamento():
    from menu import opcao_invalida, voltar_ao_menu_principal
    
    try:
        print("""
            \nCarlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
            Ele estabeleceu um limite entre R$ 2.900 e R$ 3.200, com gastos de R$ 100 em R$ 100.
        """)

        try:
            orca = float(input('Informe o gasto mensal de Carlos (em R$): ').replace(",", "."))
            if orca < 0:
                print("\nValor de gasto inválido! O gasto não pode ser negativo.")
                voltar_ao_menu_principal()
                return
        except ValueError:
            print("\nEntrada inválida! Digite um valor numérico válido para o gasto.")
            voltar_ao_menu_principal()
            return

        if orca > 3200:
            print(f'\nCarlos ultrapassou o limite do orçamento de R$ 3.200.')
        elif orca < 2900:
            print(f'\nCarlos está abaixo do limite mínimo do orçamento de R$ 2.900.')
        elif 2900 <= orca <= 3200:
            print(f'\nCarlos ainda está dentro do orçamento.')
        elif orca == 0:
            print(f'\nCarlos não realizou gastos esse mês.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
