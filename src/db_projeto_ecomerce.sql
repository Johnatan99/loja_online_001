drop database if exists db_projeto_ecomerce;
create schema db_projeto_ecomerce;
use db_projeto_ecomerce;

create table product(
	id_produto int not null auto_increment,
    nome_produto varchar(120),
    foto_produto blob,
    nota int,
    valor float,
    categoria varchar(50),
    primary key(id_produto)
    );
    
insert into product(nome_produto, foto_produto, nota, valor, categoria) values("Controle",  "sdsdsds", 5, '2500.00', "Eletrônicos");

insert into product(nome_produto, foto_produto, nota, valor, categoria) values("Controle",  null, 5, '2500.00', "Eletrônicos");

select * from product;