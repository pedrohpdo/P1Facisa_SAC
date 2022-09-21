import dataBaseOperations
import auxiliarMethods

tests = auxiliarMethods.Validation()
database = dataBaseOperations

class Suggestions:
    """
    Classe da categoria Sugesstions (Sugestões), todos os dados dessa categoria serão, adicionados e tratados na classe.
    """
    
    def setSuggestion(self, author, value):
        """
        Função que adiciona um novo registro de sugestões dentro do banco de dados.

        :param value: o registro (em String) que será adicionado a lista.
        :return: Uma String confirmando a operação
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = (
            "INSERT INTO feedbacks (type, author, description) values (%s, %s, %s)"
        )
        data = ("suggestion", author, value)

        database.insertNewRecordInDatabase(connection, sqlCode, data)
        database.closeDatabase(connection)

        return f'\033[1m{"REGISTRO ADICIONADO COM SUCESSO!":^100}\033[m'

    def getSuggestions(self):
        """
        Função que será usada para imprimir os dados da lista

        :return: Retorna um lista com as linhas do banco de dados correspondentes as sugestões
        """

        listing = ''
        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "SELECT * FROM feedbacks where type = 'suggestion'"
        result = database.getDatabaseRecords(connection, sqlCode)

        for data in result:
            listing += f"| ID: {data[0]:<8} | Tipo: {data[1]:<10} | Autor: {data[2]:<15} | Registro: {data[3]:<15}\n"

        database.closeDatabase(connection)

        return listing

    def deleteSuggestion(self, idToDelete):
        """
        Função que deleta um registro específico do banco de dados a partir de um id fornecido pelo usuário

        :param idToDelete: id fornecido pelo usuário com o registro que vai ser deletado

        :return: retorna um boolean que comprova se a posição foi apagada, ou outro que mostra se a lista estiver previamente vazia, não existindo dados a serem apagados
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "DELETE FROM feedbacks where id = %s"
        data = (idToDelete,)
        database.deleteDatabaseRecords(connection, sqlCode, data)

        database.closeDatabase(connection)

        return True

    def updateSuggestion(self, indexOfSuggestion, newValue):
        """
        Função que altera o registro de uma determinada sugestão dentro do banco de dados

        :param indexOfSuggestion: A posição da lista onde eu desejo alterar dados.
        :param newValue: nova informção que será registrada no lugar da anterior.

        :return: um boolean que comprova a alteração de dados
        """
        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "UPDATE feedbacks SET description = %s WHERE id = %s"
        data = (newValue, indexOfSuggestion)
        database.updateDatabaseRecords(connection, sqlCode, data)
        database.closeDatabase(connection)

        return True

    def deleteAllSugesstions(self):
        """
        Função que deleta todos os dados do tipo suggestion.

        :return: um boolean confirmando o processo.
        """
        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
        sqlCode = "DELETE FROM feedbacks WHERE type = %s"
        data = "claim"
        database.deleteDatabaseRecords(connection, sqlCode, data)
        database.closeDatabase(connection)
        
        return True
