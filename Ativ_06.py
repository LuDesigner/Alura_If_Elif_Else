def horas():
    from menu import opcao_invalida, voltar_ao_menu_principal
    
    try:
        print("""
            \nMariana é responsável por liberar o acesso ao escritório. O escritório só permite acesso entre 8h e 18h.
        """)

        # Solicita a hora de forma robusta, tratando erros de entrada
        try:
            hora = int(input('Informe a hora atual (sem os minutos) para Mariana: '))
            if hora < 0 or hora > 23:
                print("\nHora inválida! Por favor, informe um valor entre 0 e 23.")
                voltar_ao_menu_principal()
                return
        except ValueError:
            print("\nEntrada inválida! Por favor, digite um número inteiro válido para a hora.")
            voltar_ao_menu_principal()
            return
        
        # Lógica de acesso
        if 8 <= hora < 18:
            print("\nAcesso liberado!")
        elif hora == 0:
            print("\nHorário não existente. O horário de 0h não é válido.")
        else:
            print("\nAcesso negado! O horário de acesso é entre 8h e 18h.")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
