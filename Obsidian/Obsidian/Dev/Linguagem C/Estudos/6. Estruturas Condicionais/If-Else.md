Permite indicar quais as circunstâncias em que se deve executar determinado *conjunto de instruções*.

><small>Sempre que existam instruções if-else encadeadas, cada else pertence sempre ao último if sem else.</small>

![[Pasted image 20241111115648.png | center | 120]]

---
## Unicidade
É importante estar ciente da possibilidade de diferença de sintaxe relativo a quantas instruções estão associadas: 
- Se uma única instrução, não faz-se necessário a utilização da criação de bloco ~~{ }~~.
- Se mais de uma, faz-se necessário a utilização da criação de bloco { }.
<center><h3>Sintaxe única instrução</h3></center>
```c
if (condição)
	instrução;
else
	instrução;
```

<center><h3>Sintaxe mais de uma instrução</h3></center>
```c
if (condição){
	instrução n;
}else{
	instrução n;
}
```
