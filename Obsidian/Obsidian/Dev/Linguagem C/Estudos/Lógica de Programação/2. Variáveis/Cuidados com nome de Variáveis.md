O nome que se vai atribuir a variáveis em C implica observar um número reduzido de regras:

- O nome de uma variável pode ser constituído por letras do alfabeto (minúsculas ou maiúsculas), dígitos (0 … 9) e ainda pelo caractere underscore (_ ).
- **O primeiro caractere não pode ser um dígito**. Terá que ser uma letra ou o caractere underscore. No entanto, é desaconselhável a utilização deste último como primeira letra identificadora de uma variável.
- **Maiúsculas e minúsculas representam caracteres diferentes**, logo variáveis distintas.
- Uma variável **não pode ter por nome uma palavra reservada da própria Linguagem C**. Assim, não podemos ter uma variável denominada float, if ou for, uma vez que essas palavras são instruções ou tipos da própria linguagem.

**Não é aconselhável a utilização de caracteres acentuados** (ã, õ, á, é, etc.) no nome das variáveis, pois a grande maioria dos compiladores não os aceita como caracteres admissíveis.

O caractere underscore ( **_** ) **é habitualmente utilizado para fazer a separação entre palavras que representam uma única variável**. Ex: Num_Cliente, Id_Fatura, Vou_Continuar etc.

O número de caracteres que o nome de uma variável pode conter depende do compilador, mas é normal que sejam permitidos nomes de variáveis com até **32 caracteres** (ou mais).

## Cuidados a seguir
- O nome de uma variável deve ser descritivo daquilo que ela armazena.
- O nome de uma variável **não deve ser todo escrito em maiúsculas**, pois identificadores totalmente escritos em maiúsculas são tradicionalmente utilizados pelos programadores de C para referenciar **constantes**.
- Caso o nome de uma variável use mais do que uma palavra, utilize o caractere **underscore** **ou** a diferença entre **minúsculas e maiúsculas para as separar**, facilitando assim a leitura.
- Não utilize o caractere _underscore_ (_) para iniciar o nome de uma variável.