A função dos formulários é *recolher dados* e *enviar para o servidor* para processamento.
Abaixo, temos um exemplo genérico e comum do que costuma ser um formulário nos sites.
![[Pasted image 20250318230311.png | center | 400]]

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

	<label for="nome">Nome</label>

</form>
```
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>

</form>

Basicamente vai definir um rótulo para o campo, onde inserimos uma descrição básica do que é cada campo.
Seu uso também é muito importante pela questão de acessibilidade, pois auxilia leitores de tela, por exemplo.
``Atributos``
	*for*: <small>Onde colocamos a informação para relacionar com os subsequentes elementos, como o id do imput.</small>

---
## Input
```HTML
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>

</form>
```
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>

</form>

Define um campo de entrada de dados dentro de um formulário, podendo ser de diversos tipos, como texto, senha, número, data, e-mail, etc.
``Atributos``
	*type:*<small>Define o tipo do que será inserido (text, password, checkbox, number, date, email)...</small>
	*id:* <small></small>
	*name:* <small></small>
	*required:* <small></small>
	*minlength:* <small></small>
	*maxlength:* <small></small>
	*value:* <small>Onde deixamos um valor padrão.</small>
	*readonly:* <small></small>
	*placeholder:* <small>Texto pré-preenchido que some quando o usuário clica.</small>

---
## Select + Option
```HTML
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
</form>
```

<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
</form>

Define um menu suspenso em um formulário, permitindo que o usuário escolha uma opção de uma lista pré-definida.
``Atributos Select``
	*Id:*<small></small>
	*Name:* <small></small>
``Atributos Select``
	*Value:*<small>O que é enviado para o sistema posteriormente. Pode diferir do texto mostrado ao usuário.</small>
	*Selected:* <small>Usado quando queremos que o formulário seja carregado com uma opção pré-selecionada</small>

---
## Text Area
```HTML
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
	
	<label for="msg">Mensagem:</label>
	<textarea id="msg" name="message" cols="20" rows="2">
	</textarea>
</form>
```
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
	
	<label for="msg">Mensagem:</label>
	<textarea id="msg" name="message" cols="20" rows="2">
	</textarea>
</form>

Area de texto multiline, permitindo que o usuário insira e edite grandes quantidades de texto, como comentários , mensagens ou descrições mais longas.
``Atributos Select``
	*Id:*<small></small>
	*Name:* <small></small>
	*Cols:* <small>Meramente por definição de tamanho (não limita), define quantas colunas haverá (cada caractere é uma coluna).</small>
	*Rows:* <small>Meramente por tamanho também (não limita), define quantas linhas.</small>

---
## Button
```HTML
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
	
	<label for="msg">Mensagem:</label>
	<textarea id="msg" name="message" cols="20" rows="2">
	</textarea>
	<button type="submit">Enviar</button>
</form>
```
<form action="processa_formulario.php" method="get">

	<label for="nome">Nome</label>
	<input type="text" id="nome" name="nome" required>
	
	<label for="email">E-mail</label>
	<input type="email" id="email" name="email" required>
	
	<label for="assunto">Assunto:</label>
	<select id="assunto" name="assunto">
		<option value="orçamento">Orçamento</option>
		<option value="outros">Outros</option>
	</select>
	
	<label for="msg">Mensagem:</label>
	<textarea id="msg" name="message" cols="20" rows="2">
	</textarea>
	<button type="submit">Enviar</button>
</form>

Representa um botão clicável que ao ser pressionado executa determinada ação, como enviar um formulário.
``Atributos Select``
	*Type:*<small>Button, reset, submit.</small>
