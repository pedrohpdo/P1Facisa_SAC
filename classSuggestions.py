import dataBaseOperations
import auxiliarMethods

tests = auxiliarMethods.Validation()
database = dataBaseOperations

class Suggestions:
    """
    Classe da categoria Sugesstions (Sugestões), todos os dados dessa categoria serão, adicionados e tratados na classe.
    """
    suggestionsId = []
    
    def setSuggestion(self, author: str, value: str):
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

        return f'\033[1;32m{"REGISTRO ADICIONADO COM SUCESSO!":^100}\033[m'

    def getSuggestions(self):
        """
        Função que será usada para imprimir os dados da lista

        :return: Retorna um lista com as linhas do banco de dados correspondentes as sugestões
        """
        
        self.suggestionsId = []
        index = 1
        listing = ''

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
        sqlCode = "SELECT * FROM feedbacks where type = 'suggestion'"
        result = database.getDatabaseRecords(connection, sqlCode)
        database.closeDatabase(connection)

        for data in result:
            listing += f"| ID: {index:<8} | Tipo: {data[1]:<10} | Autor: {data[2]:<15} | Registro: {data[3]:<15}\n"

            self.suggestionsId.append(data[0])

            index += 1

        if not self.suggestionsId:
            return False
        else:
            return listing
        


    def deleteSuggestion(self, idToDelete: int):
        """
        Função que deleta um registro específico do banco de dados a partir de um id fornecido pelo usuário

        :param idToDelete: id fornecido pelo usuário com o registro que vai ser deletado

        :return: retorna um boolean que comprova se a posição foi apagada, ou outro que mostra se a lista estiver previamente vazia, não existindo dados a serem apagados
        """

        if not self.suggestionsId:
            return False
        else:
            connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

            sqlCode = "DELETE FROM feedbacks where id = %s"
            data = (self.suggestionsId[idToDelete - 1],)

            database.deleteDatabaseRecords(connection, sqlCode, data)
            database.closeDatabase(connection)

            return True


    def updateSuggestion(self, indexOfSuggestion: int, newValue: str):
        """
        Função que altera o registro de uma determinada sugestão dentro do banco de dados

        :param indexOfSuggestion: A posição da lista onde eu desejo alterar dados.
        :param newValue: nova informção que será registrada no lugar da anterior.

        :return: um boolean que comprova a alteração de dados
        """

        if not self.suggestionsId:
            return False
        else:
            connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

            sqlCode = "UPDATE feedbacks SET description = %s WHERE id = %s"
            data = (newValue, self.suggestionsId[indexOfSuggestion - 1])

            database.updateDatabaseRecords(connection, sqlCode, data)
            database.closeDatabase(connection)

            return True


    def deleteAllSugesstions(self):
        """
        Função que deleta todos os dados do tipo suggestion.

        :return: um boolean confirmando o processo.
        """

        if not self.suggestionsId:
            return False
        else:
            connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
            sqlCode = "DELETE FROM feedbacks WHERE type = %s"
            data = ("claim")
            database.deleteDatabaseRecords(connection, sqlCode, data)
            database.closeDatabase(connection)
            
            return True
         
