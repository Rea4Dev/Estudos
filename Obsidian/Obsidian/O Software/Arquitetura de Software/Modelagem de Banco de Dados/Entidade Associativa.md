- *Entidade Associativa* – Um relacionamento comum apenas liga entidades, mas se ele possuir **atributos próprios**, ele se torna uma entidade associativa. 
Também se o relacionamento for **muitos-para-muitos** (N:N) e precisa ser normalizado.
![[Pasted image 20250222163241.png | center | 300]]
<center><small><small>Aqui, `Matrícula` não é apenas um relacionamento entre `Aluno` e `Curso`, mas também uma entidade que pode ter atributos próprios, como `data_matricula`, `status` e `nota_final`.</center></small></small>

![[Pasted image 20250222173611.png]]

🔻 **Equivalências nos Modelos:**
- **Modelo Conceitual** → Representada como um retângulo conectado a duas ou mais entidades, indicando um relacionamento N:N.
- **Modelo Lógico** → Representada como uma _Tabela Associativa_ contendo as chaves estrangeiras das entidades relacionadas.
- **Modelo Físico** → Criada como uma _Tabela de Junção_ com as FKs das entidades, geralmente formando uma **Chave Primária Composta**.