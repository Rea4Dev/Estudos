# Repositório

Para um Sistema Operacional, temos o diretório como a pasta em questão que estamos operando. 
De forma semelhante, para um Sistema de Controle de Versão, temos um repositório como o projeto que estamos manipulando.

![[Pasted image 20250422171809.png | center]]

## Ramo (branch)

### Ideia Fundamental
Em controle de versão, Branch é como um ramo em uma árvore que se separa do tronco principal. *Cada ramo representa uma linha distinta de desenvolvimento do seu projeto*.
Isso **permite que você trabalhe em diferentes funcionalidades** ou **experimente novas ideias** *sem afetar a versão principal do seu código*.

### Main / Master
Branch criada automaticamente sempre que criamos um repositório.

### Feature
Ao dividir o trabalho com outra pessoa, o mais indicado é que a outra pessoa crie um novo ramo a partir do último ponto da main.

É muito comum em equipes que se padronizem com o seguinte modelo de commits para features:

`featura/funcionalidade`
> feature/menu

## Commit

É uma operação que salva quais as alterações feitas em um ou mais arquivos do repositório e cria um ponto no histórico de versões, permitindo que você acompanhe as mudanças no projeto ao longo do tempo.

1. Sempre que um commit é feito, é gerado um ID único para este commit.
2. Embora não obrigatório, é recomendado preencher o campo de descrição com as informações relevantes.
3. Quando for a primeira vez a realizar um commit, será necessário inserir um *nome de usuário* e um *e-mail* para a devida identificação.

### Staging Area
É o espaço intermediário no Git onde você prepara/elenca quais alterações serão incluídas no commit.

![[Pasted image 20250422180243.png | center ]]