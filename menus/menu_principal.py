from services.cadastro import CadastrarContato


class MenuPrincipal:

    def __init__(self):
        self.cadastro_usuario = CadastrarContato()

    def indices_menu(self):
        print("-" * 40)
        print("MENU PRINCIPAL".center(40))
        print("-" * 40)
        print("[1] CADASTRAR CONTATO")
        print("[2] CONSULTAR AGENDA DE CONTATOS")
        print("[3] SAIR")
        print("-" * 40)

    def opcao_menu(self):

        while True:

            MenuPrincipal.indices_menu(self)

            try:

                escolha_opcao = int(input("ESCOLHA UMA OPÇÃO: "))
                print()

            except (TypeError, ValueError):
                print("OPÇÃO INVALIDA...")

            if escolha_opcao == 1:
                self.cadastro_usuario.cadastrar_contato()

            if escolha_opcao == 3:
                print("PROGRAMA ENCERRADO...")
                break

            if escolha_opcao not in range(1, 3):
                print("OPÇÃO INVALIDA! ")
