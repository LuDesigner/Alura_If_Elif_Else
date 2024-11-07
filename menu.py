import os
from Ativ_01 import vendas
from Ativ_02 import dias
from Ativ_03 import temperatura
from Ativ_04 import peso
from Ativ_05 import orcamento
from Ativ_06 import horas
from Ativ_07 import media
from Ativ_08 import pedagio
from Ativ_09 import jogo
from Ativ_10 import emprestimo

def exibir_titulo():
    print("""

░█████╗░████████╗██╗██╗░░░██╗██╗██████╗░░█████╗░██████╗░███████╗███████╗███████╗███████╗
██╔══██╗╚══██╔══╝██║██║░░░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔═══╝░
███████║░░░██║░░░██║╚██╗░██╔╝██║██║░░██║███████║██║░░██║█████╗░░██████╗░█████╗░░██████╗░
██╔══██║░░░██║░░░██║░╚████╔╝░██║██║░░██║██╔══██║██║░░██║██╔══╝░░╚════██╗██╔══╝░░╚════██
██║░░██║░░░██║░░░██║░░╚██╔╝░░██║██████╔╝██║░░██║██████╔╝███████╗██████╔╝███████╗██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░╚══════╝╚═════╝░
""")

#----------
def exibir_opcoes():
    opcoes = [
        "Atividade 01 - Vendas de Bruno",
        "Atividade 02 - Dias de Camila",
        "Atividade 03 - Temperatura de Lucas",
        "Atividade 04 - IMC",
        "Atividade 05 - Orçamento de Carlos",
        "Atividade 06 - Acesso de Mariana",
        "Atividade 07 - Média da professora",
        "Atividade 08 - Pedágio de Fernanda",
        "Atividade 09 - Par ou Ímpar com Lucas",
        "Atividade 10 - Empréstimo de Pedro",
        "Sair"
    ]
    
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    print()

def escolher_opcao():
    acoes = {
        1: vendas,
        2: dias,
        3: temperatura,
        4: peso,
        5: orcamento,
        6: horas,
        7: media,
        8: pedagio,
        9: jogo,
        10: emprestimo,
        11: finalizar_app
    }
    
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))
        
        # Executa a função associada à opção escolhida, se existir
        acao = acoes.get(opcao_escolhida)
        if acao:
            acao()
        else:
            opcao_invalida()
            
    except ValueError:
        opcao_invalida()
#----------
def finalizar_app():
    os.system('cls')
    print('\nFinalizando o app')

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite Enter para reiniciar.')
    main()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()