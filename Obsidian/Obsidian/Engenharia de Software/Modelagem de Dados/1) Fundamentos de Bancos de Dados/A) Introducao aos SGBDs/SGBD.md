---
Ramo: Engenharia de Software
Campo: Modelagem de Dados
Assunto: Fundamentos de Bancos de Dados
Tópico: Introdução aos SGBDs
---
# SGBD

## Definição Conceitual

Um SGBD *é um software cuja finalidade é gerenciar as informações de um banco de dados* (também chamada de base de dados) segundo **Navathe e Ramez** (2005), e que também devem *organizar, acessar, controlar e proteger* as informações contidas no banco de dados. 

O SGBD tem por objetivo **facilitar a vida do programador ou analista**, deixando *livre para pensar na modelagem e não ficar pensando em questões técnicas de armazenamento de dados* (sendo esta uma das funções do SGBD).

### Abstração

De acordo com **Navathe e Ramez** (2005), um SGBD oferece aos usuários uma representação conceitual de dados, *omitindo vários detalhes, por exemplo, como os dados realmente são guardados ou como as transações são realizadas no banco de dados*. Essa representação de modelo de dados é informalmente conhecida como **abstração de dados**.

## Aplicação

Quando nos referenciamos ao termo aplicação, estamos mencionando os *softwares que estarão se beneficiando dos dados inseridos em um banco de dados*. 

Por exemplo, como citado anteriormente, o sistema do setor financeiro de uma faculdade utiliza as informações arquivadas no banco de dados do sistema de controle acadêmico da secretaria da faculdade, ou seja, podemos dizer que existe um banco de dados único e centralizado para diversas aplicações utilizarem.

## Constituição

O SGBD pode ser distribuído por diversos computadores, *no mesmo local ou até em locais diferentes* (espaços, cidades, países). Caso o SGBD esteja em locais físicos diferentes, cada um passa a receber o nome de **nó**, e uma operação realizada no banco de dados pode ser executada em um ou em mais nós. 

Os *computadores e seus SGBDs se comunicam através de diversos protocolos de comunicação*, de acordo com **Navathe e Ramez** (2005).

> [!Tip] Veja que
> - O SGBD é projetado para gerenciar grandes volumes de informações, chegando a 1.152.921.504.606.846.976 bytes ou exabyte. 
> <br>
> - O SGBD tem como finalidade a garantia de que as informações que foram inseridas no banco de dados estejam seguras, protegendo de ataques indevidos quanto ao seu acesso ou problemas ocasionados por erros de software ou hardware.

## Acesso ao Banco de Dados

O acesso ao banco de dados por diversas aplicações *necessita de regras específicas para garantir tanto a segurança quanto a integridade das informações inseridas*. 

São diversos programas que executam essas garantias, conhecidos como **SGBD** ou Sistema Gerenciador de Banco de Dados. Observe na Figura abaixo como é o esquema do SGBD em relação às aplicações e ao banco de dados.

![[Pasted image 20250701220648.png | center | 400]]

## Transação

Segundo **Navathe e Ramez** (2005), uma transação *é um processo ou um determinado programa que pode incluir vários bancos de dados ou somente uma parte do banco de dados*, realizando atividades como **consultas**, **alterações** e até **exclusão** de informações da base de dados.

Para **Korth, Silberschatz e Sudarshan** (2012, p. 393), uma transação é uma *consequência da efetivação de um programa* (ou uma rotina) que acessa e possivelmente atualiza vários itens de dados. *A transação é o resultado da execução de um programa de usuário escrito em uma linguagem* de manipulação de alto nível ou em uma linguagem de programação, como Java, C# ou *SQL*, entre outras.

## ACID

**Navathe e Ramez** (2005) afirmam que um SGBD possui as funções de permitir aos seus usuários a *pesquisa* em um banco de dados para recuperar uma determinada informação, alterar e gerar relatórios das informações. 

Outras funções que podemos destacar do SGBD são a *proteção e a recuperação dos dados* quando houver problemas de hardware ou software, *a segurança* a acessos indevidamente autorizados, a possibilidade de *compartilhar dados*, a administração da redundância e a restrição de integridade dos componentes do banco. 

Conforme **Guimarães** (2003), o *conjunto de requisitos de um SGBD* recebe o nome de **ACID** dos termos em inglês: 
- **A**_tomicity_
- **C**_onsistency_
- **I**_solation_
- **D**_urability_

*O SGBD escolhido pela empresa deve possuir os fatores ACID para garantir que uma transação no banco de dados seja realizada com sucesso*. O SGBD deve garantir várias propriedades durante uma transação.

### Atomicidade

Garante que **nenhuma ou a totalidade das operações da transação sejam realizadas com sucesso**. 

Por isso atomicidade, indivisível. Ou é tudo ou nada.

Suponha que estamos aumentando os salários dos funcionários (este aumento é uma alteração em uma tabela e, neste caso, é uma transação) e que durante a atualização faltou luz. Somente uma parte dos funcionários receberá o aumento no salário, caso não haja a verificação de atomicidade. 

Conforme Korth, Silberschatz e Sudarshan (2012), a ideia por trás da garantia de atomicidade é que *o sistema de banco de dados mantenha um registro (em disco) dos antigos valores de quaisquer dados a serem alterados. Caso haja algum problema durante a realização da transação, o SGBD restabelece os dados antigos*, como se nunca tivessem sido modificados.

### Consistência

**Preserva as regras impostas no banco de dados**. Assim que a transação for finalizada, todos os dados devem estar íntegros.

Um exemplo seria a soma de dois valores. Após uma transação, os valores iniciais não podem ser alterados, mas, é claro, se esta for a regra determinada no banco de dados.

A consistência é a garantia de manter os dados íntegros durante e com a finalização da transação realizada no banco de dados.

### Isolamento

É a segurança de que **uma transação não interfira no trabalho de outra**. *Somente após o término de uma transação, ela estará liberada para receber outras*. 

Korth, Silberschatz e Sudarshan (2012) afirma que, mesmo asseguradas as propriedades de atomicidade e consistência para cada transação, a intercalação das operações de várias transações concorrentes pode resultar em inconsistências (erros nos resultados e/ou nos dados). Alterações feitas por transações simultâneas precisam ser isoladas das alterações feitas por qualquer outra transação simultânea.

### Durabilidade

Garante que **uma vez que uma transação foi concluída com sucesso, seus efeitos serão permanentes no banco de dados**, mesmo em casos de falhas de sistema ou quedas de energia.

Segundo Korth, Silberschatz e Sudarshan (2012), o SGBD deve assegurar que os resultados de uma transação validada nunca sejam perdidos, *por meio de técnicas como logs de transação* e *gravação forçada* (force-write) no disco *antes da confirmação da transação*.

#### Log de Transação

O SGBD, para recuperar-se de uma transação com falhas, possui um log para registrar todas as operações realizadas em dados. Funciona como um *histórico das modificações*. Caso haja erro, através do log, haverá a **recuperação dos dados** para que eles voltem ao estado inicial.

## Características

As principais características do uso de um banco de dados, conforme Navathe e Ramez (2005), são as seguintes: 

- **Natureza autodescritiva do SGBD**.
Ou seja, o SGBD não guarda só o dado em si, mas também a descrição deste dado.

- **Isolamento entre os programas, os dados e a abstração dos dados**.
As aplicações não precisam saber como os dados estão sendo guardados lá no fundo. 
Como exemplo, temos um carro. Você vê a gasolina, liga o farol e controla o carro pela interface sem precisar saber de toda a engenharia do mobilística.
Então com a abstração, ele esconde os detalhes de como os dados são fisicamente armazenados ou como as transações são processadas.
Isso inclusive ajuda na manutenção e versionamento. Em outras palavras, com tanto que a interface para o motorista fosse a mesma, poderíamos alterar até mesmo o motor que ele não perceberia (há ressalvas, é claro).

- **Suporte a diversas visões dos dados inseridos no banco de dados**.
Como a aplicação vê a abstração, então quer dizer que aplicações diferentes podem ter interfaces diferentes com a mesma base de dados.
Muito necessário para filtrar dados (ou seja, a aplicação exibir o que deve) e para segurança (exibir apenas o que deve).
Além de tudo, simplifica o código. Uma consulta complexa pode ser encapsulada em uma mera visão, e essa visão pode ser consumida por uma aplicação posteriormente através de um Select.

- **Transações para diversos usuários do banco e a possibilidade de compartilhar os dados da base de dados.**

## Visão

Uma visão (ou view) *pode ser uma parte de uma base de dados, podendo ser resultantes de pesquisas que retornam parte das informações armazenadas*.

Um SGBD com suporte a múltiplas visões deve proporcionar facilidades para a definição de diversas visões.

O controle de concorrência é o fator primordial para que o compartilhamento de dados e as transações sejam realizados com sucesso para todos aqueles que utilizam o banco de dados. Ao criar visões, podemos criar filtros protegendo certas colunas e tornando o código mais simplificado.

## Manipulação de Estrutura

Uma característica essencial de um SGBD é possuir uma *ampla gama de possibilidades para definir a estrutura da base de dados e poder aplicar restrições* no banco. 

Os programas de aplicação que irão acessar a base de dados devem ser criados independentemente da estrutura do banco. 



