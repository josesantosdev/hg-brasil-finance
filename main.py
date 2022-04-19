import locale
from datetime import datetime

from dao.sqlite_dao_factory import SqliteDAOFactory
from models.cotacao import Cotacao
import requests as requests
import config


url_base = 'https://api.hgbrasil.com/finance'.format('?key={0}', config.api_key)

locale.setlocale(locale.LC_ALL,'')
data_hora_hoje = str(datetime.today().date().strftime('%A, %x'))

cotacaoDAO = None
cotacao_hoje = None

def consulta_dados_financeiros() -> Cotacao:
    res = requests.get(url_base)
    dados = res.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now)

    return Cotacao(dolar=dolar, euro=euro, data_hora=data_hora)


def carregar_cotacao_hoje() -> Cotacao:

    registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()

    if registro_cotacao_hoje is None:
            cotacao = consulta_dados_financeiros()
            salvar_cotacao(cotacao)
            return cotacao
    else:
        registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()
        return Cotacao(registro_cotacao_hoje[0], registro_cotacao_hoje[1],
                       registro_cotacao_hoje[2], registro_cotacao_hoje[3])

def salvar_cotacao(cotacao) -> None:
    cotacaoDAO.adicionar(cotacao)



def mostrar_menu():
    print(f'Cotação: ', {data_hora_hoje})
    print(f'Dolar: ', {cotacao_hoje.dolar})
    print(f'Euro: ', {cotacao_hoje.euro})
    print(f'Digite um valor em R$ ou 0 para Sair')

    valor_reais = float(input('R$ '))

if __name__ == '__main__':
    SqliteFactory = SqliteDAOFactory()
    cotacaoDAO = SqliteFactory.cotacao_dao
    cotacao_hoje = carregar_cotacao_hoje()
    mostrar_menu()

