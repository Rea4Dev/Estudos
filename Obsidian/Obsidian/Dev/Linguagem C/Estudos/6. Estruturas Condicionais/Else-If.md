Permite **aninhar** a estrutura condicional *if-else* quantas vezes for necessário.

---
## Unicidade
É importante estar ciente da possibilidade de diferença de sintaxe relativo a quantas instruções estão associadas: 
- Se uma única instrução, não faz-se necessário a utilização da criação de bloco ~~{ }~~.
- Se mais de uma, faz-se necessário a utilização da criação de bloco { }.
<center><h3>Sintaxe única instrução</h3></center>
```c
if (condição)
	instrução;
else if
	instrução;
```

<center><h3>Sintaxe mais de uma instrução</h3></center>
```c
if (condição){
	instrução n;
}else if{
	instrução n;
}
```
