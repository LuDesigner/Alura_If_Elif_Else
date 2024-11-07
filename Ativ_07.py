def media():
    from menu import opcao_invalida, voltar_ao_menu_principal
    
    try:
        print("""
            \nUma professora precisa de ajuda para calcular a média final dos alunos e informar se foram aprovados, ficaram de recuperação ou reprovados.
        """)

        # Função auxiliar para validar as notas
        def obter_nota(numero_nota):
            try:
                nota = float(input(f'Digite a {numero_nota} nota: ').replace(",", "."))
                if nota < 0 or nota > 10:
                    print(f"\nNota inválida! A {numero_nota} nota deve ser entre 0 e 10.")
                    return None
                return nota
            except ValueError:
                print("\nEntrada inválida! Por favor, digite um número válido para a nota.")
                return None

        # Obtendo as notas
        nota_01 = obter_nota("primeira")
        if nota_01 is None:
            voltar_ao_menu_principal()
            return

        nota_02 = obter_nota("segunda")
        if nota_02 is None:
            voltar_ao_menu_principal()
            return

        nota_03 = obter_nota("terceira")
        if nota_03 is None:
            voltar_ao_menu_principal()
            return

        # Cálculo da média
        nota_final = (nota_01 + nota_02 + nota_03) / 3

        # Classificação baseada na média
        if nota_final >= 7:
            print(f'\nA média final foi de {nota_final:.2f}. O aluno está Aprovado!')
        elif 5 <= nota_final < 7:
            print(f'\nA média final foi de {nota_final:.2f}. O aluno está de Recuperação.')
        else:
            print(f'\nA média final foi de {nota_final:.2f}. O aluno está Reprovado.')

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
