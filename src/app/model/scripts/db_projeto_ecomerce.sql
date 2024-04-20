drop database if exists db_projeto_ecomerce;
create schema db_projeto_ecomerce;
use db_projeto_ecomerce;


create table produto(
	id_produto int not null auto_increment,
    nome_produto varchar(50),
    foto_produto blob,
    nota varchar(50),
    valor int,
    categoria varchar(30),
    primary key(id_produto)
    );
    


select * from produto;

insert into produto(nome_produto, foto_produto, nota, valor, categoria) values("sadsadsa",  "nanan", 5, 2000,"Bananas" );