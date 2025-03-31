[[Índice de Python|Voltar]]

## 📌 *Importações*

- Importe módulos em **linhas separadas**.
- Agrupe na ordem: **padrão > terceiros > locais**.
- Evite `import *`.
- Prefira imports absolutos, mas use relativos em pacotes complexos.

```python
# Correto
import math
from datetime import datetime
import meu_modulo
from meu_pacote.modulo import Cliente
from .submodulo import configurar # Aceitável (relativo em pacotes)

# Errado
import sys, os  # múltiplas importações
from django import *  # wildcard
```