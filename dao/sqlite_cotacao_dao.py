import sqlite3

from dao.CotacaoDAO import CotacaoDAO
from dao.sqlite_dao_factory import SqliteDAOFactory


class SqliteCotacaoDAO(CotacaoDAO):
    def adicionar(self, cotacao):

        conexao = SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTRO Cotacao VALUES (NULL, ?, ?, ?,)'
        registro = (cotacao.dolar, cotacao.euro, cotacao.data_hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as err:
            raise Exception (f'Erro: {err}')
        finally:
            if conexao:
                conexao.close()

    def selecionar_cotacao(self):
        pass

    def excluir_cotacao(self, id):
        pass

    def pesquisar_cotacao(self):
        pass





