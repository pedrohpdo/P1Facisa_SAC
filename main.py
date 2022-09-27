import classClaims
import classCompliments
import classSuggestions
import auxiliarMethods
import dataBaseOperations

database = dataBaseOperations
claims = classClaims.Claims()
compliments = classCompliments.Compliments()
suggestions = classSuggestions.Suggestions()
validation = auxiliarMethods.Validation()
formatter = auxiliarMethods.Formatter()

isTrue = True

username = validation.testString("Digite seu nome: ").capitalize()
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
        register = validation.testString("Digite seu feedback: ")
        print()

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

        if listToPrint == "1":  # Listar Reclamações
            print(formatter.headderLine("RECLAMAÇÕES:"))
            if not claims.getClaims():
                print(
                    f'\033[1;33m{"NÃO EXISTEM RECLAMAÇÕES REGISTRADAS!":^100}\033[m\n'
                )
            else:
                print(claims.getClaims())

        elif listToPrint == "2":  # Listar Elogios
            print(formatter.headderLine("ELOGIOS:"))
            if not compliments.getCompliments():
                print(f'\033[1;33m{"NÃO EXISTEM ELOGIOS REGISTRADOS!":^100}\033[m\n')
            else:
                print(compliments.getCompliments())

        elif listToPrint == "3":  # Listar Sugestões
            print(formatter.headderLine("SUGESTÕES:"))
            if not suggestions.getSuggestions():
                print(f'\033[1;33m{"NÃO EXISTEM SUGESTÕES REGISTRADAS!":^100}\033[m\n')
            else:
                print(suggestions.getSuggestions())

        elif listToPrint == "4":  # Listar todos os dados

            print(formatter.headderLine("RECLAMAÇÕES:"))
            if not claims.getClaims():
                print(
                    f'\033[1;33m{"NÃO EXISTEM RECLAMAÇÕES REGISTRADAS!":^100}\033[m\n'
                )
            else:
                print(claims.getClaims())

            print(formatter.headderLine("ELOGIOS:"))
            if not compliments.getCompliments():
                print(f'\033[1;33m{"NÃO EXISTEM ELOGIOS REGISTRADOS!":^100}\033[m\n')
            else:
                print(compliments.getCompliments())

            print(formatter.headderLine("SUGESTÕES:"))
            if not suggestions.getSuggestions():
                print(f'\033[1;33m{"NÃO EXISTEM SUGESTÕES REGISTRADAS!":^100}\033[m\n')
            else:
                print(suggestions.getSuggestions())
            
        else:
            print(f'\033[31m{"Comando inválido!":^100}\033[m\n')
            

        print()

    elif menuAction == "3":
        """
        Deletar feedbacks específicas a partir de um id fornecido pelo usuário ou deletar todos os registros do banco de dados
        """

        print(formatter.deletingMenu())
        deleteComand = validation.testString("Selecione: ")

        if deleteComand == "4":  # Deletar todos os registros do banco de dados
            database.deleteAllDatabaseRecords()
            print(f'\033[1;32m{"TODOS OS REGISTROS FORAM DELETADOS!":^100}\033[m\n')

        elif deleteComand == "1":  # Deletar alguma reclamação
            print(formatter.headderLine("RECLAMAÇÕES"))

            if not claims.getClaims():
                print(f'\033[1;33m{"NÃO EXISTEM DADOS A SEREM APAGADOS":^100}\033[m\n')
            else:
                print(claims.getClaims())

                idToDelete = validation.testPositionList(
                    "Registro a ser apagado: ", claims.claimsId
                )

                claims.deleteClaim(idToDelete)
                print(f'\033[1;32m{"REGISTRO APAGADO COM SUCESSO!":^100}\033[m')

        elif deleteComand == "2":  # Deletar algum elogio
            print(formatter.headderLine("ELOGIOS"))

            if not compliments.getCompliments():
                print(f'\033[1;33m{"NÃO EXISTEM DADOS A SEREM APAGADOS":^100}\033[m\n')
            else:
                print(compliments.getCompliments())

                idToDelete = validation.testPositionList(
                    "Registro a ser apagado: ", compliments.complimentsId
                )
                compliments.deleteCompliment(idToDelete)
                print(f'\033[1;32m{"REGISTRO APAGADO COM SUCESSO!":^100}\033[m')

        elif deleteComand == "3":  # Deletar alguma sugestão
            print(formatter.headderLine("SUGESTÕES"))

            if not suggestions.getSuggestions():
                print(
                    f'\n\033[1;32m{"NÃO EXISTEM DADOS A SEREM DELETADOS":^100}\033[m\n'
                )
            else:
                print(suggestions.getSuggestions())

                idToDelete = validation.testPositionList(
                    "Registro a ser apagado: ", suggestions.suggestionsId
                )
                suggestions.deleteSuggestion(idToDelete)
                print(f'\n\033[1;32m{"REGISTRO APAGADO COM SUCESSO":^100}\033[m\n')

        else:
            print(f'\033[31m{"Comando inválido!":^100}\033[m\n')

        print()

    elif menuAction == "4":
        """
        Atualizar algum registro já existente dentro do banco de usuários
        """
        print(formatter.listingMenu())
        updateList = validation.testString("O que você deseja alterar? (1 | 2 | 3): ")

        if updateList == "1":  # Editar alguma reclamação
            print(formatter.headderLine("RECLAMAÇÕES"))

            if not claims.getClaims():
                print(
                    f'\n\033[1;33m{"NÃO EXISTEM DADOS A SEREM ALTERADOS":^100}\033[m\n'
                )
            else:
                print(claims.getClaims())

                positionToUpdate = validation.testPositionList("Registro a ser alterado: ", claims.claimsId)
                newValue = validation.testString("Digite seu novo feedback: ")

                claims.updateClaim(positionToUpdate, newValue)
                print(f'\n\033[1;32m{"REGISTRO ATUALIZADO COM SUCESSO!":^100}\033[m')

        elif updateList == "2":  # Editar algum elogio
            print(formatter.headderLine("ELOGIOS"))

            if not compliments.getCompliments():
                print(
                    f'\n\033[1;33m{"NÃO EXISTEM DADOS A SEREM ALTERADOS":^100}\033[m\n'
                )
            else:
                print(compliments.getCompliments())

                positionToUpdate = validation.testPositionList("Registro a ser Alterado: ", compliments.complimentsId)
                newValue = validation.testString("Digite seu novo feedback: ")

                compliments.updateCompliment(positionToUpdate, newValue)
                print(f'\n\033[1;32m{"REGISTRO ATUALIZADO COM SUCESSO!":^100}\033[m')

        elif updateList == "3":  # Editar alguma sugestão
            print(formatter.headderLine("SUGESTÕES"))

            if not suggestions.getSuggestions():
                print(
                    f'\n\033[1;33m{"NÃO EXISTEM DADOS A SEREM ALTERADOS":^100}\033[m\n'
                )
            else:
                print(suggestions.getSuggestions())
                positionToUpdate = validation.testPositionList("Registro a ser alterado: ", suggestions.suggestionsId)
                newValue = validation.testString("Digite seu novo feedback: ")

                suggestions.updateSuggestion(positionToUpdate, newValue)
                print(f'\n\033[1;32m{"REGISTRO ATUALIZADO COM SUCESSO!":^100}\033[m')
        
        else:
            print(f'\033[31m{"Comando inválido!":^100}\033[m\n')
        print()

    elif menuAction == "5":  # Sair do programa
        isTrue = False

        print()
        print(formatter.headderLine("OBRIGADO POR USAR O SISTEMA UNIFACISA!"))
        print(f'\033[1m{"Pedro Henrique Pereira de Oliveira":^100}\033[m')
        print(f'\033[1m{"github.com/pedrohpdo":^100}\033[m')
        print()
        print()


    else:
        print(f'\033[1;31m{"COMANDO INVÁLIDO! TENTE NOVAMENTE":^100}\033[m\n')
