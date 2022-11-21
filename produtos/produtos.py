
class Produto:
    """Classe de modelo do produto"""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.__valor = 0

    def nome_do_produto(self) -> str:
        return self.nome

    @property
    def valor(self) -> int: 
        return self.__valor

    @valor.setter
    def salario(self, novo_valor): 
        raise ValueError("Impossivel alterar valor diretamente. Use a funcao valor().")