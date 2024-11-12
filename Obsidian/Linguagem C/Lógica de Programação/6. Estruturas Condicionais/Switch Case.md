
> [!Important] Descrição
> A instrução switch adapta-se particularmente à tomada de decisões em que o número de possibilidades é elevado (em geral maior que 2, se não usa-se o if-else), de forma a reduzir a complexidade de if-else consecutivos e encadeados.


```C
    switch (opcao){
        case 'n':
            instruções;
            break;
            
        default:
            break;
    }
```


> [!Tip] Inline
> Não é necessária a criação de um bloco { } após um case se este for constituído por mais de uma instrução.

```C
case 'n': instrução; break;
```

---


> [!Tip] break
> O último case ou o default de um switch não necessita de break, porque depois de executar as instruções associadas ao último case termina a instrução switch.

![[Pasted image 20241111135524.png | center | 400]]

---

> Ao contrário do if, que permite definir bandas de valores (x>=10 && x<=120), o switch só admite valores constantes predefinidos dos tipos char, int ou long.
