---
data_criacao: 28-08-2025
flashcards: Não feito
revisão: Não feita
---

---
# Usos avançados do this

1. *Passar a instância atual como argumento*
Podemos usar this para passar o objeto atual a outro método ou classe.
```Java
public void apresentar() {
    Util.imprimir(this); // passa a própria instância
}
```

2. *Encadear construtores*
Em classes com múltiplos construtores, this(...) pode ser usado para chamar outro construtor da mesma classe, evitando repetição de código.
```Java
public class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome){
        this(nome, 0); // chama o outro construtor
    }

    public Pessoa(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }
}
```

3. *Retornar a própria instância (padrão Fluent Interface)*
Muito usado em builders e métodos encadeados:

```Java
public class Pessoa {
    private String nome;

    public Pessoa setNome(String nome){
        this.nome = nome;
        return this; // retorna a própria instância
    }
}
```

Uso:
```Java
Pessoa p = new Pessoa().setNome("Renan");
```

---