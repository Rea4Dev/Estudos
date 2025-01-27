Um sinal diferencial é uma técnica de transmissão de dados em que *a informação é transportada pela diferença de tensão entre dois fios*, em vez de usar um único fio para transportar o sinal em relação a um ponto de referência comum (como o terra).

---
<center><h1>Como funciona?</h1></center>
Existem dois condutores: linha positiva (A) e linha negativa (B).
O dado é representado pela diferença de potencial (A - B) entre os dois fios:

- Quando o sinal é 1 lógico, a tensão em A é maior que em B.
- Quando o sinal é 0 lógico, a tensão em A é menor que em B.

O receptor interpreta a diferença de tensão para determinar o valor lógico, ignorando tensões absolutas de A ou B em relação ao terra.

---

<center><h1>Por que usar sinais diferenciais?</center></h1>
Resistência a ruídos:
Como os dois fios estão próximos, *qualquer interferência externa afeta os dois fios igualmente*. O receptor só considera a diferença entre os dois sinais, anulando o ruído.
Isso é conhecido como *rejeição de modo comum*.

Menor interferência eletromagnética:
Correntes opostas nos dois fios criam *campos magnéticos que se cancelam*, reduzindo a interferência no ambiente.

Maior alcance e velocidade:
Sinais diferenciais permitem *transmissão em longas distâncias e em taxas altas de dados sem degradação significativa*.

---

<center><h1>Onde são usados?</center></h1>

## Comunicação serial industrial e aeronáutica:
- ARINC 429;
- RS-485;
- CAN Bus;
- I2C (em algumas variantes).

## Interfaces de alta velocidade:
- HDMI;
- USB;
- Ethernet.

## Sensores: 
Sinais diferenciais são comuns em sensores analógicos para maior precisão, como em acelerômetros.