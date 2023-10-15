/* -- Insere dados na tabela cliente */
INSERT INTO clientes (cliente_id, nome, endereco, email, telefone)
VALUES
  (1, 'João Silva', 'Rua A, 123', 'joao@email.com', 1234567890),
  (2, 'Maria Santos', 'Av. B, 456', 'maria@email.com', 9876543210),
  (3, 'Carlos Oliveira', 'Rua C, 789', 'carlos@email.com', 5678901234);

/* -- Insere dados na tabela tecnico */
INSERT INTO tecnico (tecnico_id, nome, especialidade, email, telefone)
VALUES
  (1, 'Ana Costa', 'Redes', 'ana@email.com', 1112223333),
  (2, 'Paulo Rocha', 'Hardware', 'paulo@email.com', 2223334444),
  (3, 'Marta Fernandes', 'Software', 'marta@email.com', 3334445555);

/* -- Insere dados na tabela ordem_servico */
INSERT INTO ordem_servico (ordem_id, cliente_id, tecnico_id, data_abertura, data_conclusao, status, descricao_problema, solucao, custo_total)
VALUES
  (1, 1, 1, TIMESTAMP '2023-10-15 09:00:00', TIMESTAMP '2023-10-17 15:30:00', 'Concluída', 'Problemas de rede', 'Substituição do roteador', 120.50),
  (2, 2, 2, TIMESTAMP '2023-10-16 10:15:00', TIMESTAMP '2023-10-18 14:45:00', 'Concluída', 'Falha de hardware', 'Substituição da placa-mãe', 200.00),
  (3, 3, 3, TIMESTAMP '2023-10-17 08:30:00', TIMESTAMP '2023-10-19 17:00:00', 'Em andamento', 'Problemas de software', 'Atualização do sistema', 75.75);

/* -- Insere dados na tabela peca */
INSERT INTO peca (peca_id, nome, preco_uni)
VALUES
  (1, 'Roteador', 50.00),
  (2, 'Placa-mãe', 100.00),
  (3, 'Memória RAM', 30.00);

/* -- Insere dados na tabela pecas_utilizadas */
INSERT INTO pecas_utilizadas (peca_utilizada_id, peca_id, ordem_id, preco_uni, quant_utilizada)
VALUES
  (1, 1, 1, 50.00, 1),
  (2, 2, 2, 100.00, 1),
  (3, 3, 2, 30.00, 2),
  (4, 1, 3, 50.00, 2),
  (5, 3, 3, 30.00, 1);