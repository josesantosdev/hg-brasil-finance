from abc import ABC, abstractmethod


class CotacaoDAO(ABC):

    @abstractmethod
    def adicionar(self, cotacao):
        pass

    @abstractmethod
    def selecionar_cotacao(self):
        pass

    @abstractmethod
    def excluir_cotacao(self, id):
        pass

    @abstractmethod
    def buscar_cotacao_hoje(self):
        pass