O processo de troca de loads é feito nos notebooks da *PPV*, usando o *Software Manager*.

---
## O que é um Load?
Um Load da aviônica é análogo ao versionamento de um sistema operacional, sendo necessário com que *o notebook e a aeronave estejam no mesmo Load*.

## Registros
É esperado que pela interação Software Manager e Load tenham registros que *são requisitados sempre na manipulação*. Algo que esteja setado no registro ocorrerá sempre que o Load for carregado no Software Manager.

---
<center><h1>Problemas Comuns</h1></center>
## Case Sensitivismo
Neologismos a parte, este é um problema do E1 causado pelo *registro* carregando o *arquivo com nome em minúsculo*.

Para solucionar, altere os arquivos *.reg* em *C:\LOADSE1* colocando onde fica *"File"="C:\\FLIGHTLINE\\TIU\\SYSTEM.CFG* com o final (system.cfg) em letra minúscula.

Os arquivos de load do E1 encontram-se em "*\\flmfs02\sistemas2\SINTEGT\Software Manager PPV - Procedimentos\LOADSE1*"