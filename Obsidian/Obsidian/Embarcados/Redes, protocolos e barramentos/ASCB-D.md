Projetado para aplicações críticas, garantindo alta confiabilidade e baixo atraso na troca de informações. 

---
## Tipo de Dados
Os dados transmitidos no ASCB-D são geralmente estruturados em palavras digitais. Essas palavras possuem:

- *Bits de Controle*: <small>Para identificar o tipo de mensagem ou prioridade.</small>
- *Dados do Sistema*:<small>Informações úteis como parâmetros de voo, comandos, etc.</small>
- *Bits de paridade*: <small>Para garantir a integridade do dado transmitido.</small>

---

## Arquitetura ASCB-D
Embora a documentação oficial possa variar dependendo do fabricante e da aplicação, em geral, o pacote (ou "word) transmitido pelo ASCB-D é composto por campos predefinidos.

Um pacote de dados ASCB-D costuma ter *32 bits* (1 palavra), organizados da seguinte forma:

<table> 

<thead> 
<tr> 
<th><center>Bits</center></th> 
<th><center>Campo</center></th> 
<th><center>Descrição</center></th> 
</tr> 
</thead>


<tr> 
<td><center>1</center></td> 
<td><center><strong>Sinal de Paridade</strong> (Paridade Ímpar)</center></td>
<td><center>Usado para checar a integridade do pacote.<br><br><small>- Garante a detecção de erros simples.</small><br><small>- Paridade ímpar significa que o número total de bits "1" deve ser ímpar.</small><br></center></td>
</tr>

<tr> 
<td><center>2-4</center></td> 
<td><center><strong>Tipo de palavra</strong> (Word Type)</center></td>
<td><center>Indica o tipo de dado (comando, status ou dados).<br><br><small>Indentifica se a palavra é:</small><br><small>- Um comando (para controlar dispositivos)</small><br><small>- Um status (para reportar o estado de um dispositivo.</small><br><small>- Dados úteis (informações operacionais).</small><br></center></td>
</tr>

<tr> 
<td><center>5-8</center></td> 
<td><center><strong>Prioridade</strong></center></td>
<td><center>Determina a prioridade no barramento, garantindo que mensagens críticas sejam transmitidas primeiro.</center></td>
</tr>

<tr> 
<td><center>9-31</center></td> 
<td><center><strong>Dados Úteis</strong></center></td>
<td><center>Informação específica da aplicação (ex: parâmetros de voo, comandos, etc.</center></td>
</tr>

</tbody> 


---
## Topologia
Normalmente funciona em uma arquitetura de barramento, onde múltiplos dispositivos podem se comunicar em uma linha compartilhada.

---
## Taxa de transmissão
Tem taxas de transmissão relativamente altas para suportar sistemas modernos de aeronaves.

---
## Determinismo
Como é usado em sistemas críticos, ele prioriza a previsibilidade e controle de tempos de resposta.

---
## Imunidade a Ruídos
Inclui mecanismos para garantir integridade de dados em ambientes eletricamente ruidosos, típicos de aeronaves.

---
## Aplicações

- Troca de dados entre sensores, atuadores e sistemas de controle (ex: sistemas de navegação, piloto automático);
- Comunicação entre módulos de sistemas eletrônicos centralizados ou distribuídos;
- Interface de dados em sistemas aviônicos integrados.

---
## Por que usar o ASCB-D?

*Alta confiabilidade*
	Crucial para evitar falhas em sistemas críticos.

*Baixo atraso*
	Fundamental para aplicações que demandam resposta imediata, como controle de voo.

*Interoperabilidade*
	Permite que sistemas de diferentes fabricantes se conectem usando um padrão comum.
	