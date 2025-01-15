*Organiza* a *entrega* de dados na rede local usando quadros, endereços MAC, switches e mecanismos para evitar colisões e erros.

---

# <span style="color:white;"><small>1</small></span>. Estrutura dos Quadros Ethernet:

<center>
<table>
<thead>

<tr>

<th><center><strong>64 bits</strong></center></th>

<th><center><strong>48 bits</strong></center></th>

<th><center><strong>48 bits</strong></center></th>

<th><center><strong>16 bits</strong></center></th>

<th><center><strong>46 a 1500 bits</strong></center></th>

<th><center><strong>32 bits</strong></center></th>

</tr>

</thead>
  

<tr>

<td><center>Perâmbulo</center></td>

<td><center>Endereço destino</center></td>

<td><center>Endereço de origem</center></td>

<td><center>Tipo</center></td>

<td><center>Dados</center></td>

<td><center>Sequência de verificação de quadro</center></td>

</tr>

</tbody>
</center>

## Perâmbulo

Inserido pelo nível físico e é *utilizado para a sincronização* dos nós envolvidos na comunicação. Esse sincronismo é necessário para que os bits possam ser lidos pelo receptor no momento exato.

## Endereço de Destino

O endereço **MAC** do **destinatário**.

## Endereço de Origem

O endereço **MAC** do **remetente**.

## Tipo

Identifica o tipo de *protocolo que está encapsulado* no quadro (como **IPv4**, **IPv6**).

- Dados
A informação que está sendo transmitida.

- FCS (Frame Check Sequence)
Um código de verificação para detectar erros durante a transmissão.

---
# <span style="color:white;"><small>2</small></span>. Endereçamento MAC:
Cada dispositivo tem um endereço MAC único, que é um *identificador físico gravado na placa de rede*.
Ethernet usa endereços MAC para definir quem é o remetente e o destinatário dentro da rede local.

---

# <span style="color:white;"><small>3</small></span>. Protocolo de Controle de Acesso ao Meio (CSMA/CD):
Ethernet originalmente usava o CSMA/CD (Carrier Sense Multiple Access with Collision Detection) para controlar o acesso ao meio e evitar colisões em redes com hubs.
Hoje em dia, com redes full-duplex e switches, o CSMA/CD raramente é necessário, pois cada porta em um switch opera de forma independente, eliminando colisões.

---

# <span style="color:white;"><small>4</small></span>. Switches e Segmentação de Rede:
Switches Ethernet operam na camada de enlace, criando um caminho direto entre o remetente e o destinatário dentro de uma rede local. Eles permitem que diferentes dispositivos se comuniquem simultaneamente sem interferência, organizando a rede em segmentos.

---

# <span style="color:white;"><small>5</small></span>. Controle de Erro e Qualidade de Serviço (QoS):
A camada de enlace também inclui mecanismos de detecção de erro (como o FCS) para assegurar que os dados não estejam corrompidos ao chegar no destino.
Em redes mais avançadas, existem funções para QoS (priorização de tráfego), melhorando a qualidade para serviços sensíveis, como vídeo e voz.