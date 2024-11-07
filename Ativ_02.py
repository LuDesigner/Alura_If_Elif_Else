def dias():
    from menu import opcao_invalida, voltar_ao_menu_principal

    def obter_tempo_projeto(numero_projeto):
        try:
            tempo = int(input(f'Digite o tempo do projeto {numero_projeto}: '))
            if tempo < 0:
                print("O tempo não pode ser negativo. Informe um número válido.")
                return None
            return tempo
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para o tempo.")
            return None

    try:
        print("""
            \nCamila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades.
            Obs: Somente números positivos!
        """)

        # Obter o tempo para cada projeto
        ativ1 = obter_tempo_projeto(1)
        if ativ1 is None:
            voltar_ao_menu_principal()
            return

        ativ2 = obter_tempo_projeto(2)
        if ativ2 is None:
            voltar_ao_menu_principal()
            return

        ativ3 = obter_tempo_projeto(3)
        if ativ3 is None:
            voltar_ao_menu_principal()
            return

        soma_total = ativ1 + ativ2 + ativ3

        if soma_total > 0:
            print(f'\nO total de dias para realizar os 3 projetos é de {soma_total}.')
        else:
            print(f'\nNão há dias para realizar o projeto.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
