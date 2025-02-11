# Resumo do Protocolo MQTT
## O que é o MQTT?

O MQTT (Message Queuing Telemetry Transport) é um protocolo de comunicação leve, baseado no modelo [[publish-subscribe]]. 
Criado em 1999 por Andy Stanford-Clark (da IBM) e Arlen Nipper (da Cirrus Link) *para possibilitar a troca de mensagens entre dispositivos com recursos limitados e redes de baixa largura de banda*, ele se tornou um dos pilares das aplicações de IoT (Internet das Coisas).

## Vantagens do MQTT

- **Baixo consumo de recursos**  
  Ideal para dispositivos com hardware restrito, o MQTT utiliza cabeçalhos compactos e requer pouca memória e processamento, permitindo a implementação em *microcontroladores e sensores*

- **Eficiência e velocidade**  
  Seu design simples possibilita uma troca rápida de mensagens, com tráfego reduzido na rede. Essa eficiência é especialmente útil em ambientes onde a largura de banda é limitada

- **Confiabilidade**  
  Com suporte a diferentes níveis de Qualidade de Serviço (QoS):
  - **QoS 0:** A mensagem é enviada uma única vez, sem confirmação.
  - **QoS 1:** Garante que a mensagem seja entregue pelo menos uma vez, com confirmação.
  - **QoS 2:** Assegura a entrega exatamente uma vez, utilizando um handshake mais complexo.  
  Esses níveis permitem ajustar a confiabilidade conforme a necessidade da aplicação 

- **Escalabilidade e desacoplamento**  
  O modelo publish/subscribe desacopla o remetente do destinatário, o que facilita a integração e a comunicação com um grande número de dispositivos sem que eles precisem conhecer uns aos outros

- **Facilidade de implementação**  
  Com amplo suporte em diversas linguagens de programação e bibliotecas prontas, o MQTT é simples de integrar em projetos, acelerando o desenvolvimento de soluções IoT 
## Considerações Finais

O MQTT se destaca por sua leveza e eficiência, sendo ideal para aplicações onde o consumo de recursos e a largura de banda são críticos. Por essas razões, ele é amplamente utilizado em automação industrial, monitoramento remoto, sistemas de telemetria e em qualquer cenário que exija comunicação rápida e confiável entre dispositivos.

