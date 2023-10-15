DECLARE
  VCOD_CLIENTE NUMBER;
  VCOD_ORDEM NUMBER;
  VCOD_TECNICO NUMBER;
  VCOD_PECA NUMBER;
BEGIN
  -- Inserir dados na tabela clientes
  VCOD_CLIENTE := clientes_seq.NEXTVAL;
  INSERT INTO clientes (cliente_id, nome, endereco, email, telefone)
  VALUES (VCOD_CLIENTE, 'João Silva', 'Rua A, 123', 'joao@email.com', 1234567890);

  -- Inserir dados na tabela ordem_servico
  VCOD_ORDEM := ordem_servico_seq.NEXTVAL;
  SELECT tecnico_id INTO VCOD_TECNICO FROM tecnico WHERE nome = 'Ana Costa';
  INSERT INTO ordem_servico (ordem_id, cliente_id, tecnico_id, data_abertura, data_conclusao, status, descricao_problema, solucao, custo_total)
  VALUES (VCOD_ORDEM, VCOD_CLIENTE, VCOD_TECNICO, TO_TIMESTAMP('2023-10-15 09:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('2023-10-17 15:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Concluída', 'Problemas de rede', 'Substituição do roteador', 120.50);

  -- Inserir dados na tabela peca
  VCOD_PECA := peca_seq.NEXTVAL;
  INSERT INTO peca (peca_id, nome, preco_uni)
  VALUES (VCOD_PECA, 'Roteador', 50.00);

  -- Inserir dados na tabela pecas_utilizadas
  INSERT INTO pecas_utilizadas (peca_utilizada_id, peca_id, ordem_id, preco_uni, quant_utilizada)
  VALUES (pecas_utilizadas_seq.NEXTVAL, VCOD_PECA, VCOD_ORDEM, 50.00, 1);
END;
/

  -- Inserir dados na tabela tecnico
  VCOD_TECNICO := tecnico_seq.NEXTVAL;
  INSERT INTO tecnico (tecnico_id, nome, especialidade, email, telefone)
  VALUES (VCOD_TECNICO, 'Maria Santos', 'Redes', 'maria@email.com', 1234567890);
END;
