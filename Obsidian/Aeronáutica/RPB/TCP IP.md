
---
<center><h1>TCP</h1></center>
## O que é TCP
O protocolo de controle de transmissão (TCP) é um padrão de comunicação que permite que programas aplicativos e dispositivos de computação *intercambiem mensagens em uma rede*. Ele foi projetado para *enviar pacotes pela internet e garantir a entrega bem-sucedida* de dados e mensagens nas redes.

O TCP é *um dos padrões básicos que definem as regras da internet* e está incluído nos padrões definidos pela Internet Engineering Task Force (IETF). É um dos protocolos mais comumente usados nas comunicações de rede digital e *garante a entrega de dados de ponta a ponta*.

O TCP organiza os dados para que possam ser *transmitidos entre* um **servidor** e um **cliente**. Ele garante a integridade dos dados que são comunicados em uma rede. Antes de transmitir os dados, o *TCP estabelece uma conexão entre uma origem e seu destino, que ele garante que permaneça ativa até que a comunicação comece*. Então, ele divide grandes quantidades de dados em *pacotes menores*, garantindo que a integridade dos dados esteja em vigor durante todo o processo.

Como resultado, o TCP é usado para transmitir dados de protocolos de alto nível que precisam que todos os dados cheguem ao destino. Isso inclui protocolos de compartilhamento ponto a ponto, como File Transfer Protocol (FTP), Secure Shell (SSH) e Telnet. Ele também é usado para enviar e receber e-mails por meio do Protocolo de acesso a mensagens da internet (IMAP), Protocolo dos correios (POP) e Protocolo de transferência de correio simples (SMTP), e para acessar a web por meio do Protocolo de transferência de hipertexto (HTTP).

O TCP pode ser uma ferramenta de rede cara, pois inclui *pacotes ausentes ou corrompidos* e *protege a entrega de dados* com controles como confirmações, inicialização de conexão e controle de fluxo. 

## UDP
Uma alternativa ao TCP é o User Datagram Protocol (UDP), que é *usado para estabelecer conexões de baixa latência* entre aplicativos e *acelerar transmissões*. 

O UDP *não oferece correção de erros ou sequenciamento de pacotes nem sinaliza um destino antes de entregar os dados*, o que o torna **menos confiável**, porém menos caro. Como tal, é uma boa opção para *situações urgentes*, como pesquisa de Sistema de nomes de domínio (DNS), Voz sobre IP (VoIP) e streaming de mídia.

---
<center><h1>IP</h1></center>
## O que é IP

O protocolo de internet (IP) é o *método para enviar dados de um dispositivo para outro pela internet*. Cada dispositivo tem um endereço IP que o identifica exclusivamente e permite que ele se comunique e intercambie dados com outros dispositivos conectados à internet.

O IP é responsável por definir como os aplicativos e dispositivos intercambiam pacotes de dados entre si. É o principal protocolo de comunicações responsável pelos formatos e regras para intercambiar dados e mensagens entre computadores em uma única rede ou várias redes conectadas à internet. Ele faz isso através da Suíte de protocolos para a internet (TCP/IP), um grupo de protocolos de comunicação que *são divididos em quatro camadas de abstração*.

O IP é o protocolo principal dentro da camada de internet do TCP/IP. *Seu objetivo principal é entregar pacotes de dados do aplicativo* ou dispositivo de origem *ao destino usando métodos e estruturas que colocam tags*, como informações de endereço, dentro dos pacotes de dados.
## TCP vs. IP (Protocolo de controle de transmissão, TCP vs. Protocolo de Internet, IP): Qual é a diferença?

O TCP e o IP são protocolos independentes que trabalham juntos para garantir que os dados sejam entregues ao destino pretendido dentro de uma rede. O *IP obtém e define o endereço* — o endereço IP — do aplicativo ou dispositivo para o qual os dados devem ser enviados. O *TCP é responsável por transportar dados* e garantir que eles sejam entregues ao aplicativo ou dispositivo de destino que o IP definiu. 

Em outras palavras, o endereço IP é semelhante a um número de telefone atribuído a um smartphone. O TCP é a versão de rede de computadores da tecnologia usada para fazer o smartphone tocar e permitir que seu usuário fale com a pessoa que ligou para ele. Os dois protocolos são frequentemente usados juntos e dependem um do outro para que os dados tenham um destino e cheguem a ele com segurança, razão pela qual o processo é regularmente chamado de TCP/IP.

---
<center><h1>Funcionamento TCP/IP</h1></center>
## Como funciona o TCP/IP?

O modelo TCP/IP foi desenvolvido pelo Departamento de Defesa dos Estados Unidos para permitir a transmissão precisa e correta de dados entre dispositivos. 
- Ele *divide* as mensagens em pacotes para *não ter que reenviar a mensagem inteira* caso encontre um *problema* durante a transmissão. 
- Os pacotes são *remontados* assim que chegam ao seu *destino*. 
- *Cada pacote pode seguir uma rota diferente* entre o computador de origem e o computador de destino, se a rota original usada se tornar congestionada ou indisponível.

## Camadas

O TCP/IP divide as tarefas de comunicação em camadas que mantêm o processo padronizado, sem que os provedores de hardware e software tenham que tentar gerenciá-lo por conta própria. 

- Os pacotes de dados devem passar por *quatro camadas antes de serem recebidos* pelo dispositivo de destino; 
- Depois, o TCP/IP passa pelas camadas *na ordem inversa* para colocar a mensagem de volta em seu formato original. 

Como um protocolo orientado à conexão, o *TCP estabelece e mantém uma conexão entre aplicativos ou dispositivos até que eles concluam o intercâmbio de dados*. Ele determina como a mensagem original deve ser dividida em pacotes, numera, remonta os pacotes, os envia para outros dispositivos na rede, como roteadores, gateways de segurança e switches e, depois, para o destino deles. O TCP também envia e recebe pacotes da camada de rede, lida com a transmissão de todos os pacotes perdidos, gerencia o controle de fluxo e garante que todos os pacotes cheguem ao seu destino.

Um bom exemplo de como isso funciona na prática é quando um e-mail é enviado usando o SMTP de um servidor de e-mail. A camada TCP no servidor divide a mensagem em pacotes, numera-os e os encaminha para a camada IP, que depois transporta cada pacote para o servidor de e-mail de destino. Quando os pacotes chegam, eles são devolvidos à camada TCP para serem remontados no formato de mensagem original e devolvidos ao servidor de e-mail, que entrega a mensagem à caixa de entrada de e-mail do usuário.

O TCP/IP usa um handshake de três vias para estabelecer uma conexão entre um dispositivo e um servidor, o que garante que várias conexões de soquete TCP possam ser transferidas em ambas as direções simultaneamente. Tanto o dispositivo quanto o servidor devem sincronizar e confirmar os pacotes antes do início da comunicação, depois, eles podem negociar, separar e transferir conexões de soquete TCP.

## As 4 camadas do modelo TCP/IP

O modelo TCP/IP define como os dispositivos devem transmitir dados entre eles e permite a comunicação por redes e grandes distâncias. O modelo representa como os dados são intercambiados e organizados em redes. Ele é dividido em quatro camadas, que definem os padrões para intercâmbio de dados e representam como os dados são tratados e empacotados quando entregues entre aplicativos, dispositivos e servidores.

As quatro camadas do modelo TCP/IP são as seguintes:

1. Camada DataLink: A camada DataLink define como os dados devem ser enviados, lida com o ato físico de enviar e receber dados e é responsável pela transmissão de dados entre aplicativos ou dispositivos em uma rede. Isso inclui definir como os dados devem ser sinalizados por hardware e outros dispositivos de transmissão em uma rede, como um driver de dispositivo de computador, um cabo Ethernet, uma placa de interface de rede (NIC) ou uma rede sem fio. Ela também é chamada de camada de link, camada de acesso de rede, camada de interface de rede ou camada física e é a combinação das camadas físicas e de link de dados do [modelo de Interconexão de Sistemas Abertos (OSI)](https://www.fortinet.com/br/resources/cyberglossary/osi-model), que padroniza as funções de comunicação em sistemas de computação e telecomunicações.
2. Camada de internet: A camada de internet é responsável por enviar pacotes a partir de uma rede e controlar seu movimento na rede para garantir que eles cheguem ao seu destino. Ele fornece as funções e procedimentos para transferir sequências de dados entre aplicativos e dispositivos em redes.
3. Camada de transporte: A camada de transporte é responsável por fornecer uma conexão de dados sólida e confiável entre o aplicativo ou dispositivo original e seu destino pretendido. Este é o nível onde os dados são divididos em pacotes e numerados para criar uma sequência. A camada de transporte então determina quantos dados devem ser enviados, para onde devem ser enviados e a que taxa. Ela garante que os pacotes de dados sejam enviados sem erros e em sequência e obtém a confirmação de que o dispositivo de destino recebeu os pacotes de dados.
4. Camada de aplicativo: A camada de aplicativo se refere a programas que precisam de TCP/IP para ajudá-los a se comunicar uns com os outros. Esse é o nível com o qual os usuários normalmente interagem, como sistemas de e-mail e plataformas de mensagens. Ele combina as camadas de sessão, apresentação e aplicativo do modelo OSI.

## Seus pacotes de dados são privados no TCP/IP?

Os pacotes de dados enviados por TCP/IP não são privados, o que significa que podem ser vistos ou interceptados. Por esse motivo, é vital evitar o uso de redes Wi-Fi públicas para enviar dados privados e garantir que as informações sejam criptografadas. Uma maneira de criptografar dados que são compartilhados por meio de TCP/IP é por meio de uma [rede privada virtual (VPN).](https://www.fortinet.com/br/resources/cyberglossary/what-is-a-vpn)

### O que é TCP e quais são seus tipos?

TCP é um protocolo ou padrão usado para garantir que os dados sejam entregues com sucesso de um aplicativo ou dispositivo para outro. O TCP faz parte do Protocolo de Controle de Transmissão/Protocolo de Internet (TCP/IP), que é um conjunto de protocolos originalmente desenvolvido pelo Departamento de Defesa dos EUA para apoiar a construção da internet. O modelo TCP/IP consiste em vários tipos de protocolos, incluindo TCP e IP, protocolo de resolução de endereço (ARP), protocolo de mensagem de controle de internet (ICMP), protocolo de resolução de endereço reverso (RARP) e User Datagram Protocol (UDP).

O TCP é o mais comumente usado desses protocolos e é responsável pela maior parte do tráfego usado em uma rede TCP/IP. O UDP é uma alternativa ao TCP que não fornece correção de erros, é menos confiável e tem menos sobrecarga, o que o torna ideal para streaming.