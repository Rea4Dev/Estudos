

Quais as características do AFDX? ;; <br>(**FSVT**)<br><br>**Full-Duplex** (*ambos sentidos*, *evitando colisões*, *velocidade e segurança*)<br>**Switching Determinístico** (*Switches*, *caminhos fixos VLs*, *Banda garantida*)<br> **Virtual Links (VLs)** (*MAC*)<br> **Trafego Determinístico** (*garante tempo de transmissão*, *envio e recebimento previsível e constante*).
<!--SR:!2024-11-20,1,230-->

O que são End Systems no pacote AFDX? ;; <br> Componente *conectado à rede capaz de suportar todas as operações relacionadas com o protocolo*. <br><br> Normalmente um end system é uma parte de um aviônico ou um *subsistema de uma aeronave que necessita enviar ou receber dados*, para desencadear um procedimento que seja elétrico, eletrônico, mecânico ou etc. <br><br> Para interligar estes sistemas estão *localizados entre os end systems um ou mais switches AFDX*, dependendo da hierarquia da rede.<br><br> ![[Pasted image 20241113114924.png | center | 500]]
<!--SR:!2024-11-20,1,230-->

O que é o **Perâmbulo** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; Uma sequência de bits utilizada para *sincronizar o transmissor e o receptor*. Este campo <u style="text-decoration-color:rgba(200, 47, 75, 0.6);">ajuda o receptor a identificar o início de um frame e a se preparar para receber dados.</u> - (7 bytes)
<!--SR:!2024-11-20,1,230-->

O que é o **Start Frame Delimiter** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; Indica o *início do frame*. Este byte específico <u style="text-decoration-color:rgba(200, 47, 75, 0.6);">sinaliza que o restante do frame está prestes a começar</u>. - (1 byte)
<!--SR:!2024-11-20,1,230-->

O que é o **Destination Adress** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Contém o endereço <u style="text-decoration-color:rgba(200, 47, 75);">MAC de destino</u>, representando o identificador do Virtual Link (<u style="text-decoration-color:rgba(200, 47, 75);">VL</u>). Cada VL tem um endereço MAC único que permite o roteamento do pacote para o destino correto na rede AFDX.</small> - (6 bytes)
<!--SR:!2024-11-20,1,230-->

O que é o **Source Adress** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Contém o endereço <u style="text-decoration-color:rgba(200, 47, 75);">MAC da origem</u>, indicando de onde o frame está vindo. Isso permite que o receptor saiba de qual dispositivo o pacote foi enviado.</small>
<!--SR:!2024-11-20,1,230-->

O que é o **Type** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Especifica o <u style="text-decoration-color:rgba(200, 47, 75);">tipo de protocolo usado no nível de rede</u>. No caso do AFDX, o tipo é 0x0800, que representa o protocolo IP versão 4 (IPv4).</small>

O que é o **IP Header** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Esta seção contém o cabeçalho do protocolo IP, incluindo informações como o <u style="text-decoration-color:rgba(200, 47, 75);">endereço IP de origem e destino</u>, a <u style="text-decoration-color:rgba(200, 47, 75);">versão</u> do IP, o <u style="text-decoration-color:rgba(200, 47, 75);">tamanho</u> do pacote, a <u style="text-decoration-color:rgba(200, 47, 75);">identificação</u> do pacote e <u style="text-decoration-color:rgba(200, 47, 75);">outras informações de controle</u>.</small>
<!--SR:!2024-11-20,1,210-->

O que é o **UDP Header** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Cabeçalho do protocolo UDP (User Datagram Protocol), que inclui informações sobre as <u style="text-decoration-color:rgba(200, 47, 75);">portas de origem e destino</u>, o <u style="text-decoration-color:rgba(200, 47, 75);">comprimento</u> do datagrama UDP e um campo de checksum para verificar a <u style="text-decoration-color:rgba(200, 47, 75);">integridade</u> do segmento UDP.</small>
<!--SR:!2024-11-20,1,230-->

O que é o **AFDX Payload** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Esta é a <u style="text-decoration-color:rgba(200, 47, 75);">carga útil do frame</u>, que contém os dados reais a serem transmitidos. No contexto de redes AFDX, esse é o dado de aplicação encapsulado pelo protocolo IP/UDP.</small>
<!--SR:!2024-11-20,1,230-->

O que é o **Padding** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Campo opcional para preenchimento (padding), garantindo que o frame tenha o <u style="text-decoration-color:rgba(200, 47, 75);">comprimento mínimo necessário para transmissão</u> (normalmente 46 bytes no Ethernet). Esse campo ajuda a alinhar os dados corretamente no frame.</small>
<!--SR:!2024-11-20,1,230-->

O que é o **Sequence Number** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; <small>Este campo contém o número de sequência do pacote, que é usado para <u style="text-decoration-color:rgba(200, 47, 75);">rastrear a ordem dos pacotes e detectar perdas de pacotes na transmissão</u>. Ele é importante para manter a integridade dos dados na rede AFDX.</small>
<!--SR:!2024-11-20,1,230-->

O que é o **Frame Check Sequence** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; Um campo de verificação de integridade que contém um valor de checksum calculado sobre o conteúdo do frame. Ele <u style="text-decoration-color:rgba(200, 47, 75);">permite ao receptor verificar se o frame foi recebido corretamente, sem erros de transmissão</u>.
<!--SR:!2024-11-20,1,230-->

O que é o **Interframe Gap** pacote AFDX?<br>![[Pasted image 20241113131247.png]]<br> ;; Intervalo de <u style="text-decoration-color:rgba(200, 47, 75);">tempo obrigatório entre frames consecutivos para permitir que a rede processe o frame anterior antes de receber o próximo</u>. Esse campo não é parte do frame de dados em si, mas sim um espaço de tempo necessário para o funcionamento adequado da rede.
<!--SR:!2024-11-20,1,230-->