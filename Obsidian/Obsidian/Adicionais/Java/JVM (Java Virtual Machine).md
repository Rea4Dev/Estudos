# Portabilidade de Softwares

Um dos desafios comuns no desenvolvimento de software é a *portabilidade*. Por exemplo, um executável gerado a partir de um programa escrito em Python no *Windows* geralmente *não funcionará* diretamente em um sistema *Linux*, e o contrário também é verdadeiro.

Isso ocorre devido às *diferenças entre os sistemas operacionais*, como:

- Formatos de arquivos executáveis distintos (`.exe` no Windows, binários ELF no Linux);
- Diferenças nas bibliotecas nativas e dependências;
- Variações na forma como o sistema operacional gerencia permissões, caminhos e chamadas de sistema.

Essas incompatibilidades tornam difícil executar o mesmo software em diferentes plataformas sem adaptações específicas.

# JVM (Java Virtual Machine)

É justamente nesse contexto que a **JVM** se destaca. A **Java Virtual Machine** resolve o problema de portabilidade ao **intermediar a execução** do código Java.

Em vez de gerar um executável dependente do sistema operacional, o compilador Java gera um **bytecode**, armazenado em arquivos `.class`. Esse bytecode é **independente de plataforma** e pode ser interpretado pela JVM instalada em qualquer sistema operacional,  seja Windows, Linux, macOS, etc.

Ou seja:

- O código-fonte Java é compilado em **bytecode**.
- Esse bytecode é **executado pela JVM**, que atua como uma camada de abstração entre o software e o sistema operacional.

## JDK e JRE

Utilizamos a JDK (*Java Development Kit*) para desenvolver em Java, ele nos traz compilador, ferramentas de monitoramento e etc.

Temos a Ambiente de Execução do Java (JRE - *Java Runtime Enviroment*)

Já a JVM (Java Virtual Machine) traduz o bytecode para o computador, o que o torna *portável*.

![[Pasted image 20250808170543.png | center]]

# WORA (Write Once, Run Anywhere)

Graças à JVM, o Java se tornou uma linguagem conhecida por sua **portabilidade**. Esse conceito é resumido pela expressão **WORA**, _Write Once, Run Anywhere_, que significa que o desenvolvedor pode escrever o código uma única vez e executá-lo em qualquer ambiente que tenha uma JVM compatível.

Essa característica foi um dos principais fatores que impulsionaram a popularidade do Java, especialmente em ambientes corporativos e sistemas embarcados.