# Exemplo utilizando hotel com bits de quartos
# Os quartos começam por 0

import os
from getpass import getpass # usei para não mostrar caracteres digitados quando peço para apertar enter

def limparTela():
   # para mac e linux(onde os.name é 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # para windows
      _ = os.system('cls')

def estaOcupado(**kwargs):
    quarto = kwargs.get('quarto')
    if quarto is None:
        quarto = int(input("Digite o quarto que deseja verificar a disponibilidade: ")) 
    teste = 0b1
    # rotaciona para que o bit ligado fique no quarto desejado
    teste = teste << quarto
    # se o retorno for diferente de 0 o quarto esta ocupado
    if hotel & teste:
        print(f"O quarto {quarto} está ocupado" )
    else:
        print(f"O quarto {quarto} está vago")
    
    getpass("Aperte enter para voltar ao menu")
    menu()
    

def ocuparQuarto():
    quarto = int(input("Digite o quarto que deseja ocupar: "))
    teste = 0b1 
    teste = teste << quarto

    # o bit ligado do teste garante que o quarto vai ficar ocupado,
    # os outros bits do teste estão desligados e não vão alterar o hotel
    global hotel 
    hotel = hotel | teste

    print(f"Ocupando o quarto {quarto}...")    
    print( estaOcupado(quarto=quarto) )


def liberarQuarto():
    quarto = int(input("Digite o quarto que deseja ocupar: "))
    teste = 1
    teste <<= quarto
    # inverte o teste
    teste = ~teste
    # o bit desligado do teste garante que o quarto vai ser liberado,
    # os bits ligados do teste não alteram o hotel.
    
    global hotel
    hotel = hotel & teste
    print(f"Liberando o quarto {quarto}...")
    print( estaOcupado(quarto=quarto) )
    

def sair():
    exit()

def opcaoErrada():
    print("Por favor, selecione uma opção válida")
    limparTela()
    menu()


def menu():
    limparTela()
    print("""Menu do hotel 5 estrelas
    1 - Ver se o quarto está ocupado
    2 - Ocupar quarto
    3 - Liberar quarto
    4 - Sair
    """)
    opcao = int(input("Digite a opção: "))
    opcoes = {
        1 : estaOcupado,
        2 : ocuparQuarto,
        3 : liberarQuarto,
        4 : sair,
    }
    
    # Gambiarra para switch
    # Tenta pegar a opção que esta na lista de opções
    # Caso não exista a opção, então retorna 'opcaoErrada'
    # O parênteses no final é para chamar a função
    opcoes.get(opcao, opcaoErrada)()

       
hotel = 0b0
menu()