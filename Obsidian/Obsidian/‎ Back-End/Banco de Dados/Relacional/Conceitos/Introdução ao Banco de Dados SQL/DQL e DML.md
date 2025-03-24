# DQL e DML - A Arte de Consultar e Manipular Dados
O DQL (Data Query Language) é a parte do SQL que se dedica à extração e visualização dos dados que você precisa. 


- **SELECT**: Seleciona colunas da tabela. Se possuir <strong>*</strong> significa todas colunas. 
```SQL
SELECT test_id, mmc, name, datetime_finish
```
```SQL
SELECT *
```
<small>Não faz sentido utilizar este comando sozinho, pois estaria mandando selecionar as colunas mas de qual tabela? Necessitaria do próximo, o FROM.</small>



- **FROM**: Especifica a tabela de onde os dados serão recuperados
```SQL
SELECT test_id, mmc, name, datetime_finish FROM its.its_test
```
```SQL
SELECT * FROM its.its_test
```
<small>No FROM, usamos <strong>ITS<big><big><big>.</big></big></big></strong> antes de ITS_TEST pois esta tabela está dentro das tabelas do usuário ITS.<br>Desta forma, para acessas tabelas de usuários deve utilizar <strong>USUARIO<big><big><big>.</big></big></big></strong></small>



- **WHERE**: Aplica uma condição aos registros recuperados
```SQL
SELECT * FROM its.its_actions
WHERE status = 'PASSED'
```
<small>Em SQL usa-se apenas aspas simples para strings.</small>



- **ORDER BY**: Ordena os resultados com base em uma ou mais colunas
```SQL
SELECT * FROM its.its_actions
WHERE status = 'PASSED'
ORDER BY datetime_start ASC
```
<small>É possível ainda adicionar ASC e DESC a depender se quer crescente ou decrescente.</small>



- **GROUP BY**: Agrupa os registros que têm valores idênticos em colunas especificadas. Usado geralmente para permitir funções agregadas.
	- SUM
	- COUNT
	- AVG
	- MAX e MIN
<center>
<table border="1">
  <tr>
    <th>i_cliente_cliente</th>
    <th>s_nome_cliente</th>
    <th>s_cpf_cliente</th>
    <th>d_nasc_cliente</th>
    <th>i_tipo_cliente</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Braum</td>
    <td>00000000000</td>
    <td>1978-03-07 00:00:00</td>
    <td>4</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Aurélion</td>
    <td>0101010101</td>
    <td>1948-03-07 00:00:00</td>
    <td>3</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Tristana</td>
    <td>0202020202</td>
    <td>1918-03-07 00:00:00</td>
    <td>3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Karma</td>
    <td>0303030303</td>
    <td>2005-03-05 00:00:00</td>
    <td>1</td>
  </tr>
</table></center>
```SQL
SELECT i_tipo_cliente, count(i_cliente_cliente) as Quantidade
FROM tabela_cliente
group by i_tipo_cliente
```
<center>
<table border="1">
  <tr>
    <th>i_tipo_cliente</th>
    <th>Quantidade</th>
  </tr>
  <tr>
    <td>1</td>
	<td>1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
  </tr>
  <tr>
    <td>4</td>
    <td>1</td>
  </tr>
</table>
</center>



- **HAVING**: Aplica uma condição aos grupos criados pelo `GROUP BY`. Funciona como um pós filtro (where filtraria antes do agrupamento e having filtraria depois).


[Caso tenha dificuldades com a funcionamento dos Joins, clique aqui](https://www.youtube.com/watch?v=Yh4CrPHVBdE)
- **JOIN**: Combina registros de duas ou mais tabelas com base em uma condição
    
    - **INNER JOIN**: Retorna registros que têm correspondência em ambas as tabelas
        
    - **LEFT JOIN**: Retorna todos os registros da tabela à esquerda e os correspondentes da tabela à direita
        
    - **RIGHT JOIN**: Retorna todos os registros da tabela à direita e os correspondentes da tabela à esquerda
        
    - **FULL JOIN**: Retorna registros quando há correspondência em uma das tabelas
![[Imagem do WhatsApp de 2025-02-21 à(s) 13.37.12_d46cc056.jpg | center | 312]]


- **DISTINCT**: Remove duplicatas dos resultados


- **LIMIT**: Restringe o número de registros retornados
