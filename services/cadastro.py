class CadastrarContato:

    def __init__(self):
        self.contatos_cadastrados = []

    def estilizacao_menu(self):
        print("-" * 40)
        print("CADASTRAR CONTATO".center(40))
        print("-" * 40)

    def cadastrar_contato(self):

        self.estilizacao_menu()

        while True:

            print()

            flag_continuar = int(
                input(
                    "[1] CADASTRAR OUTRO CONTATO \n[2]VOLTAR AO MENU PRINCIPAL \nESCOLHA UMA OPÇÃO: "
                )
            )

            if flag_continuar == 2:
                print()
                break
