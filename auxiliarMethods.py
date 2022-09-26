"""
Arquivo auxiliarMethods ou Métodos Auxiliares. Uma classe extra onde resolvi
implementa alguns métodos que vão ser úteis ao longo do código, tal como formatação
de Strings e tratamento de excessões
"""


class Validation:
    """
    Classe criada para executar testes de entrada do usuário [input()] e validá-los
    antes de serem usados, afim de evitar que o código quebre e o programa acabe parando
    de forma inesperada.
    """

    def testString(self, value: str):
        """
        Função que testa Strings que serão fornecidas pelo usuário. A ideia é evitar que o usuário passe uma String
        vazia e o programa saia do funcionamento padrão.

        :param value: representa a mensagem apresentada ao usuário antes dele digitar seu valor.

        :return: caso a stringToRead seja aprovada pelo sistema, ela é retornada para que o sistema possa livremente
        utilizá-la ao longo das classes das categorias.
        """
        
        while True:
            stringToRead = input(value)
            if stringToRead == "":
                print("\033[31mDigite alguma coisa!\033[m")
            else:
                return stringToRead

    def testInt(self, value: int):
        """
        Função que testa valores inteiros que serão fornecidos pelo usuário. A ideia é evitar que o programa pare
        inesperadamente por conta de uma entrada inválida. Se espera um inteiro o usuário passa uma String,
        por exemplo, o programa ao invés de quebrar, retorna uma mensagem personalizada e pergunta novamente um novo
        valor, até que o mesmo seja aceito pelo sistema.
        :param value: representa a mensagem apresentada ao usuário antes dele digitar o inteiro.
        :return: caso o intValidation seja aprovado, ele é retornado para o sistema principal para que possa ser
        livremente utilizado nas classes necessárias
        """
        while True:
            try:
                intValidation = int(input(value))
            except (ValueError, TypeError):
                print("\033[31mDigite um Valor Válido!\033[m")
            else:
                return intValidation

    def testPositionList(self, value: int, listToRead: list):
        """
        Função que testa valores inteiros referentes a posições na lista fornecidos pelo usuário. A ideia é evitar
        que o programa pare por conta de uma posição fornecida que não existe na lista [IndexError], seja ela maior ou
        menor. Ao invés disso, é retornada uma mensagem personalizada ao usuário e logo em seguida o pergunta uma
        nova posição.
        :param listToRead: lista onde função vai tentar deletar a respectiva posição.
        :return: retorna um boolean que confirma o procedimento de deletaxxr uma posição

        Nota: caso a função consiga executar o comando na linha 64 [deletar a posição na lista], a posição já é
        deletada automáticamente e não é preciso chamar novamente essa função na classe correspondente a
        categoria

        """
        while True:
            try:
                positionToValidate = int(input(value))
                listToRead[positionToValidate - 1]
            except (ValueError, TypeError):
                print("\033[31mDigite um Valor Válido!\033[m")
            except IndexError:
                print("\033[31mDigite uma Posição Válida!\033[m")
            else:
                return positionToValidate - 1


class Formatter:
    """
    Classe de formatadores, apresetação de alguns menus que são utilizados no main e outras funcionalidades para
    melhorar a vizualização do usuário.
    """

    def principalMenu(self):
        menu = (
            f'{"MENU PRINCIPAL":-^100}\n\n'
            f"1 | Adicionar Novo FeedBack\n"
            f"2 | Listar FeedBacks\n"
            f"3 | Apagar Feedback\n"
            f"4 | Editar Feedback\n"
            f"5 | Sair"
        )

        return menu

    def registerMenu(self):
        menu = (
            f'{"NOVO REGISTRO:":-^100}\n\n'
            f"1 | Reclamações\n"
            f"2 | Elogios\n"
            f"3 | Sugestões\n"
        )

        return menu

    def listingMenu(self):
        menu = (
            f'{"LISTAR:":-^100}\n\n'
            f"1 | Reclamações\n"
            f"2 | Elogios\n"
            f"3 | Sugestões\n"
            f"4 | Listar Tudo\n"
        )

        return menu

    def deletingMenu(self):
        
        menu = (
            f'{"APAGAR:":-^100}\n\n'
            f"1 | Reclamações\n"
            f"2 | Elogios\n"
            f"3 | Sugestões\n"
            f"4 | Apagar todos os Registros!\n"
        )

        return menu

    def headderLine(self, title):
        headline = f'{100 * "="}\n' f"{title:^100}\n" f'{100 * "="}'
        return headline
