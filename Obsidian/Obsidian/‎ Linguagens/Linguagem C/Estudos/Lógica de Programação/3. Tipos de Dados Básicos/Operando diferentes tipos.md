Observe o código abaixo e veja que estamos tentando dividir um inteiro por um float:
```c
#include <stdio.h>

  

int main(){

    int A =7;

    float B =3;

    printf("%f\n",A/B);

}
```

O código acima não dará erro, pelo contrário, ele exibirá o resultado correto (2.3 em dízima).

Não pense que em casos como este ocorre erro de compilação, isso te levaria a sempre tornar os tipos iguais para poder operá-los, o que aqui prova-se não ser necessário.

A operação de diferentes tipos ocorre sim, entretanto, o resultado sempre será do tipo de maior força:

<table> 

<thead> 
<tr> 
<th>Tipo</th> 
<th>Tipo</th> 
<th>Resultado</th> 
</tr> 
</thead>


<tbody> 
<tr> 
<td>int</td> 
<td>float</td> 
<td>float</td> 
</tr>
<tr> 
<td>int</td> 
<td>double</td> 
<td>double</td> 
</tr> 
</tbody> 

</table>

Lembre sempre de *respeitar o tipo do resultado!* 
Assim sendo, referencie-o de maneira correta quando utilizar o "%".