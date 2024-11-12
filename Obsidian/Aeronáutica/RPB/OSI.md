O modelo OSI (Open Systems Interconection) nada mais é do que um modelo teórico *criado para auxiliar que toda a comunicação entre computadores e dispositivos ocorra na mesma língua*, a fim de que todos os envolvidos possam se entender e que as mensagens sejam entregues da forma correta.

---
<center><h1>Camadas</h1></center>
Assim, o modelo OSI divide um sistema de comunicação em **7 camadas** (AASTREF), cada uma com sua função e seus **protocolos de comunicação** específicos:
![[Pasted image 20241108081513.png]]
![[Pasted image 20241111094721.png | center]]
## 7: Camada de Aplicação
É nessa camada que ocorre a interação entre o usuário e os dados, apresentados por meio de interfaces e aplicações como navegadores de internet e servidores de email. Alguns dos protocolos de comunicação mais populares utilizados na camada de aplicação são [**HTTP**](https://www.azion.com/pt-br/blog/o-que-e-http-e-como-ele-funciona/), **FTP**, **POP** e [**DNS**](https://www.azion.com/pt-br/blog/o-que-e-dns-e-como-ele-funciona/).

## 6: Camada de Apresentação
Camada que funciona como um tradutor de dados para a rede, responsável por criptografar, compactar e apresentar os dados.

## 5: Camada de Sessão
Camada onde se inicia, gerencia e encerra sessões de transferência de dados entre dispositivos. Ela também pode realizar verificações para garantir, caso uma sessão seja encerrada bruscamente, que uma nova sessão de transferência seja retomada do início para que não haja corrupção dos dados e informações.

## 4: Camada de Transporte

> A informação, que é pacote, recebe um transmissor. Transmissor este UDP ou TCP.
> TCP: <small>Confiável, Garante a entrega, Handshake, orientado a conexão, unicast.</small>

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
- 