## Introdução
- Módulo `logging` da biblioteca padrão Python para registro de eventos em aplicações
- Alternativa superior a `print()` para:
  - Controle de saída em diferentes níveis de severidade
  - Redirecionamento para múltiplos destinos (arquivo, console, rede)
  - Manutenção de histórico de execução

## Componentes Principais
1. **Loggers**: Objetos principais de interface (criados com `getLogger()`)
2. **Handlers**: Destinos dos logs (FileHandler, StreamHandler, etc)
3. **Formatters**: Estruturação das mensagens (formato, data/hora)
4. **Filters**: Controle granular de quais logs são registrados
5. **Níveis**: DEBUG < INFO < WARNING < ERROR < CRITICAL

## Configuração Básica
```python
import logging

# Configuração inicial
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Uso
logger = logging.getLogger(__name__)
logger.debug('Mensagem para depuração')
logger.info('Informação geral')
logger.warning('Aviso importante')
logger.error('Erro na operação')
logger.critical('Falha crítica')
```

## Configurações Avançadas
- Handlers múltiplos:
  ```python
  file_handler = logging.FileHandler('app.log')
  console_handler = logging.StreamHandler()
  
  formatter = logging.Formatter('%(levelname)s - %(message)s')
  file_handler.setFormatter(formatter)
  
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)
  ```

- Hierarquia de loggers (usando `__name__`)
- Filtros personalizados
- Configuração via arquivo/dicionário

## Boas Práticas
- Utilizar níveis adequados para cada tipo de mensagem
- Evitar logger root (`logging.info()`), usar instâncias específicas
- Incluir informações contextuais (usuário, sessão, transação)
- Usar exceções com `logger.exception()` para tracebacks
- Configurar logging no início da aplicação

## Troubleshooting Comum
- Logs não aparecendo: verificar nível do logger e handler
- Mensagens duplicadas: herança na hierarquia de loggers
- Formatação incorreta: verificar formatters nos handlers
- Problemas de desempenho: evitar logging em nível DEBUG em produção

## Conclusão
O módulo logging oferece sistema robusto para diagnóstico e monitoramento, essencial para aplicações profissionais. Sua flexibilidade permite adaptação desde scripts simples até sistemas complexos.