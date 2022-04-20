import sqlite3
import dao.sqlite_dao_factory as dao
from dao.CotacaoDAO import CotacaoDAO

class SqliteCotacaoDAO(CotacaoDAO):
    def adicionar(self, cotacao):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO Cotacao VALUES (NULL, ?, ?, ?)'
        registro = (cotacao.dolar, cotacao.euro, cotacao.data_hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as err:
            raise Exception(f'Erro: {err}')
        finally:
            if conexao:
                conexao.close()

    def selecionar_cotacao(self):
        pass

    def excluir_cotacao(self, id):
        pass

    def pesquisar_cotacao(self):
        pass

    def buscar_cotacao_hoje(self):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'SELECT * FROM Cotacao WHERE DATE(data_hora_coleta) = DATE();'

        try:
            dados = cursor.execute(query).fetchone()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close





