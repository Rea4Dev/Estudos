![[Pasted image 20250218123426.png]]

![[Pasted image 20250218130920.png | center | 400]]

![[Pasted image 20250218131549.png | center]]

A consulta SQL pode ser efetuada sempre juntando estes elementos, tal como:
```SQL
SELECT * FROM vendas LIMIT 10
```
---
1. Da tabela vendas, obtenha os 10 primeiros elementos levando em consideração apenas codigo, qty, ship_country e ordenados em ordem crescente de data.
```SQL
SELECT codigo, qty, ship_country FROM vendas ORDER BY date ASC LIMIT 10
```

2. Da tabela vendas, obtenha os 10 primeiros elementos levando em consideração apenas codigo, qty, ship_country e ordenados em ordem crescente de data e apenas para dias acima de 2022-06-28.
```SQL
SELECT codigo, qty, ship_country FROM vendas WHERE date >= '2022-06-29' ORDER BY date ASC LIMIT 10
```

3. Na tabela vendas com os campos date e qty, desejo saber o total de quantidades vendidas por dia, do mais atual ao mais antigo.
```SQL
SELECT date, SUM(qty) FROM vendas GROUP BY date ORDER BY date DESC
```

4. Suponhamos que precisamos saber os produtos que tiveram o maior volume financeiro de vendas, ou seja, os produtos que trouxeram mais receita bruta para nossa loja. Algumas das informações encontra-se em tabelas diferentes.
```SQL
SELECT pr.produto, SUM(ve.qty*pr.preco)
FROM produtos pr
JOIN vendas ve
ON pr.codigo = ve.codigo
GROUP BY pr.produto
```