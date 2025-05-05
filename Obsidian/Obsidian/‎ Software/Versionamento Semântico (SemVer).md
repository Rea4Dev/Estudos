
---
<center>Conceitos</center>

A página atual foi feita com base na documentação oficial da SemVer, entretanto, modificada para meu entendimento.
# Contextualizando SemVer

A Especificação da Semântica de Versionamento é autoria de [Tom Preston-Werner](http://tom.preston-werner.com/), criador do Gravatar e co-fundador do GitHub. Veja os tópicos abaixo:
## Dependency Hell

No mundo de gerenciamento de software existe algo terrível conhecido como inferno das dependências (“dependency hell”). Quanto mais o sistema cresce, e mais pacotes são adicionados a ele, maior será a possibilidade de, um dia, você encontrar-se neste poço de desespero.

Em sistemas com muitas dependências, lançar novos pacotes de versões pode se tornar rapidamente um pesadelo. Se as especificações das dependências são muito amarradas você corre o risco de um bloqueio de versão (A falta de capacidade de atualizar um pacote sem ter de liberar novas versões de cada pacote dependente). Se as dependências são vagamente especificadas, você irá inevitavelmente ser mordido pela ‘promiscuidade da versão’ (assumindo compatibilidade com futuras versões mais do que é razoável). O inferno das dependências é onde você está quando um bloqueio de versão e/ou promiscuidade de versão te impede de seguir em frente com seu projeto de maneira fácil e segura.

## Solução ao Dependency Hell

Como uma solução para este problema proponho um conjunto simples de regras e requisitos que ditam como os números das versões são atribuídos e incrementados.

Essas regras são baseadas em, mas não necessariamente limitadas às, bem difundidas práticas comumente em uso tanto em softwares fechados como open-source. Para que este sistema funcione, primeiro você precisa declarar um Client. Isto pode consistir de documentação ou ser determinada pelo próprio código. De qualquer maneira, é importante que este Client seja clara e precisa. Depois de identificada o Client, você comunica as mudanças com incrementos específicos para o seu número de versão. Considere o formato de versão X.Y.Z (Maior.Menor.Correção). Correção de falhas (bug fixes) que não afetam o Client, incrementa a versão de Correção, adições/alterações compatíveis com as versões anteriores do Client incrementa a versão Menor, e alterações incompatíveis com as versões anteriores do Client incrementa a versão Maior.

Eu chamo esse sistema de “Versionamento Semântico”. Sob este esquema, os números de versão e a forma como eles mudam transmitem o significado do código subjacente e o que foi modificado de uma versão para a próxima.

## Use-o!
Esta não é uma ideia nova ou revolucionária. De fato, você provavelmente já faz algo próximo a isso. O problema é que “próximo” não é bom o bastante. Sem a aderência a algum tipo de especificação formal, os números de versão são essencialmente inúteis para gerenciamento de dependências. Dando um nome e definições claras às ideias acima, fica fácil comunicar suas intenções aos usuários de seu software. Uma vez que estas intenções estão claras, especificações de dependências flexíveis (mas não tão flexíveis) finalmente podem ser feitas.

Como um desenvolvedor responsável você irá, é claro, querer certificar-se que qualquer atualização no pacote funcionará como anunciado. O mundo real é um lugar bagunçado; não há nada que possamos fazer quanto a isso senão sermos vigilantes. O que você pode fazer é deixar o Versionamento Semântico lhe fornecer uma maneira sensata de lançar e atualizar pacotes sem precisar atualizar para novas versões de pacotes dependentes, salvando-lhe tempo e aborrecimento.

Se tudo isto soa desejável, tudo que você precisar fazer para começar a usar Versionamento Semântico é declarar que você o esta usando e então, seguir as regras. 

## Referencie-o!
**Adicione um link** para este website no seu README para que outros saibam as regras e possam beneficiar-se delas.

# <span style="color:black;">.</span>
---
<center>Prática</center>

Os números abaixo referenciam a regras presentes na própria documentação oficial.
Entenda como API Pública = Client. Prefiro esta nomenclatura, devida familiaridade
# Client

1. Software usando Versionamento Semântico DEVE declarar um Client. Este Client poderá ser declarado no próprio código ou existir estritamente na documentação, desde que seja preciso e compreensivo.

# Versionamento
<center>Major.Minor.Patch</center>

1. Uma vez que um versionamento foi lançado, o conteúdo desta versão *NÃO DEVE ser modificado*. Qualquer modificação DEVE ser lançado como uma nova versão, seja em Major, Minor ou Patch.

## Major

2. No início do desenvolvimento, a versão Major DEVE ser zero (0.y.z). Qualquer coisa PODE mudar a qualquer momento. O Client NÃO DEVE ser considerada estável.

3. Versão 1.0.0 define o Client como público. A maneira como o número de versão é incrementado após este lançamento é dependente do Client e como ele muda.

4. Versão Maior X (X.y.z | X > 0) DEVE ser incrementada se forem introduzidas mudanças incompatíveis no Client. PODE incluir alterações a nível de versão Menor e de versão de Correção. Versão de Correção e Versão Menor DEVEM ser redefinidas para 0(zero) quando a versão Maior for incrementada.

## Minor

5. Versão Menor Y (x.Y.z | x > 0) DEVE ser incrementada se uma funcionalidade nova e compatível for introduzida no Client. DEVE ser incrementada se qualquer funcionalidade do Client for definida como descontinuada. PODE ser incrementada se uma nova funcionalidade ou melhoria substancial for introduzida dentro do código privado. PODE incluir mudanças a nível de correção. A versão de Correção DEVE ser redefinida para 0(zero) quando a versão Menor for incrementada.

## Patch

4. Versão de Correção Z (x.y.Z | x > 0) DEVE ser incrementado apenas se mantiver compatibilidade e introduzir correção de bugs. Uma correção de bug é definida como uma mudança interna que corrige um comportamento incorreto.

## Pré-Release

9. Uma versão de Pré-Lançamento (pre-release) PODE ser identificada adicionando um hífen (dash) e uma série de identificadores separados por ponto (dot) imediatamente após a versão de Patch.

10. Identificador DEVE incluir apenas caracteres alfanuméricos e hífen [0-9A-Za-z-]. 

11. Identificador NÃO DEVE ser vazio. 

12. Indicador numérico NÃO DEVE incluir zeros à esquerda. 

13. Versão de Pré-Lançamento tem precedência inferior à versão normal a que está associada.

14. Uma versão de Pré-Lançamento (pre-release) indica que a versão é instável e pode não satisfazer os requisitos de compatibilidade pretendidos, como indicado por sua versão normal associada. Exemplos: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.

15. Metadados de construção(Build) PODE ser identificada por adicionar um sinal de adição (+) e uma série de identificadores separados por ponto imediatamente após a Correção ou Pré-Lançamento. Identificador DEVE ser composto apenas por caracteres alfanuméricos e hífen [0-9A-Za-z-]. Identificador NÃO DEVE ser vazio. Metadados de construção PODEM ser ignorados quando se determina a versão de precedência. Assim, duas versões que diferem apenas nos metadados de construção, têm a mesma precedência. Exemplos: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85.
# <span style="color:black;">.</span>
---
<center>Complementos</center>

# Dúvidas Comuns
### Como devo lidar com revisões na fase 0.y.z de desenvolvimento inicial?

A coisa mais simples a se fazer é começar sua versão de desenvolvimento inicial em 0.1.0 e, então, incrementar a uma versão ‘menor’ em cada lançamento subsequente.

### Como eu sei quando lançar a versão 1.0.0?

Se seu software está sendo usado em produção, ele já deve ser provavelmente 1.0.0. Se você possui um Client estável a qual usuários passaram a depender, deve ser 1.0.0. Se você está se preocupando bastante com compatibilidade com versões anteriores, já deve ser 1.0.0.