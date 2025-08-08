class MenuPrincipal:

    def __init__(self):
        pass

    def indices_menu(self):
        print("-" * 40)
        print("MENU PRINCIPAL".center(40))
        print("-" * 40)
        print("[1] CADASTRAR CONTATO")
        print("[2] CONSULTAR AGENDA DE CONTATOS")
        print("[3] SAIR")
        print("-" * 40)

    def opcao_menu(self):

        MenuPrincipal.indices_menu(self)

        while True:

            escolha_opcao = int(input("ESCOLHA UMA OPÇÃO: "))

            if escolha_opcao == 3:
                print()
                print("PROGRAMA ENCERRADO...")
                break
