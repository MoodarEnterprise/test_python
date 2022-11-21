from produtos.produtos_interface import ProdutoRepositorioInterface


class ProdutoRepositorio(ProdutoRepositorioInterface):

    @classmethod
    def criar_produto(cls, name:str):
        """ Responsavel por cadastrar o produto no banco de dados"""
        ...

    @classmethod
    def deletar_produto(cls, id: int):
        """ Responsavel por deletar o produto do banco de dados"""
        ...

    @classmethod
    def listar_produtos(cls):
        """ Responsavel por listar todos os produtos do banco de dados"""
        ...
        
    @classmethod
    def pegar_produto(cls, id:int ):
        """ Responsavel por buscar um unico produto do banco de dados"""
        ...