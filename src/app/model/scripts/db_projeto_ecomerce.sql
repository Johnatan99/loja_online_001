drop database if exists db_projeto_ecomerce;
create schema db_projeto_ecomerce;
use db_projeto_ecomerce;

create table produto(
	id_produto int not null auto_increment,
    nome_produto varchar(120),
    foto_produto varchar(100),
    nota int,
    valor float,
    categoria varchar(50),
    primary key(id_produto)
    );
    
insert into produto(nome_produto, foto_produto, nota, valor, categoria) values("Controle",  "sdsdsds", 5, '2500.00', "Eletrônicos");

select * from produto;