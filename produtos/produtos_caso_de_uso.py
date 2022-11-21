
from produtos.produtos_repository import ProdutoRepositorio


class ProdutoCasoDeUso:

    def __init__(self, nome:str, valor:int, quantidade_de_itens:int, produto_repo:ProdutoRepositorio) -> None:
        self.nome = nome
        self.produto_repo = produto_repo
        self.valor = valor
        self.quantidade_de_itens = quantidade_de_itens
        self.__valor_total = 0

    def calcular_valor(self):
        self.__valor_total = self.quantidade_de_itens * self.valor


    def criar_produto(self):
        """ Caso de uso que cria o produto"""
        return self.produto_repo.criar_produto(name=self.name)


    def deletar_produto(self, id: int):
        """ Caso de uso que deleta o produto"""
        return self.produto_repo.deletar_produto(id=id)


    def listar_produtos(self):
        """ Caso de uso que lista o produto"""
        return self.produto_repo.listar_produtos()
        

    def pegar_produto(self, id:int ):
        """ Caso de uso que pega o produto"""
        return self.produto_repo.pegar_produto(id=id)