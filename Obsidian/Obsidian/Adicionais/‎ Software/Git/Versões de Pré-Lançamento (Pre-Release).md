Uma **versão de pré-lançamento** é um rótulo opcional que indica que aquela publicação **ainda não é estável** ou está em fase experimental. Seguem as regras e práticas recomendadas: --------> (PAREI AQUI) <----------------- INCLUA PRE-ALFA

# Sintaxe

1. Após o componente **Patch** (`Z`) acrescente um hífen (`-`) e uma lista de identificadores separados por pontos:

X.Y.Z-identificador.identificador…

2. Cada **identificador** deve usar apenas `[0-9A-Za-z-]`, não pode estar vazio e, se for puramente numérico, não ter zeros à esquerda.

## Identificadores Comuns

| Prefixo | Significado                                                                      | Exemplos                       |
| ------- | -------------------------------------------------------------------------------- | ------------------------------ |
| `alpha` | Versão inicial, pode faltar funcionalidade ou conter bugs graves                 | `1.2.0-alpha`, `1.2.0-alpha.1` |
| `beta`  | Mais madura que alpha, mas ainda sujeita a alterações                            | `1.2.0-beta`, `1.2.0-beta.2`   |
| `rc`    | Release Candidate: quase a versão final, apenas correções finais                 | `1.2.0-rc.1`                   |
| outros… | Qualquer outro identificador de sua escolha (e.g., `next`, `canary`, `snapshot`) |                                |

## Precedência e Ordenação

- **Precedence**: toda versão de pré-lançamento tem precedência **inferior** à versão normal correspondente.  
Exemplo:

1.2.0-alpha < 1.2.0 < 1.2.1

- Entre si, pré-releases são ordenadas **lexicograficamente** e depois **numericamente**:

1.2.0-alpha < 1.2.0-alpha.1 < 1.2.0-beta < 1.2.0-rc.1

## Metadados de Build

- Opcionalmente, você pode adicionar metadados após um sinal de mais (`+`):

X.Y.Z(-pre)+metadados

- Metadados **não afetam** precedência:

1.2.0-alpha+20250428 == 1.2.0-alpha

## Exemplos de Uso em Workflow

1. **Desenvolvimento contínuo**  
 - Comece com `0.1.0-alpha` → `0.1.0-alpha.1` → … → `0.1.0-beta` → `0.1.0-rc.1` → `0.1.0`.
2. **Publicação em npm/yarn**  
 - Utilize `npm dist-tag` para apontar `latest`, `beta`, `alpha` etc.  
   ```bash
   npm publish --tag beta   # publica como “beta”
   npm install meu-pacote@beta
   ```
3. **Controle de dependência**  
 - Permitir somente betas:  
   ```yaml
   "dependencies": {
     "meu-pacote": "^1.2.0-beta"
   }
   ```
 - Combinar com ranges:  
   ```
   >=1.2.0-alpha <1.2.0
   ```

## Boas Práticas

- **Seja consistente**: defina um fluxo (alpha→beta→rc) e siga-o em todas as bibliotecas.
- **Documente** na sua seção “Release” o que cada identificador significa.
- **Limpe tags antigas** nos repositórios/remotos para evitar confusão.
- **Automatize** a geração de pré-lançamentos via CI/CD (ex.: GitHub Actions).