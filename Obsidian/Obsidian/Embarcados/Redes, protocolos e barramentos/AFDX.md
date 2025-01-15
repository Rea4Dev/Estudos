Baseada no padrão **ARINC 664**, ela é usada para *comunicação de dados em tempo real* entre *sistemas críticos* em aviões modernos.

> [!TIP] Relação com Ethernet
> AFDX é uma *versão especializada de Ethernet* desenvolvida para aviação, com garantias de *performance*, como *largura de banda* e *latência*, o que o torna confiável e seguro para *aplicações sensíveis* (como controle de voo).

---

## Características e Protocolos Envolvidos

**Full-Duplex**
	A comunicação ocorre em *ambos os sentidos* ao mesmo tempo, *evitando colisões* de dados e aumentando a *velocidade e segurança* da transmissão.

**Switching Determinístico**
	O AFDX usa *switches* para direcionar pacotes a destinos específicos. Os switches têm “*caminhos fixos*” (*Virtual Links*) e uma largura de *banda garantida* para que os dados trafeguem sem congestionamentos.

**Virtual Links (VLs)**
	O AFDX organiza as comunicações através de VLs, que são “*rotas*” *fixas* para pacotes de dados. *Cada VL é unidirecional* e tem largura de banda alocada, garantindo tempo e ordem de chegada.<br>
	Cada VL tem um endereço MAC único que permite o roteamento do pacote para o destino correto na rede AFDX.

**Trafego Determinístico**
	Com cada pacote tendo uma largura de banda fixa e caminho pré-determinado, o AFDX garante que o *tempo de transmissão* entre o envio e o recebimento seja *previsível e constante*.

---
## End Systems

Um end system é *um componente conectado à rede capaz de suportar todas as operações relacionadas com o protocolo*.

Normalmente um end system é uma parte de um aviônico ou um *subsistema de uma aeronave que necessita enviar ou receber dados, para desencadear um procedimento que seja elétrico, eletrônico, mecânico ou etc*. 

Para interligar estes sistemas estão localizados entre os end systems um ou mais switches AFDX, dependendo da hierarquia da rede.

![[Pasted image 20241113114924.png | center | 500]]

---
## Especificação Pacotes

<small>Esse frame AFDX segue o padrão Ethernet e <strong>encapsula os dados IP e UDP</strong>, que por sua vez <strong>contêm a carga útil da aplicação AFDX</strong>. <br>O uso de endereços MAC, IP e UDP fornece a infraestrutura necessária para a comunicação em redes Ethernet, enquanto os campos específicos do AFDX (como o Sequence Number) garantem a confiabilidade e a integridade da transmissão, que são cruciais em sistemas de aviação onde a perda ou a desordem de pacotes pode ter consequências graves.</small>

![[Pasted image 20241113131247.png]]

**Perâmbulo**
	Uma sequência de bits utilizada para *sincronizar o transmissor e o receptor*. Este campo <u style="text-decoration-color:rgba(200, 47, 75, 0.6);">ajuda o receptor a identificar o início de um frame e a se preparar para receber dados.</u>

**Start Frame Delimiter**
	Indica o *início do frame*. Este byte específico <u style="text-decoration-color:rgba(200, 47, 75, 0.6);">sinaliza que o restante do frame está prestes a começar</u>.

> [!note] MAC
> **Destination adress**
> <span style="color:red">|</span>   <small>Contém o endereço <u style="text-decoration-color:rgba(200, 47, 75);">MAC de destino</u>, representando o identificador do Virtual Link (<u style="text-decoration-color:rgba(200, 47, 75);">VL</u>). Cada VL tem um endereço MAC único que permite o roteamento do pacote para o destino correto na rede AFDX.</small>
> 
> **Source adress**
> <span style="color:red">|</span> <small>Contém o endereço <u style="text-decoration-color:rgba(200, 47, 75);">MAC da origem</u>, indicando de onde o frame está vindo. Isso permite que o receptor saiba de qual dispositivo o pacote foi enviado.</small>
> 
> 
> **Type**
> <span style="color:red">|</span> <small>Especifica o <u style="text-decoration-color:rgba(200, 47, 75);">tipo de protocolo usado no nível de rede</u>. No caso do AFDX, o tipo é 0x0800, que representa o protocolo IP versão 4 (IPv4).</small>


> [!note] IP
> **Ip Header**
> <span style="color:red">|</span> <small>Esta seção contém o cabeçalho do protocolo IP, incluindo informações como o <u style="text-decoration-color:rgba(200, 47, 75);">endereço IP de origem e destino</u>, a <u style="text-decoration-color:rgba(200, 47, 75);">versão</u> do IP, o <u style="text-decoration-color:rgba(200, 47, 75);">tamanho</u> do pacote, a <u style="text-decoration-color:rgba(200, 47, 75);">identificação</u> do pacote e <u style="text-decoration-color:rgba(200, 47, 75);">outras informações de controle</u>.</small>
> > [!tip] UDP
> **UDP header**
> <span style="color:red">|</span> <small>Cabeçalho do protocolo UDP (User Datagram Protocol), que inclui informações sobre as <u style="text-decoration-color:rgba(200, 47, 75);">portas de origem e destino</u>, o <u style="text-decoration-color:rgba(200, 47, 75);">comprimento</u> do datagrama UDP e um campo de checksum para verificar a <u style="text-decoration-color:rgba(200, 47, 75);">integridade</u> do segmento UDP.</small>
> > > [!tip] AFDX Message
> > >** AFDX Payload**
> > > <span style="color:red">|</span> <small>Esta é a <u style="text-decoration-color:rgba(200, 47, 75);">carga útil do frame</u>, que contém os dados reais a serem transmitidos. No contexto de redes AFDX, esse é o dado de aplicação encapsulado pelo protocolo IP/UDP.</small>
> > > <br>
> > > **Padding**
> > > <span style="color:red">|</span> <small>Campo opcional para preenchimento (padding), garantindo que o frame tenha o <u style="text-decoration-color:rgba(200, 47, 75);">comprimento mínimo necessário para transmissão</u> (normalmente 46 bytes no Ethernet). Esse campo ajuda a alinhar os dados corretamente no frame.</small>
> > > <br>
> > > **Sequence Number**
> > > <span style="color:red">|</span> <small>Este campo contém o número de sequência do pacote, que é usado para <u style="text-decoration-color:rgba(200, 47, 75);">rastrear a ordem dos pacotes e detectar perdas de pacotes na transmissão</u>. Ele é importante para manter a integridade dos dados na rede AFDX.</small>

**Frame Check Sequence**
	Um campo de verificação de integridade que contém um valor de checksum calculado sobre o conteúdo do frame. Ele <u style="text-decoration-color:rgba(200, 47, 75);">permite ao receptor verificar se o frame foi recebido corretamente, sem erros de transmissão</u>.

**Interframe Gap**
	Intervalo de <u style="text-decoration-color:rgba(200, 47, 75);">tempo obrigatório entre frames consecutivos para permitir que a rede processe o frame anterior antes de receber o próximo</u>. Esse campo não é parte do frame de dados em si, mas sim um espaço de tempo necessário para o funcionamento adequado da rede.

---
## Implementação e Configuração de Switches

A configuração dos switches AFDX é *fundamental para garantir a alocação correta de cada VL*. Esses switches são configurados para manter as taxas de transmissão e latência mínimas.

**Qualidade de Serviço (QoS)**
	Cada VL tem uma *prioridade e largura de banda específica configurada* para garantir que os dados de *maior prioridade cheguem primeiro*.

---

## Monitoramento e Manipulação de Dados

No caso, para um leitor e manipulador de dados AFDX, será necessário:

*Ferramentas para Captura de Pacotes* 
	Wireshark, por exemplo, pode capturar pacotes AFDX em uma rede e exibir dados como VL, timestamp, e sequência.

*Bibliotecas para Manipulação de Pacotes*
	Algumas bibliotecas permitem manipular pacotes, mas pode ser necessário implementar cabeçalhos específicos do AFDX.

*Análise de VL e Timestamps*
	Muitas ferramentas conseguem monitorar e validar os tempos de chegada de pacotes e analisar o funcionamento de cada VL, garantindo que a comunicação está de acordo com os requisitos de tempo real.

---

## Pontos Críticos e Desafios

- *Latência e Sincronização*: O AFDX depende de sincronização e latências bem definidas. É importante considerar clocks sincronizados na captura dos pacotes para garantir a precisão.

- *Gerenciamento de Erros e Redundância*: O AFDX oferece opções de redundância para evitar falhas. Cada pacote pode ter uma cópia redundante enviada simultaneamente para garantir que pelo menos um chegue.

---

- [ ] Evoluir C
- [ ] Aprender a usar Wireshark
- [ ] Manipulações Básicas
