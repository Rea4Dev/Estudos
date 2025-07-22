Tipos de Variáveis em Bancos de Dados Relacionais

**Introdução**
No universo dos bancos de dados relacionais, definir corretamente os tipos de dados para as colunas das tabelas é essencial. Os tipos de variáveis determinam os valores que podem ser armazenados, influenciando diretamente a integridade, eficiência e desempenho do banco de dados. Compreender profundamente esses tipos é fundamental para projetar estruturas robustas e eficazes.

**Categorias de Tipos de Variáveis**
Os tipos de variáveis em bancos de dados relacionais são geralmente classificados nas seguintes categorias:

---

1. **Numéricos**

   a) **Inteiros**
   - **SMALLINT**: Para números inteiros pequenos, variando de -32.768 a 32.767. Ideal para quantidades limitadas, como a idade de uma pessoa ou números de itens em estoque.

   - **INTEGER ou INT**: Números inteiros padrão, variando de -2.147.483.648 a 2.147.483.647. Comumente utilizado para identificadores únicos (IDs) e contadores.

   - **BIGINT**: Suporta números inteiros muito grandes, variando de -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807. Útil em aplicações que exigem contagens enormes, como visualizações em plataformas de grande escala.

   b) **Decimais e Ponto Flutuante**
   - **DECIMAL(p,s) ou NUMERIC(p,s)**: Números decimais exatos com precisão (p) e escala (s) definidas. Indicado para valores monetários onde a precisão é crucial, como preços e salários.

   - **REAL**: Números de ponto flutuante de precisão simples. Usado em cálculos que toleram pequenas imprecisões, como medições científicas.

   - **DOUBLE PRECISION**: Números de ponto flutuante de precisão dupla. Aplicado quando é necessária maior precisão em cálculos complexos.

---

2. **Caracteres e Strings**
   - **CHAR(n)**: Cadeia de caracteres com tamanho fixo de n caracteres. Preenche com espaços em branco se a entrada for menor que n. Utilizado para códigos padronizados, como código de países ou estados.

   - **VARCHAR(n)**: Cadeia de caracteres de tamanho variável até um máximo de n caracteres. Ideal para textos de comprimento variável, como nomes e endereços.

   - **TEXT**: Armazena cadeias de caracteres de comprimento ilimitado ou muito extenso. Adequado para campos de descrição ou conteúdos extensos.

---

3. **Datas e Horas**
   - **DATE**: Armazena datas no formato ano-mês-dia. Usado para datas de nascimento, de contratação, entre outras.

   - **TIME [ (p) ] [ WITHOUT TIME ZONE ]**: Armazena horários no formato hora:minuto:segundo, opcionalmente com precisão adicional. Útil para registrar horários de eventos.

   - **TIMESTAMP [ (p) ] [ WITHOUT TIME ZONE ]**: Combina data e hora, opcionalmente com precisão extra. Essencial para marcações de tempo em registros (logs) e transações.

   - **INTERVAL**: Representa um intervalo de tempo, como dias, horas ou minutos. Usado para calcular durações entre datas.

---

4. **Booleanos**
   - **BOOLEAN**: Armazena valores lógicos VERDADEIRO (TRUE) ou FALSO (FALSE). Usado para flags ou indicadores binários.

---

5. **Binários**
   - **BYTEA** (PostgreSQL) ou **BLOB** (MySQL): Armazena dados binários de tamanhos variados. Aplicado para arquivos, imagens e outros dados binários.

---

6. **Tipos Especializados**
   - **ENUM**: Conjunto de valores pré-definidos. Útil para campos com opções limitadas, como estado civil ('Solteiro', 'Casado').

   - **ARRAY**: Armazena uma lista de valores do mesmo tipo. Usado quando uma coluna precisa conter múltiplos valores relacionados.

   - **JSON e JSONB**: Armazena dados em formato JSON. Ideal para armazenar dados semiestruturados ou configurações.

   - **UUID**: Identificador universal único. Utilizado para chaves primárias que precisam ser únicas globalmente.

   - **GEOMETRY**: Armazena dados espaciais. Necessário para aplicações que lidam com informações geográficas.

---

**Exemplos Práticos de Implementação**
**Tabela de Clientes**

<table>
  <tr>
    <th>Coluna</th>
    <th>Tipo de Variável</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>cliente_id</td>
    <td>SERIAL ou UUID</td>
    <td>Identificador único do cliente</td>
  </tr>
  <tr>
    <td>nome</td>
    <td>VARCHAR(100)</td>
    <td>Nome completo do cliente</td>
  </tr>
  <tr>
    <td>email</td>
    <td>VARCHAR(255)</td>
    <td>Endereço de e-mail</td>
  </tr>
  <tr>
    <td>data_nascimento</td>
    <td>DATE</td>
    <td>Data de nascimento</td>
  </tr>
  <tr>
    <td>ativo</td>
    <td>BOOLEAN</td>
    <td>Status do cliente (ativo/inativo)</td>
  </tr>
</table>

**Tabela de Pedidos**

<table>
  <tr>
    <th>Coluna</th>
    <th>Tipo de Variável</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>pedido_id</td>
    <td>SERIAL ou UUID</td>
    <td>Identificador único do pedido</td>
  </tr>
  <tr>
    <td>cliente_id</td>
    <td>INTEGER ou UUID</td>
    <td>Referência ao cliente (chave estrangeira)</td>
  </tr>
  <tr>
    <td>data_pedido</td>
    <td>TIMESTAMP</td>
    <td>Data e hora do pedido</td>
  </tr>
  <tr>
    <td>valor_total</td>
    <td>DECIMAL(10,2)</td>
    <td>Valor total do pedido</td>
  </tr>
  <tr>
    <td>status</td>
    <td>ENUM('Pendente', 'Processando', 'Concluído')</td>
    <td>Status do pedido</td>
  </tr>
</table>


