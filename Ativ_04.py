def peso():
    from menu import opcao_invalida, voltar_ao_menu_principal
    
    try:
        print("""
            \nBem-vindo ao sistema de Anna Júlia para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas.
        """)

        try:
            peso = float(input('Digite o seu peso (kg): ').replace(",", "."))
            altura = float(input('Digite sua altura (m): ').replace(",", "."))
            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser números positivos.")
                voltar_ao_menu_principal()
                return
        except ValueError:
            print("Entrada inválida! Por favor, digite valores numéricos.")
            voltar_ao_menu_principal()
            return

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print(f'\nSeu IMC é {imc:.2f}. Você está abaixo do peso.')
        elif 18.5 <= imc < 25:
            print(f'\nSeu IMC é {imc:.2f}. Você está com o peso normal.')
        elif 25 <= imc < 30:
            print(f'\nSeu IMC é {imc:.2f}. Você está com sobrepeso.')
        else:
            print(f'\nSeu IMC é {imc:.2f}. Você está na faixa de obesidade.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
