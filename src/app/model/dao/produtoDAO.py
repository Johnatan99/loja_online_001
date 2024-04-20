from connection import Connection
from entities.produtoEntity import Produto
import mysql.connector
import PIL
from PIL import Image

class ProdutoDAO:
    
    def create():
        conn = Connection.conectar()
        cursor = conn.cursor()
        print(cursor)
    #produto = Produto()
    # def __create(self) -> None:
    #     conn = Connection.__connect()
    #     cursor = conn.cursor()
        
        nome = "Relógio"
        foto = Image.open('/Estudos/Desenvolvimento_de_Software/curso_estacio/Semestre 2/site_de_compras_01/app/static/images/exclusive.png')
        #     nota = 5
        #     valor = 1000
        #    # produto = Produto(nome, foto, nota, valor)
        sql = f'''insert into produto(
                        nome_produto,
                        foto_produto, 
                        nota, 
                        valor,
                        categoria
                    ) values(
                        "{nome}", 
                        "{foto}",
                        5, 
                        2000,
                        "Bananas"
                    );
                '''
        cursor.execute(sql)
        conn.commit()
        Connection.closeAll(cursor, conn)

    
    def select(aid):
        conn = Connection.conectar()
        cursor = conn.cursor()
        sql = f'''
                select 
                    *
                from
                    produto
                where 
                    id_produto = {id};
            '''

        cursor.execute(sql)
        registro = cursor.fetchall()
        print(registro)

        Connection.closeAll(cursor, conn)


id = 3
ProdutoDAO.select(id)