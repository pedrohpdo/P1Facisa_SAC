import auxiliarMethods
import dataBaseOperations

tests = auxiliarMethods.Validation()
database = dataBaseOperations


class Claims:
    """
    Classe da categoria Claims(Reclamações), todos os dados dessa categoria
    serão, adicionados e tratados na classe.
    """

    def setClaim(self, author, value):
        """
        Função que adiciona um novo registro de reclamação ao banco de Dados
        :param value: o registro (em String) que será adicionado a lista.
        :param author: username que está reallizando o registro
        :return: Uma String confirmando a operação
        """
        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = (
            "INSERT INTO feedbacks (type, author, description) values (%s, %s, %s)"
        )
        data = ("claim", author, value)

        database.insertNewRecordInDatabase(connection, sqlCode, data)
        database.closeDatabase(connection)

        return f'\033[1m{"REGISTRO ADICIONADO COM SUCESSO!":^100}\033[m'

    def getClaims(self):
        """
        Função que será usada para imprimir os dados de reclamação do banco de dados

        :return: Retorna um lista com as linhas do banco de dados correspondentes as reclamações
        """

        listing = ''
        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "SELECT * FROM feedbacks where type = 'claim'"
        result = database.getDatabaseRecords(connection, sqlCode)

        for data in result:
            listing += f"| ID: {data[0]:<8} | Tipo: {data[1]:<10} | Autor: {data[2]:<15} | Registro: {data[3]:<15}\n"

        database.closeDatabase(connection)

        return listing

    def deleteClaim(self, idToDelete):
        """
        Função que deleta um registro específico do banco de dados a partir de um id fornecido pelo usuário
        
        :param idToDelete: id fornecido pelo usuário com o registro que vai ser deletado

        :return: retorna um boolean que comprova se o registro foi apagado, ou outro que mostra se a lista estiver previamente vazia, não existindo dados a serem apagados
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "DELETE FROM feedbacks where id = %s"
        data = (idToDelete,)
        database.deleteDatabaseRecords(connection, sqlCode, data)

        database.closeDatabase(connection)
        return True

    def updateClaim(self, indexOfClaim, newValue):
        """
        Edita um valor já existente no banco de dados e o sobrescreve por um novo.

        :param indexOfClaim: id correspondente ao registro que vai ser alterado.
        :param newValue: novo registro que vai sobrescrever o antigo.
        :return: um boolean que confirma o novo registro.
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = "UPDATE feedbacks SET description = %s WHERE id = %s"
        data = (newValue, indexOfClaim)
        database.updateDatabaseRecords(connection, sqlCode, data)
        database.closeDatabase(connection)

        return True

    def deleteAllClaims(self):
        """
        Função que deleta todos os dados dentro do Banco de Dados que possuem o tipo 'claim'.

        :return: um boolean confirmando o processo.
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
        sqlCode = "DELETE FROM feedbacks WHERE type = %s"
        data = "claim"
        database.deleteDatabaseRecords(connection, sqlCode, data)
        database.closeDatabase(connection)

        return True
