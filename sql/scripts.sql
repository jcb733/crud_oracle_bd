/*Apaga os relacionamentos*/
ALTER TABLE LABDATABASE.ordem_servico DROP CONSTRAINT fk_cliente;
ALTER TABLE LABDATABASE.ordem_servico DROP CONSTRAINT fk_tecnico;
ALTER TABLE LABDATABASE.pecas_utilizadas DROP CONSTRAINT fk_peca;
ALTER TABLE LABDATABASE.pecas_utilizadas DROP CONSTRAINT fk_ordem_servico;

/*Apaga as tabelas*/
DROP TABLE LABDATABASE.clientes;
DROP TABLE LABDATABASE.ordem_servico;
DROP TABLE LABDATABASE.tecnico;
DROP TABLE LABDATABASE.peca;
DROP TABLE LABDATABASE.pecas_utilizadas;

/* -- Criação da tabela clientes */
CREATE TABLE clientes (
  cliente_id NUMBER PRIMARY KEY NOT NULL,
  nome NVARCHAR2(255) NOT NULL,
  endereco VARCHAR2(100) NOT NULL,
  email VARCHAR2(100) NOT NULL,
  telefone NUMBER NOT NULL
);

/* -- Criação da tabela ordem_servico */
CREATE TABLE ordem_servico (
  ordem_id NUMBER PRIMARY KEY NOT NULL,
  cliente_id NUMBER NOT NULL,
  tecnico_id NUMBER NOT NULL,
  data_abertura TIMESTAMP NOT NULL,
  data_conclusao TIMESTAMP NOT NULL,
  status VARCHAR2(50) NOT NULL,
  descricao_problema VARCHAR2(500) NOT NULL,
  solucao NVARCHAR2(255) NOT NULL,
  custo_total NUMBER NOT NULL
);

/* -- Criação da tabela tecnico */
CREATE TABLE tecnico (
  tecnico_id NUMBER PRIMARY KEY NOT NULL,
  nome NVARCHAR2(255) NOT NULL,
  especialidade VARCHAR2(50) NOT NULL,
  email VARCHAR2(50),
  telefone NUMBER NOT NULL
);

/* -- Criação da tabela peca */
CREATE TABLE peca (
  peca_id NUMBER PRIMARY KEY NOT NULL,
  nome NVARCHAR2(255) NOT NULL,
  preco_uni NUMBER NOT NULL
);

/* Criação da tabela pecas_utilizadas */
CREATE TABLE pecas_utilizadas (
  peca_utilizada_id NUMBER PRIMARY KEY NOT NULL,
  peca_id NUMBER NOT NULL,
  ordem_id NUMBER NOT NULL,
  preco_uni NUMBER NOT NULL,
  quant_utilizada NUMBER NOT NULL
);

/* -- Adicionar restrições de chave estrangeira */
ALTER TABLE ordem_servico ADD CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id);

ALTER TABLE ordem_servico ADD CONSTRAINT fk_tecnico FOREIGN KEY (tecnico_id) REFERENCES tecnico(tecnico_id);

ALTER TABLE pecas_utilizadas ADD CONSTRAINT fk_peca FOREIGN KEY (peca_id) REFERENCES peca(peca_id);

ALTER TABLE pecas_utilizadas ADD CONSTRAINT fk_ordem_servico FOREIGN KEY (ordem_id) REFERENCES ordem_servico(ordem_id);

/* -- Garante acesso total as tabelas */
GRANT ALL ON LABDATABASE.clientes TO LABDATABASE;
GRANT ALL ON LABDATABASE.ordem_servico TO LABDATABASE;
GRANT ALL ON LABDATABASE.tecnico TO LABDATABASE;
GRANT ALL ON LABDATABASE.peca TO LABDATABASE;
GRANT ALL ON LABDATABASE.pecas_utilizadas TO LABDATABASE;

ALTER USER LABDATABASE quota unlimited on USERS;