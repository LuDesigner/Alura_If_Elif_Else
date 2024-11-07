def temperatura():
    from menu import opcao_invalida, voltar_ao_menu_principal

    try:   
        print("""
            \nLucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse o limite.
            A temperatura máxima permitida é de 35°C.
        """)

        try:
            temp = int(input('Informe a temperatura atual da sala de servidores (em °C): '))
        except ValueError:
            print("Digite um número inteiro para a temperatura.")
            voltar_ao_menu_principal()
            return

        if temp > 35:
            print(f'\nA temperatura está em {temp}°C e ultrapassou o limite! Cuidado, os servidores podem superaquecer.')
        else:
            print(f'\nA temperatura está em {temp}°C e está dentro do limite seguro.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
