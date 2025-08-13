---
data_criacao: 12-08-2025
flashcards: Não feito
revisão: Não feita
---
# Formatação

Utilizamos **PascalCase** em classes. É semelhante ao *camelCase*, mas ao invés da primeira palavra começar com minúscula, agora começa com maiúscula.
```Java
PascalCase
camelCase
```
# Classes

Java é uma linguagem já no paradigma de orientação a objeto. 

Desta forma, Classes são **blueprints** (plantas/receita) para **criar instâncias**.
As classes definem:
- O que a instância precisa ter
- Como ela vai se comportar

## JVM

Neste contexto, encare a JVM como o *arquiteto* que irá olhar e interpretar as nossas classes para *construir os nossas instâncias* que serão utilizadas pelo nosso programa Java.

## Instâncias

No exemplo abaixo, ambos gatos são objetos (*instâncias*) da Classe "Gato".
![[Pasted image 20250813091706.png | center | 450]]

```Java
public class Despertador{    /* Classe */
	int horas;               /* Instância de Classe */
	int minutos;
	int soneca;

	void ativarSoneca(){    /* Método */
		System.out.println("Só mais " + soneca + " minutinhos")
	}

	String agendarAlarme() {
		return "Alarme configurado para" + hora + ":" + minutos;
	}
}
```