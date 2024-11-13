O modelo OSI (Open Systems Interconection) nada mais é do que um modelo teórico *criado para auxiliar que toda a comunicação entre computadores e dispositivos ocorra na mesma língua*, a fim de que todos os envolvidos possam se entender e que as mensagens sejam entregues da forma correta.

Vídeo referência: [Modelo OSI e TCP/IP](https://www.youtube.com/watch?v=KOrWZnGbx7s)

---

<center><h1>Modelos</h1></center>
O modelo OSI é o mais atual e aceito, sendo o nosso escolhido para estudo. Entretanto, o modelo TCP/IP (de Andrews) e modelo TCP/IP (de Kurose) são análogos ao OSI, com apenas diferenciação na forma que categorizam cada etapa.

![[Pasted image 20241112110011.png]]

---
<center><h1>Camadas</h1></center>
Assim, o modelo OSI divide um sistema de comunicação em **7 camadas** (AASTREF), cada uma com sua função e seus **protocolos de comunicação** específicos:

![[Pasted image 20241111094721.png | center | 500]]
## 7: Camada de Aplicação

> Interação dos usuários com os dados.
> HTTP (sem criptografia SSL ou TLS), HTTPS (com criptografia), FTP, POP e DNS.

## 6: Camada de Apresentação

> Prepara o pacote para ser apresentado.
> Criptografia.
> Codificação de caracteres.
> Compactação

## 5: Camada de Sessão

> <small><small>Estabelece sessão de início (Start) e fim de conexão (End). Responsável por restabelecer a conexão perdida.</small> </small>
## 4: Camada de Transporte

> A informação, que é pacote, recebe um transmissor. Transmissor este UDP ou TCP.
> TCP: <small>Confiável, Garante a entrega, Handshake, orientado a conexão, unicast.</small>
> UDP: <small><small>Não confiável, Não garante a entrega, não orientado a conexão, Broadcast/Multicast/Unicast (vantagem).</small></small>

![[Pasted image 20241112104755.png]]

## 3: Camada de Rede

![[Pasted image 20241111095541.png | center | 70]]

>Informação é pacote, com endereço IP **de origem**, **de destino** e o **dado**.
><small>Endereço IP é colocado pelo administrador de rede na configuração, lógico. Propósito externo</small> 
>Roteador, dispositivo que gerencia pacotes e controla tráfego, usando IP.

## 2: Camada de Enlace

![[Pasted image 20241111095541.png | center | 70]]

>Informação é quadro, com endereço MAC **de origem**, **de destino** e o **dado**.
><small>Endereço MAC é da placa de rede do hardware, físico e de fábrica. Propósito Interno</small>.
>Switch, dispositivo que controla tráfego (usando MAC) e gerencia quadros.

## 1: Camada Física

![[Pasted image 20241111095240.png | center | 200]]

> Informação é  **bits brutos**. 
> Energia elétrica, cabos de rede, pinagem. 
> Pode haver Hub, opera em broadcast (envia para todos). Lento e inviável.

---
<center><h3>Termos</h3></center>

**Handshake**
	Composto por *SYN ->* (envio inicial), *<- SYNACK* (feedback), *ACK ->* (estabelecimento).

**Unicast**
	Conexão unitária entre dispositivos. 1/1.

**Broadcast**
	Conexão para todos.

**Multicast**
	Conexão para mais de um dispositivo, entretanto, não todos.

---
<center><h3>Observações</h3></center>

- O cabo de conexão Ethernet (o clássico azul), é denominado RJ-45;
- Roteador não conecta computadores e sim redes;
- TCP "**T**em **C**ompromisso com **P**acote"