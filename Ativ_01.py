def vendas():
    from menu import opcao_invalida, voltar_ao_menu_principal

    def obter_mes():
        mes = input('Digite o mês de venda: ')
        if not mes.isalpha():
            print("Entrada inválida! Digite apenas letras para o mês.")
            return None
        return mes

    def obter_produto():
        produto = input('Digite o nome do produto: ')
        if not produto.isalpha():
            print("Entrada inválida! Digite apenas letras para o nome do produto.")
            return None
        return produto

    def obter_quantidade():
        try:
            quantidade = int(input('Digite a quantidade vendida: '))
            if quantidade < 0:
                print("A quantidade não pode ser negativa. Informe um número válido.")
                return None
            return quantidade
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para a quantidade.")
            return None

    try:
        print("""
            \nBruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado.
            Agora, ele precisa identificar qual deles teve maior venda.
        """)

        mes = obter_mes()
        if mes is None:
            voltar_ao_menu_principal()
            return

        produto01 = obter_produto()
        if produto01 is None:
            voltar_ao_menu_principal()
            return

        quant_prod01 = obter_quantidade()
        if quant_prod01 is None:
            voltar_ao_menu_principal()
            return

        produto02 = obter_produto()
        if produto02 is None:
            voltar_ao_menu_principal()
            return

        quant_prod02 = obter_quantidade()
        if quant_prod02 is None:
            voltar_ao_menu_principal()
            return

        # Comparação das quantidades de venda
        if quant_prod01 > quant_prod02:
            print(f'\nNo mês de {mes}, o produto {produto01} vendeu mais do que o produto {produto02}.')
        elif quant_prod01 < quant_prod02:
            print(f'\nNo mês de {mes}, o produto {produto02} vendeu mais do que o produto {produto01}.')
        elif quant_prod01 == 0 and quant_prod02 == 0:
            print(f'\nNo mês de {mes}, não houve venda de nenhum dos dois produtos.')
        else:
            print(f'\nNo mês de {mes}, o produto {produto01} e o produto {produto02} venderam a mesma quantidade.')

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        opcao_invalida()
    finally:
        voltar_ao_menu_principal()
