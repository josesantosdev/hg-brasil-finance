import sqlite3

from dao.dao_factory import DAOFactory
from dao.sqlite_cotacao_dao import SqliteCotacaoDAO


class SqliteDAOFactory(DAOFactory):
    URL_DB = 'db/cotacao.py'

    @staticmethod

    def ciar_conexao():
        conexao = None

        try:
            conexao = sqlite3.connect(SqliteDAOFactory.URL_DB)
        except sqlite3.Error as err:
            raise Exception(err)
        return conexao

    def deo_factory(self) -> DAOFactory:
        return SqliteDAOFactory()

    @property
    def cotacao_dao(self):
        return SqliteCotacaoDAO()