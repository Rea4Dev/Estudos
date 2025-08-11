# Introdução

Na programação existem diversos paradigmas, o que muda de um para outro é a maneira de se pensar e organizar para solucionar o problema através de codificação.
Dentre estes paradigmas, um de grande destaque é a Orientação a Objeto.

## Como funciona a Orientação a Objeto?

Para entender a Orientação a Objeto, precisamos entender que uma <em>instância</em> de algo é como se fosse um elemento deste algo, podendo (dinamicamente) esta instância existir, ser modificada ou até mesmo excluída.

Toda a Orientação a Objeto circula na existencia de ==grupos com modelagem/padronização== para todas essas possíveis instâncias.

Então, formalmente, a orientação a objeto utiliza de **Classes** (que seriam esses "grupos") com seus *Atributos* e *Métodos* para criar uma *modelagem*/*padrão* para todas as *instâncias*.

- `Classe`
É a estrutura maior que modela/padroniza a existência de cada uma das instâncias em um objeto. 
---
- `Atributo de Classe`
Valor (mutável) em comum para todas as instâncias daquela classe.

Para acessar um atributo de classe é necessário utilizar 'cls' como objeto (obviamente tem que estar no parâmetro também) (PAREI AQUI)

---
- `Método`
Ação possível que aquela classe pode fazer (tal como uma função). 

Há o método especial *__ init__* que é automaticamente chamado sempre que uma nova instância é criada. 

---
- `self`
	- Comando que usamos dentro de classes para representar a instância do momento. É parâmetro de presença obrigatória em toda classe.
	
	- Um atributo com ==self.== pode ser acessada por qualquer outro método daquela mesma classe.
	
	- No método __ init __ , declarar um atributo  *self*.**atributo** recebendo de um parâmetro é uma forma de permitir, quando externo a classe durante a declaração, a armazenagem do argumento na instância.
---
- `Atributo de Instância`
Valor (mutável) individual daquela instância. Atributos de Instância estão sempre dentro de métodos.

```Python
class CachorroCaramelo:                  #------> Classe
	cor = 'Caramelo'                     #------> Atributo de Classe
	especie = 'Cachorro'
	
	def latir(self):                     #------> Método
		print("Au!")

cachorro_instancia1 = CachorroCaramelo() #------> Instância

cachorro_instancia1.latir()
```

Veremos um exemplo de Atributo de Instância mais para frente. Por hora, mantenha em mente o conceito.  