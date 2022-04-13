import locale
from datetime import datetime

from dao.sqlite_dao_factory import SqliteDAOFactory
from models.cotacao import Cotacao
import requests
import config


url_base = 'https://api.hgbrasil.com/finance'.format('?key={0}', config.api_key)

locale.setlocale(locale.LC_ALL,'')
data_hora = str(datetime.today().date().strftime('%A, %x'))

cotacaoDAO = None
cotacao_hoje = None

def consulta_dados_financeiros() -> Cotacao:
    res = requests.get(url_base)
    dados = res.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now)

    return Cotacao(dolar=dolar, euro=euro, data_hora=data_hora)


if __name__ == '__main__':
    SqliteFactory = SqliteDAOFactory()
    cotacaoDAO = SqliteFactory.cotacao_dao
