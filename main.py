import classClaims
import classCompliments
import classSuggestions
import auxiliarMethods

claims = classClaims.Claims()
compliments = classCompliments.Compliments()
suggestions = classSuggestions.Suggestions()
validation = auxiliarMethods.Validation()
formatter = auxiliarMethods.Formatter()

isTrue = True

username = validation.testString("Digite seu nome: ")
userid = validation.testInt("Digite sua matrícula: ")

print("\033[1:34m-\033[m" * 100)
print(f'\033[1m{"Bem Vindo ao Sistema de Ouvidoria UNIFACISA!":^100}\033[m')
print("\033[1:34m-\033[m" * 100)
print()

while isTrue:
    title = f"Usuário: {username}  |  Matrícula: {userid}"
    print(f"{title:^100}")
    print()
    print(formatter.principalMenu())
    print()

    menuAction = input("Selecione (1/ 2/ 3/ 4): ")

    if menuAction == "1":
        """
        Interação do Usuário para adicionar um novo feedback no banco de dados
        """

        print(formatter.registerMenu())

        category = validation.testString("O que você deseja Registrar? (1/2/3): ")
        register = validation.testString("Digite sua ocorrência: ")

        if category == "1":
            print(claims.setClaim(username, register))

        elif category == "2":
            print(compliments.setCompliment(username, register))

        elif category == "3":
            print(suggestions.setSuggestion(username, register))

        else:
            print("Categoria não encontrada! Tente novamente!")
        print()

    elif menuAction == "2":
        """
        Listar ocorrências específicas ou todas as ocorrências do banco de dados
        para consulta do usuário
        """

        print(formatter.listingMenu())
        listToPrint = validation.testString("Listar (1/2/3/4): ")
        print()

        if listToPrint == "1": #Listar Reclamações
            print(formatter.headderLine("RECLAMAÇÕES:"))
            print(claims.getClaims())

        elif listToPrint == "2": #Listar Elogios
            print(formatter.headderLine("ELOGIOS:"))
            print(compliments.getCompliments())

        elif listToPrint == "3": #Listar Sugestões
            print(formatter.headderLine("SUGESTÕES:"))
            print(suggestions.getSuggestions())

        elif listToPrint == "4": #Listar todos os dados

            print(formatter.headderLine("RECLAMAÇÕES:"))
            print(claims.getClaims())

            print(formatter.headderLine("ELOGIOS:"))
            print(compliments.getCompliments())

            print(formatter.headderLine("SUGESTÕES:"))
            print(suggestions.getSuggestions())

        print()

    elif menuAction == "3":
        """
        Deletar feedbacks específicas a partir de um id fornecido pelo usuário ou deletar todos os registros do banco de dados
        """

        print(formatter.deletingMenu())
        deleteComand = validation.testString("Selecione: ")

        if deleteComand == "4": # Deletar todos os registros do banco de dados
            claims.deleteAllClaims()
            compliments.deleteAllCompliments()
            suggestions.deleteAllSugesstions()
            print("Todos os dados foram deletados! ")
            print()

        elif deleteComand == "1": #Deletar alguma reclamação
            print(formatter.headderLine("RECLAMAÇÕES"))
            print(claims.getClaims())
            idToDelete = validation.testInt("Registro a ser apagado: ")

            if claims.deleteClaim(idToDelete):
                print("Registro apagado com sucesso!")
            else:
                print(f'\033[0:33m{"NÃO EXISTEM DADOS A SEREM APAGADOS":^100}\033[m\n')
            print()

        elif deleteComand == "2": #Deletar algum elogio
            print(formatter.headderLine("ELOGIOS"))
            print(compliments.getCompliments())
            idToDelete = validation.testInt("Registro a ser apagado: ")

            if compliments.deleteCompliment(idToDelete):
                print("Registro apagado com sucesso!")
            else:
                print(f'\033[0:33m{"NÃO EXISTEM DADOS A SEREM APAGADOS":^100}\033[m\n')
            print()

        elif deleteComand == "3": #Deletar alguma sugestão
            print(formatter.headderLine("SUGESTÕES"))
            print(suggestions.getSuggestions())

            idToDelete = validation.testInt("Registro a ser apagado: ")

            if suggestions.deleteSuggestion(idToDelete):
                print("Registro apagado com sucesso!")
            else:
                print(f'\033[0:33m{"NÃO EXISTEM DADOS A SEREM APAGADOS":^100}\033[m\n')
            print()

    elif menuAction == "4":
        """
        Atualizar algum registro já existente dentro do banco de usuários
        """
        print(formatter.listingMenu())
        updateList = validation.testString("O que você deseja alterar? (1 | 2 | 3): ")
 
        if updateList == "1": #Editar alguma reclamação
            print(formatter.headderLine("RECLAMAÇÕES"))
            print(claims.getClaims())

            positionToUpdate = validation.testInt("Registro a ser alterado: ")
            newValue = validation.testString("Digite seu novo feedback: ")

            if claims.updateClaim(positionToUpdate, newValue):
                print("Registro Atualizado Com Sucesso!")

        elif updateList == "2": #Editar algum elogio
            print(formatter.headderLine("ELOGIOS"))
            print(compliments.getCompliments())

            positionToUpdate = validation.testInt("Registro a ser Alterado: ")
            newValue = validation.testString("Digite seu novo feedback: ")

            if claims.updateCompliment(positionToUpdate, newValue):
                print("Registro Atualizado com Sucesso!")

        elif updateList == "3": #Editar alguma sugestão
            print(formatter.headderLine("SUGESTÕES"))
            print(suggestions.getSuggestions())

            positionToUpdate = validation.testPositionList(suggestions.suggestionsList)
            newValue = validation.testString("Digite seu novo feedback: ")

            if suggestions.updateSuggestion(positionToUpdate, newValue):
                print("Registro Atualizado com Sucesso!")

    elif menuAction == "5": #Sair do programa
        print()
        print(formatter.headderLine('OBRIGADO POR USAR O SISTEMA UNIFACISA!'))
        isTrue = False

    else:
        print("Comando Inválido! Tente Novamente!")
