Uma constante não é mais que um nome correspondente a um valor fixo (não se pode alterar ao longo de uma execução).

>As constantes devem ser declaradas fora das funções, de forma a serem “visíveis” por todo o código do programa. Normalmente a sua definição é realizada imediatamente após as linhas dos includes

A definição de constantes pode ser realizada de duas maneiras distintas:

•Através da palavra reservada const ;
```C
const int num1 = 12;
```

•Através da diretiva de pré-processamento define
```C
#define num1 12
```

___
## Diferenças entre const e define

<center>
<table>
        <tr>
            <th>const</th>
            <th>#define</th>
        </tr>
        <tr>
            <td>Existe fisicamente em uma posição de memória.</td>
            <td>Não existe fisicamente em memória, seu valor é substituído na fase de pré-processamento.</td>
        </tr>
        <tr>
            <td>Faz parte das palavras reservadas da linguagem C.</td>
            <td>É uma diretiva de pré-processamento.</td>
        </tr>
        <tr>
            <td>Não há substituição automática no código.</td>
            <td>O pré-processador substitui todas as ocorrências do símbolo pelo valor definido antes da compilação.</td>
        </tr>
        <tr>
            <td>Fica com o tipo definido na declaração.</td>
            <td>O tipo é determinado pela expressão que aparece na definição.</td>
        </tr>
        <tr>
            <td>Segue a sintaxe da linguagem C e é finalizada com ponto e vírgula.</td>
            <td>Não faz parte da linguagem C e não é seguida de ponto e vírgula.</td>
        </tr>
    </table>
    </center>

	As constantes definidas com o símbolo #define chamam-se Constantes Simbólicas.
	Embora não seja obrigatório, habitualmente os programadores de C colocam as constantes simbólicas em maiúsculas.