Imagine que temos dois vetores e queremos utilizar uma função para preencher todas as posições do vetor com zero. 
```C
main(){
	int v[10];
	int x[20];
	inic1(v);    /* Iniciar o vetor v usando a função inic1 */
	inic2(x);    /* Iniciar o vetor x usando a função inic2 */
}

void inic1(int s[10]){
	int i;
	for(i=0;i<10;i++)
		s[i]=0;
}

void inic2(int s[20]){
	int i;
	for(i=0;i<20;i++)
	s[i]=0;
}
```

A função acima funciona bem para o caso, mas ela poderia ser melhorada *utilizando apenas uma função* para preencher os dois vetores. Para isso, seria necessário saber o seguinte:
- Dentro de uma função não é possível saber com quantos elementos foi declarado um vetor que foi passado como argumento para essa função, mas sim qual o tipo dos seus elementos. 
![[Pasted image 20250205210813.png | center | 400]]
- Logo, mantenha o tipo do argumento correspondente ao tipo do parâmetro <small>(pois o compilador consegue compará-los)</small>.
- Indique no parâmetro o numero de elementos que o vetor tem <small>(pois o compilador não consegue saber sozinho)</small>.