Em *validações específicas* onde queremos montar uma estrutura condicional que apenas *executa determinada ação se positiva a condição*, utilizamos a estrutura condicional If sozinha. 
Como mostrado acima, não caia no erro de achar que esta estrutura condicional não tem valor sozinha, pelo contrário. 

---
## Unicidade
É importante estar ciente da possibilidade de diferença de sintaxe relativo a quantas instruções estão associadas: 
- Se uma única instrução, não faz-se necessário a utilização da criação de bloco ~~{ }~~.
- Se mais de uma, faz-se necessário a utilização da criação de bloco { }.
<center><h3>Sintaxe única instrução</h3></center>
```c
if (condição)
	instrução;

```

<center><h3>Sintaxe mais de uma instrução</h3></center>
```c
if (condição){
	instrução n;
}
```
