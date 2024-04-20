import mysql.connector 
import PIL
from PIL import Image
from typing import Dict
import os

class Connection:

    def conectar():
        fields = '__all__' 
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        port='3306',
        password='PassWord#123',
        database='db_projeto_ecomerce' 
        )
        return conexao

    def closeAll(cursor, conn):
        cursor.close()
        conn.close()
    


