O ARINC (**A**eronautical **R**adio **Inc**) 429 foi publicado em **1977** para definir *como os sistemas aviônicos e componentes devem se comunicar*.

A *especificação técnica* ARINC-429, originalmente referida como *Sistema de Transferência Digital de Informação* (**DTIS**), foi publicada em **1977** para *definir como sistemas e componentes aviônicos devem se comunicar*. 

O **MARK 33 - Sistema de Transferência de Informação Digital**, como é conhecido hoje, ainda é o modelo mais comumente usado. Esta especificação é usada para estabelecer **comunicação de barramento 429** para estrutura de palavras, características elétricas e outros protocolos.
## Especificação Geral
O que é único a respeito da transferência de dados do ARINC-429 é seu simples **fluxo unidirecional de comunicação de dados de barramento**.
![[Pasted image 20241030083021.png]]
- Hardware consistindo em um único transmissor suportando de 1 a 20 receptores (conhecidos como "sinks") em um único par de fios.
- A transmissão de dados é unidirecional.
- Um transmissor de dados consegue apenas se comunicar com um número definido de receptores.
## Especificação Pacotes
- A maior parte das mensagens são constituídas de um único pacote.
- O pacote de dados é constituído de 32 bits, sendo 24 bits contendo o core da informação e 8 bits agindo como um label descrevendo o dado transmitido. 
- Os pacotes são enviados em baixa velocidade (12.5 Kbit/s) ou em alta velocidade (100 Kbit/s).

![[Pasted image 20241031102028.png | center | 522]]

- <big>SDI</big> : Source Destination Identifiers (2 bits)
Usado por um transmissor para identificar qual receptor deverá processar a mensagem. Se não utilizado, os bits podem ser usados para dados.

- <big>Dados</big>
A informação que está sendo comunicada.

- <big>SSM</big> : Sign Status Matrix (2 bits)
Par de bits para indicar qual o modo de funcionamento da LRU (Normal Operation, Error A, Error B, Test Mode...), propósito de validação.

- <big>P</big> : Parity (1 bit)
Bit do encerramento do pacote. Diz respeito ao pacote em si.

- Label
Categoriza o dado, tal qual uma classe numa programação orientada a objeto.

![[Pasted image 20241101111838.png | center]]

