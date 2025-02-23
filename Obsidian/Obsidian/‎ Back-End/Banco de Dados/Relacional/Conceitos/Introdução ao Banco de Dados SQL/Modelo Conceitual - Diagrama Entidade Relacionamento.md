<center><h1>📌 Modelo Conceitual</h1></center>

O Modelo Conceitual representa as *entidades* e seus *relacionamentos* de forma gráfica, geralmente usando um *Diagrama Entidade-Relacionamento (DER)*.

💡 Essa etapa *não define tabelas ou colunas*, apenas *o que será armazenado e como se relaciona*.

## 🔹 Elementos principais do DER:

- *Entidades* – Representam os principais objetos do banco (ex: `Cliente`, `Carro`, `Contrato`). Representados por retângulo.
	- *Instâncias*: São os dados registrados nas entidades.

- *Atributos* – São as características das entidades (ex: `nome`, `CPF`, `modelo`, `placa`). Representado por círculos.
	- *Atributo Identificador | Chave Primária*: Atributo de uma entidade que tem a função de **identificá-la de forma única**.  Não pode ser nulo, deve ser imutável. Aqui representado por uma bolinha preta.
	- *Chave Composta*: Dois ou mais atributos combinados identificam a entidade. **(Matrícula, Disciplina)** em uma tabela que registra quais alunos cursam quais matérias.
	- *Chave Substituta*: Criada artificialmente, sem significado real para os dados.

---

- *Relacionamentos* – Definem como as entidades se conectam (ex: "Cliente faz um **Aluguel**"). Representados por losango.
![[Pasted image 20250222170412.png | center]]

---

- *Generalização/Especialização* – Representa uma hierarquia entre entidades.
	- **Generalização** ocorre quando entidades diferentes compartilham características em comum, então elas são agrupadas em uma entidade mais genérica.
	- **Especialização** é o oposto: uma entidade genérica pode ser dividida em subtipos mais específicos, que possuem atributos ou comportamentos próprios.
![[Pasted image 20250222170955.png | center ]]

No modelo de [[Engenharia de Informaçao]] representamos:
![[Pasted image 20250223172831.png]]

---

- *Entidade Associativa* – Um relacionamento comum apenas liga entidades, mas se ele possuir **atributos próprios**, ele se torna uma entidade associativa. 
Também se o relacionamento for **muitos-para-muitos** (N:N) e precisa ser normalizado.
![[Pasted image 20250222163241.png | center | 300]]
<center><small><small>Aqui, `Matrícula` não é apenas um relacionamento entre `Aluno` e `Curso`, mas também uma entidade que pode ter atributos próprios, como `data_matricula`, `status` e `nota_final`.</center></small></small>

![[Pasted image 20250222173611.png]]

