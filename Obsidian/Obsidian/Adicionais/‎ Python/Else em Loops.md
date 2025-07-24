# Uso do else em Loops

Em Python, tanto o while quanto o for podem ser acompanhados de um bloco else. Esse bloco é executado quando o loop termina normalmente (ou seja, sem que haja uma interrupção com break).

```python
for i in range(3):
    print(i)
else:
    print("Loop concluído sem interrupções!")
```

**Nota**: Se o loop for interrompido por um break, o bloco else não será executado.