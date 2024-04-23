from typing import Dict
class Produto:
    
    def __init__(self, id_produto, nome_produto, foto_produto, nota, valor, categoria) -> None:
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.foto_produto = foto_produto
        self.nota = nota
        self.valor = valor
        self.categoria = categoria