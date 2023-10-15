SELECT
  t.nome AS nome_tecnico,
  os.ordem_id AS numero_ordem,
  os.descricao_problema AS problema
FROM
  tecnico t
  JOIN ordem_servico os ON t.tecnico_id = os.tecnico_id;