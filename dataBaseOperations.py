import mysql.connector
"""
Classe que armazena todas as funções de interação dentro do bando de dados
MYSQL. Basicamente, as funções CRUD do Sistema de Ouvidoria.
"""


def openDatabase(host, user, password, database):
    """
    Abertura do Banco de Dados MYSQL

    :param host: hostnome
    :param user: login username
    :param password: login password
    :param database: database que vai ser utilizada no sistema
    :return retorna a abertura da conexão com o sistema
    """

    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def closeDatabase(connection):
    """
    Fecha a conexão com o banco de dados MYSQL
    :param connection: conexão com o banco de dados MYSQL, que vai ser
    encerrada abaixo.
    """

    connection.close()


def insertNewRecordInDatabase(connection, sql, data):
    """
    Insere novos dados na tabela do banco de dados a partir do seu comando
    e dos dados que são fornecidos nas classes das categorias

    :param connection: conexão com o banco de dados MYSQL
    :param sql: comando que vai inserir os novos dados na tabela
    :param data: dados específicos que vão ser passados pelo usuário

    return retorna o id referente ao dado recém adicionado
    """

    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()

    return id


def getDatabaseRecords(connection, sql):
    """
    Busca todos os dados da tabela, que será impressa para o usuário

    :param connection: conexão com o banco de dados MYSQL
    :param sql: comando para buscar todos os dados da tabela

    :return todas as linhas que estão salvas dentro da tabela
    """

    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()

    return results


def deleteDatabaseRecords(connection, sql, idToDelete):
    """
    Deleta elementos específico da tabela a partir de sua PRIMARY KEY id

    :param connection: conexão com o banco de dados MYSQL
    :param sql: comando que vai deletar algum dado da tabela
    :param idToDelete: key que será usada como referência para deletar informações

    return: todas as linhas que foram afetadas pelo processo
    """
    cursor = connection.cursor()
    cursor.execute(sql, idToDelete)
    connection.commit()

    dataAffected = cursor.rowcount
    cursor.close()

    return dataAffected


def updateDatabaseRecords(connection, sql, data):
    """ """
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()

    dataAffected = cursor.rowcount
    cursor.close()
    return dataAffected
