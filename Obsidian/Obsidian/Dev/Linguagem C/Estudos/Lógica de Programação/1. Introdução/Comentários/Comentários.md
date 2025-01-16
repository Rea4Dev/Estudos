Um comentário em C é qualquer conjunto de caracteres compreendido entre os sinais de /* e * /.

Os comentários não se destinam a ser interpretados pelo compilador ou por qualquer componente do processo de desenvolvimento. São **simplesmente ignorados pelo compilador**, e o **programa executável não terá qualquer sinal deles**.

Uma vez que os comentários não têm qualquer interferência num programa, servem apenas para documentação de código. O seu objetivo é facilitar a vida do programador que tem que olhar para um determinado projeto em C, evitando que este tenha que perceber todo o código para saber o que determinado conjunto de instruções faz.

- Mesmo que por grande parte das vezes não recomendável, os comentários podem sempre ser colocados dentro de códigos. Apenas não serão tratados como comentários se você os colocar dentro de uma string.

- Os compiladores não permitem, em geral, a existência de comentários dentro de comentários. Porque seguindo a regra dos comentários em C, o comentário inicial terminava quando encontrasse o símbolo * /, que encerra o comentário. A extensão do comentário variaria então apenas entre a primeira ocorrência de /* e a primeira ocorrência de * /, detectando então um final de comentário sem o correspondente início.