---
data_criacao: 01-09-2025
flashcards: Não feito
revisão: Não feita
---

---

# Mock

No contexto de **testes unitários em Python**, um **"mock"** é uma técnica usada para **simular o comportamento de objetos reais** de forma controlada. Isso permite testar partes do código isoladamente, sem depender de componentes externos como banco de dados, APIs, arquivos ou sensores.

Logo, um **mock** é um objeto "falso" que imita a interface de um objeto real, mas permite controlar suas respostas e verificar como ele foi usado. Em Python, isso é comumente feito com a biblioteca `unittest.mock`.

- **Isolar o código** que está sendo testado.
- **Evitar efeitos colaterais** (como chamadas reais a APIs ou escrita em disco).
- **Controlar o ambiente de teste**, simulando diferentes cenários.
- **Verificar interações**, como se uma função foi chamada, com quais argumentos, quantas vezes, etc.

- `Mock()`: cria um mock genérico.
- `patch()`: substitui objetos reais por mocks temporariamente.
- `MagicMock()`: como `Mock`, mas com suporte a operadores especiais (como `__len__`, `__getitem__`, etc).

## Exemplo

Pense que temos:

`tests/run.py`
```Python
def fetch_discount_rate():
	return 0.10

def get_discount(price: float):
	discount_rate = fetch_discount_rate()
	return price - (price * discount_rate)

```

E então, na hora de fazer os testes, para isolar o *get_discount* de *fetch_discount_rate*, construímos:
``tests/run_test.py`
```Python
import pytest
from tests import run

def test_get_discount(mocker):
	mocker.patch("tests.run.fetch_discount_rate", return_value=0.50)
	
	resp = run.get_discount(100)
	assert resp == 50
```