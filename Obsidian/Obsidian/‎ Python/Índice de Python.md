# <p style="color: #C82F4B; text-align:center;font-size:40px;">PEP 8 - Guia de Estilo para Códigos Python</p>
1. [[PEPs de Formatação do Código]]
	1. [[Espaçamento e Identações]]
	2. [[Nomes]]
		1. [[Booleanos]]
		2. [[PEP 8 - Funções e Variáveis]]
		3. [[Funções e métodos dunder]]
		4. [[Valores Privados]]
		5. [[Valores Protegidos]]
		6. [[PEP8 - Classes]]
		7. [[Métodos de Classe e Estáticos]]
		8. [[Constantes e Variáveis Globais]]
		9. [[Métodos de Instância]]
		10. [[Pacotes]]
		11. [[Exceções]]
	3. [[Quebras de Linha]]
	4. [[Comentários]]
	5. [[PEP 257 - Docstrings]]
	6. [[Comparações e Booleanos]]
	7. [[Importações]]
	8. [[Estruturas de Controle]]
	9. [[Funções e Classes]]
	10. [[Formatação de Strings]]
	11. [[Tratamento de Exceções]]
	12. [[Type Hints]]
	13. [[Exceções ao PEP8]]
	14. [[Ferramentas e Linters]]
	15. [[Considerações Finais]]

---
# <p style="color: #C82F4B; text-align:center;font-size:40px;">Práticas</p>
1. [[Mandamentos]]
2. [[Uso de logging]]
3. [[Manipulação de Arquivos com Open With]]
4. [[Definição de main e app]]
5. [[Testes Unitários]]
6. [[Tratamento de Exceções]]
	1. [[Custom Exceptions]]
7. [[Documentação com Docstrings]]
8. [[Padrões de Projeto]]
	1. [[Singleton Pattern]]
---
# <p style="color: #C82F4B; text-align:center;font-size:40px;">Sintaxe</p>
1. [[Sintaxe Fundamental]]
	1. [[Variáveis e Constantes]]
	2. [[Conversão de tipos]]
	3. [[Entrada e Saída]]
	4. [[Operadores]]
	5. [[Estruturas Condicionais]]
	6. [[Estruturas de Repetição]]
	7. [[Funções]]
	8. [[Módulos]]

2. [[Estruturas de Dados]]
	1. [[Lista]]
		1. [[Acessando e Modificando Elementos de Listas]]
		2. [[Métodos de Listas]]
		3. [[List Comprehensions]]
		4. [[Iterando sobre Listas]]
	2. [[Tupla]]
	    1. [[Named Tuple]]
	3. [[Dicionário]]
	4. [[Conjuntos (Sets)]]
	5. [[Queue e Stack]]

3. [[Orientação a Objeto]]
    1. [[Namespaces, Pacotes e Escopos]]
    2. [[Objetos]]
	     1. [[Classes]]
		 2.  [[Herança]]
		 3.  [[Métodos Mágicos]]
		 4.  [[Decoradores de Classe]]
		 5.  [[Métodos Estáticos vs de Classe]]
	3. [[Entendendo o contexto da Orientação a Objetos]] 
	4. [[Construtores e Destrutores]]
	5. [[Atributos de visibilidade e encapsulamento]]
	6. [[Herança]]
	7. [[Classes abstratas e a biblioteca ABC]]
	8. [[ Pseudo-Interfaces]]
	9. [[Lidando com erros e exceções]]

4. [[Sintaxe Complementar]]
	1. [[Operadores]]
	    1. [[Operadores Bitwise]]
	    2. [[Walrus Operator (:=)]]
	2. [[Estruturas Condicionais]]
	    1. [[Match-Case (Python 3.10+)]]
	3. [[Estruturas Condicionais]]
	    1. [[Match-Case (Python 3.10+)]]
	4. [[Funções]]
	    1. [[Funções Lambda]]
	    2. [[Decoradores]]
	    3. [[Geradores (Yield)]]
	    4. [[Parâmetros (*args e **kwargs)]]
	5. [[Manipulação de Strings]]
	    1. [[f-strings]]
	    2. [[Expressões Regulares (re)]]
	6. [[Context Managers (With)]]
	7. [[Tipagem Estática]]
	    1. [[Type Hinting]]
	    2. [[Typing Module]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Conceitos Avançados</p>
1. [[Programação Assíncrona]]
2. [[Metaprogramação]]
	1. [[Decoradores]]
	2. [[Descriptors]]
3. [[Closures]]
4. [[Pfrotocolos Estruturais]]
5. [[Desempacotamento de Valores]]
6. [[Serialização]]
	1. [[JSON]]
	2. [[Pickle]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Bibliotecas Padrão</p>
1. [[Datetime]]
2. [[Pathlib]]
3. [[CSV]]
4. [[Subprocess]]
5. [[Itertools]]
6. [[Functools]]
7. [[os/sys]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Ferramentas</p>
1. [[Ambientes Virtuais]]
	1. [[venv]]
	2. [[pipenv]]
	3. [[poetry]]
2. [[Debugging com PDB]]
3. [[Jupyter Notebooks]]
4. [[Type Checkers (mypy)]]
5. [[Formatters (Black/Flake8)]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Data Science</p>

1. [[NumPy]]
	1. [[Arrays Numéricos]]
	2. [[Operações Vetorizadas]]
2. [[Pandas Basics]]
3. [[Visualização de Dados]]
	1. [[Matplotlib]]
	2. [[Seaborn]]
	3. [[Plotly]]
4. [[Análise Exploratória]]
5. [[Limpeza de Dados]]
6. [[Estatística Básica]]
7. [[Scikit-learn]]
	1. [[Pré-processamento]]
	2. [[Modelos Básicos]]
8. [[APIs para Dados (requests)]]
9. [[Manipulação de DataFrames]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Ecossistema Python</p>
1. [[Web Frameworks]]
	1. [[FastAPI]]
	2. [[Flask]]
2. [[APIs REST]]
3. [[Empacotamento (setuptools)]]
4. [[Docker Integration]]

---

# <p style="color: #C82F4B; text-align:center;font-size:40px;">Performance</p>
1. [[Memoization (lru_cache)]]
2. [[Cython]]
3. [[Concorrência vs Paralelismo]]

```Python
a = "Renan Bobão"
a = a.replace("Bobão", "Fodão")
print(a)
```

Texto _negrito_
