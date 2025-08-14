---
data_criacao: 14-08-2025
flashcards: Não feito
revisão: Não feita
---
```Java
class NomeDaClasse {
	public NomeDaClasse() { /* Construtor */
	
	}
}

NomeDaClasse variavel = new NomeDaClasse();
```

Se não criarmos o construtor, ele será considerado por padrão da mesma forma.

```Java
class NomeDaClasse {
	
}

NomeDaClasse variavel = new NomeDaClasse();
```

---

# Manipulando

![[Pasted image 20250814104135.png]]

---

Aqui, obrigamos um tipo a ser informado na hora de instanciar uma variável.
- "this" é para referenciar o atributo (linha 2). 
- O "tipo" sem this é referente ao parâmetro do construtor.
![[Pasted image 20250814104009.png]]

Na manipulação, fica
![[Pasted image 20250814104027.png]]