---
data_criacao: 19-08-2025
flashcards: Não feito
revisão: Não feita
---
# 🔎 Por que *System.out.println(pessoa1)* funciona sem eu chamar **toString()**?

`src/br/com/rengcarv/hello/HelloWorld.java`
```Java
package br.com.rengcarv.hello;

public class HelloWorld{
    public static void main(String[] args){
        Pessoa pessoa1 = new Pessoa("Renan", 24);
        System.out.println(pessoa1);
    }
}
```

1. Em Java, há o **Object**, e **toda classe herda dele** (mesmo que você não escreva isso).

2. A classe Object **já define um método**:
```Java
public String toString()
```
Este método retorna ==nome da classe + hash==: *br.com.rengcarv.hello.Pessoa@6a6824be*

3. Quando você cria **seu próprio toString()** na classe Pessoa, você **sobrescreve (substitui) o comportamento padrão**.

4. O método *println(Object x)* <small>(da classe PrintStream e que é o tipo de System.out)</small> *chama automaticamente x.toString()*.

5. Então, quando você faz:
```Java
System.out.println(pessoa1);
```

o Java na verdade executa:
```Java
System.out.println(pessoa1.toString());
```


---

# 🔎 O que é @Override?

`src/br/com/rengcarv/hello/Pessoa.java`
```Java
package br.com.rengcarv.hello;

public class Pessoa{
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome(){
        return nome;
    }

    public int getIdade(){
        return idade;
    }

    @Override
    public String toString(){
        return "Sou " + nome + " e tenho " + idade + " anos";
    }
}
```

``@Override`` é uma anotação que você coloca acima de um método.

Ela avisa o compilador:
> "Esse método está **sobrescrevendo** (override) **um método herdado de uma superclasse ou interface**."

## Por que usar?

1. **Protege contra erros de digitação**:
Se você escrever public String tostring() (com s minúsculo), sem @Override compila, mas nunca será chamado. Com @Override, o compilador reclama.

2. **Clareza de intenção**:
Outro programador sabe que você está substituindo um método existente, e não criando um novo sem querer.