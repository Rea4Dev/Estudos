Abaixo, temos um exemplo genérico e comum do que costuma ser um formulário nos sites.
![[Pasted image 20250318230311.png | center]]

Para ela, teríamos o seguinte código HTML.
![[Pasted image 20250318230401.png | center]]

---

## Form
```HTML
<form action="processa_formulario.php" method="get">
(...)
</form>
```
É o formulário em si. Usado para criar um formulário HTML para entrada do usuário.

``Atributos``
	*action*: <small>Endereço de para onde este formulário vai.</small>
	*method*: <small>Como esta informação será enviada. É "get" por padrão.
		<br>- Para get:   <br>a informação será enviada por URI, existem alguns problemas associados. Usado para dados não sigilosos.
		<br><br>- Para post:   <br>a informação será enviada para o payload, não aparecendo na URL. Método favorito caso seja formulário de login.</small>

---

## Label
```HTML
<form action="processa_formulario.php" method="get">

<label for="nome">Nome></label>

</form>
```
Basicamente vai definir um rótulo para o campo, onde inserimos uma descrição básica do que é cada campo.
Seu uso também é muito importante pela questão de acessibilidade, pois auxilia leitores de tela, por exemplo.
``Atributos``
	*for*: <small>Onde colocamos a informação para relacionar com os subsequentes elementos, como o id do imput.</small>