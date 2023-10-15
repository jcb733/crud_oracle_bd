SELECT os.ordem_id AS codigo_pedido,
       pu.peca_utilizada_id AS codigo_item_pedido,
       pu.peca_id AS codigo_produto,
       p.nome AS descricao_produto,
       pu.quant_utilizada AS quantidade,
       p.preco_uni AS valor_unitario,
       (pu.quant_utilizada  p.preco_uni) AS valor_total
FROM pecas_utilizadas pu
INNER JOIN ordem_servico os ON pu.ordem_id = os.ordem_id
INNER JOIN peca p ON pu.peca_id = p.peca_id
ORDER BY os.ordem_id, p.nome