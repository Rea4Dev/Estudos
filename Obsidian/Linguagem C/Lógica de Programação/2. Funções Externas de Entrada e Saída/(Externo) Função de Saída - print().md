Na realidade, C é uma linguagem com *muitas poucas palavras reservadas*, desta forma, não é de se surpreender que C não possua mecanismos de Entrada e Saída incorporados. Em vez disso, *ela recorre à sua potente biblioteca de funções* para fornecer este tipo de serviço.

Uma das funções que permite a escrita na tela é a função printf = print + **formatado**. 
```
printf()
```

> - "_Sempre que queremos tratar conjuntos de caracteres temos que colocá-los entre aspas, para que sejam considerados como um todo_".

Dentro dos parênteses é feita a comunicação com a função. Nesse caso passamos a string (conjunto de caracteres) que queremos que seja escrita:
```
printf("Hello, World!");
```

Em C, cada instrução deve ser terminada com um ponto-e-vírgula.

---
# Revisão Espaçada
#flashcards/Logica_de_programação 

Por que é printf e não print;;Pois printf = print + **formatado**.<br>Formatado pois, o uso do **%** e diversos outros artifícios (como %.2f) são possíveis pois printf é formatado.
<!--SR:!2024-10-29,4,270-->