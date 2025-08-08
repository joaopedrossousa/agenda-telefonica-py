from services.cadastro import CadastrarContato


class ConsultaMenu:

    # Injeção de dependencia
    def __init__(self, cadastro: CadastrarContato):
        self.contatos = cadastro

    def estilizacao_menu(self):
        print("-" * 40)
        print("CONTATOS SALVOS".center(40))
        print("-" * 40)

    def mostrar_contatos_salvos(self):

        self.estilizacao_menu()

        if not self.contatos.contatos_cadastrados:
            print("NENHUM CONTATO CADASTRADO...")
            print()
            return

        for i, dados in enumerate(self.contatos.contatos_cadastrados, start=1):
            print(f"{i} Nome: {dados.get('Nome', '')}")
            print(f"  Numero: {dados.get('Numero', '')}")
            print()
