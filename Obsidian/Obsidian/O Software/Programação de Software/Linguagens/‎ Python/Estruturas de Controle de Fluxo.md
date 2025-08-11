# Comandos de Controle de Fluxo

## Break

O comando break interrompe imediatamente o laço, saindo do loop mesmo que a condição ainda seja verdadeira ou que existam elementos restantes na sequência.
```python
for numero in range(1, 10):
    if numero == 5:
        break
    print(numero)
```

## Continue

O comando continue faz com que a iteração atual seja interrompida, passando para a próxima iteração do loop.
```python
for numero in range(1, 10):
    if numero % 2 == 0:
        continue
    print(numero)
```
## Pass

O comando pass não realiza nenhuma ação. Ele serve como um espaço reservado quando um comando é sintaticamente necessário, mas nenhuma ação precisa ser executada.
```python
for i in range(5):
    pass  # Implementação futura
```
