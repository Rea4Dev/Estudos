Aqui é uma versão resumida, caso queira algo completo consulte [Comandos Git - Aprenda Git do básico ao avançado](https://comandosgit.github.io/)

# Fazendo Login

A primeira coisa que você deve fazer quando instalar o Git é definir o seu nome de usuário e endereço de e-mail. Isso é importante porque todos os commits no Git utilizam essas informações, e está imutavelmente anexado nos commits que você realiza:

```Bash
git config --global user.name "John Doe"  
git config --global user.email johndoe@example.com
```

Relembrando, você só precisará fazer isso uma vez caso passe a opção --global, pois o Git sempre usará essa informação para qualquer coisa que você faça nesse sistema. Caso você queira sobrepor estas com um nome ou endereço de e-mail diferentes para projetos específicos, você pode executar o comando sem a opção --global quando estiver no próprio projeto.

# Obtendo Ajuda

Se você precisar de ajuda ao usar Git, existem três maneiras de obter a ajuda para qualquer um dos comandos Git:

```Bash
git help {comando}  
git {comando} --help  
man git- {comando}
```

# Mudando de diretório
```bash
cd ~/Desktop/Exemplo
```

# Criando e escrevendo um arquivo
```Bash
echo "# Título de Exemplo" >> README.md
```

# Iniciando um repositório em sua Máquina
```Bash
git init
```

# Adicionando arquivo na Stagging Area
```Bash
git add README.md
```

# Removendo arquivo da Stagging Area
```bash
git rm --cached README.md
```

# Visualizando Estado
```Bash
git status
```

# Dando Commit
```bash
git commit -m "Mensagem de Commit"
```

# Criando uma nova Branch
```bash
git branch -M nome_da_branch
```

# Adicionando o repositório local no da Web
```bash
git remote add origin https://github.com/seulink/seulink.git
```

# Dando push de um diretório para repositório
```bash
git push -u origin main
```