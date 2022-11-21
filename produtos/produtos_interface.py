from abc import abstractmethod, ABC
from typing import List
from .produtos import Produto

class ProdutoRepositorioInterface(ABC):

    @abstractmethod
    def criar_produto(self, name:str) -> Produto:
        """ abstractmethod """
        raise Exception("Metodo não implementado")

    @abstractmethod
    def deletar_produto(self, id: int) -> None:
        """ abstractmethod """
        raise Exception("Metodo não implementado")

    @abstractmethod
    def listar_produtos(self) -> List[Produto]:
        """ abstractmethod """
        raise Exception("Metodo não implementado")
        
    @abstractmethod
    def pegar_produto(self, id:int ) -> Produto:
        """ abstractmethod """
        raise Exception("Metodo não implementado")