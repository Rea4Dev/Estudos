---
data_criacao: 15-08-2025
flashcards: Não feito
revisão: Não feita
---
Como conteitos básicos do Java, temos:

1.  Java exige que **todo código esteja dentro de uma classe**.
```Java
package br.com.rengcarv.hello;

public class Hello{

}
```

2. O ponto de entrada do programa é o método `public static void main(String[] args)`.
3. O *nome* do arquivo deve ser igual ao nome da classe pública e deve seguir *PascalCase*.
```Java
package br.com.rengcarv.hello;

public class Hello{
	public static void main (String[] args){
	
	}
}
```

(faça um hello world, continue o que o gpt pede, dps pergunte pq esse String { }  e pq tem que chamar o package)

# String[ ] args
É um **parâmetro obrigatório** que permite que o programa receba **argumentos da linha de comando** quando ele é executado. Ou seja, se você rodar seu programa pelo terminal e passar alguns valores, eles vão aparecer dentro desse array `args`.

Imagine que você quer que seu programa faça algo diferente dependendo do que o usuário digitar ao iniciar o programa. Por exemplo:
```Java
java Hello Renan Gabriel
```

Nesse caso, o array args vai conter:
```Java
args[0] = "Renan"
args[1] = "Gabriel"
```

Você poderia usar algo assim
```Java
public class Hello {
    public static void main(String[] args) {
        if (args.length > 0) {
            System.out.println("Olá, " + args[0] + "!");
        } else {
            System.out.println("Olá, mundo!");
        }
    }
}
```

## E se não usar?
Se você não pretende passar argumentos pela linha de comando, pode deixar o `args` ali sem usar. Ele é **obrigatório na assinatura do método** `main`, porque é o ponto de entrada padrão para programas Java. A *JVM (Java Virtual Machine) espera encontrar esse método* com essa assinatura para iniciar o programa.