## O que é bat
Um arquivo *batch* é um arquivo texto contendo linhas com comandos que podem ser executados sequencialmente pelo interpretador de comandos do Windows.

## Nosso uso
No GRASIT, já possuímos o executável de um arquivo .py (executável é necessário para rodar sem necessitar de python instalado). Precisaremos transformar em .bat agora para colocar o script como execução ao iniciar o computador (e de forma mais robusta que o agendador de tarefas).

Para isso, digite ``gpedit.msc`` e siga os passos:
- Abra o Windows settings
![[Pasted image 20250121134958.png]]

- Vá em scripts
![[Pasted image 20250121135028.png]]

- Vá em Startup e adicione o local do seu .bat
![[Pasted image 20250121135101.png]]