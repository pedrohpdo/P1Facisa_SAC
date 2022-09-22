# P1Facisa_SAC
Desenvolvimento de um aplicação CRUD com implementação de um Sistema de Ouvidoria, fazendo implementação de categorias distintas (Reclamação, Elogios, Sugestão ou quantas
o usuário quiser), adicionando novas informações e as manipulando em um banco de dados MySQL dentro de uma conexão local.

O projeto foi proposto como avaliação da disciplina de Linguagem de Programação Estruturada do primeiro período de Sistemas de Informação da Unifacisa

# Start
Para também usar essa aplicação, close o repositório com:

```bash
$ git clone https://github.com/pedrohpdo/P1Facisa_SAC
```

Dentro do MySQL Workbench crie uma nova conexão com o user _root_ e o password _root_, depois, crie as tabelas com os seguintes comandos:

```sql
CREATE DATABASE ouvidoria;

USE ouvidoria;

CREATE TABLE feedbacks (
    
    id int not null auto_increment primary key,
    type varchar(20) not null,
    author varchar(45) not null,
    description varchar(250) not null
    
);
```

Depois é só rodar o arquivo _main.py_ com:

```bash
$ python main.py
```

## Tecnologias Usadas

- Python 3
- MySQL
