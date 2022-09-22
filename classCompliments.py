import auxiliarMethods
import dataBaseOperations

tests = auxiliarMethods.Validation()
database = dataBaseOperations


class Compliments:
    """
    Classe da categoria Compliments (Elogios), todos os dados dessa categoria serão, adicionados e tratados na classe.
    """

    complimentsId = []

    def setCompliment(self, author, value):
        """
        Função que adiciona um novo registro de elogios dentro do banco de dados.

        :param value: o registro (em String) que será adicionado ao BD.
        :return: Uma String confirmando a operação
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

        sqlCode = (
            "INSERT INTO feedbacks (type, author, description) values (%s, %s, %s)"
        )
        data = ("compliment", author, value)

        database.insertNewRecordInDatabase(connection, sqlCode, data)
        database.closeDatabase(connection)

        return f'\033[1m{"REGISTRO ADICIONADO COM SUCESSO!":^100}\033[m'

    def getCompliments(self):
        """
        Função que será usada para imprimir os dados da lista

        :return: Retorna um lista com as linhas do banco de dados correspondentes as reclamações
        """

        self.complimentsId =[]
        index = 1
        listing = ""

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
        sqlCode = "SELECT * FROM feedbacks where type = 'compliment'"

        result = database.getDatabaseRecords(connection, sqlCode)
        database.closeDatabase(connection)

        for data in result:

            listing += f"| ID: {index:<8} | Tipo: {data[1]:<10} | Autor: {data[2]:<15} | Registro: {data[3]:<15}\n"

            self.complimentsId.append(data[0])

            index+=1


        return listing

    def deleteCompliment(self, idToDelete):
        """
        Função que deleta um registro específico do banco de dados a partir de um id fornecido pelo usuário

        :param idToDelete: id fornecido pelo usuário com o registro que vai ser deletado

        :return: retorna um boolean que comprova se a posição foi apagada, ou outro que mostra se a lista estiver previamente vazia, não existindo dados a serem apagados
        """

        if not self.complimentsId:
            return False
        else:
            connection = database.openDatabase("localhost", "root", "root", "ouvidoria")

            sqlCode = "DELETE FROM feedbacks where id = %s"
            data = (self.complimentsId[idToDelete - 1],)

            database.deleteDatabaseRecords(connection, sqlCode, data)
            database.closeDatabase(connection)


        return True

    def updateCompliment(self, indexOfCompliments, newValue):
        """
        Função que altera o registro de uma determinada posição na lista.

        :param indexOfCompliments: A posição da lista onde eu desejo alterar
        dados.
        :param newValue: nova informção que será registrada no lugar da anterior.
        :return: um boolean que comprova a alteração de dados
        """
        if not self.complimentsId:
            return False
        else:
            connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
            sqlCode = "UPDATE feedbacks SET description = %s WHERE id = %s"
            data = (newValue, indexOfCompliments)

            database.updateDatabaseRecords(connection, sqlCode, data)
            database.closeDatabase()
            
            return True 



    def deleteAllCompliments(self):
        """
        Função que deleta todos os dados do tipo Compliments.

        :return: um boolean confirmando o processo.
        """

        connection = database.openDatabase("localhost", "root", "root", "ouvidoria")
        sqlCode = "DELETE FROM feedbacks WHERE type = %s"
        data = ("compliment")
        database.deleteDatabaseRecords(connection, sqlCode, data)
        database.closeDatabase(connection)

        return True
