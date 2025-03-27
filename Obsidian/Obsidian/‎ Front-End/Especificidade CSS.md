_Especificidade_ é o critério usado pelos navegadores para determinar quais regras CSS terão prioridade quando houver conflito entre seletores.

## Como funciona a especificidade?

A especificidade é calculada com base nos tipos de seletores usados. O navegador atribui um peso a cada tipo e resolve os conflitos considerando esse peso.

A hierarquia básica de especificidade segue este padrão:

![[Pasted image 20250326153056.png | center]]

Se houver um empate, a regra que aparece por último no código será aplicada.

## Exemplo prático

Dado o seguinte CSS:

```css
p {
  color: blue;
}

.texto-vermelho {
  color: red;
}

#meu-paragrafo {
  color: green;
}

<p id="meu-paragrafo" class="texto-vermelho">Texto colorido</p>
```

Neste caso, a cor do texto será _verde_ pois o seletor de ID tem maior especificidade.

## Dicas para evitar problemas com especificidade

- Prefira usar classes em vez de IDs sempre que possível.
    
- Evite o uso excessivo de `!important`, pois pode dificultar a manutenção do código.
    
- Mantenha a hierarquia do CSS organizada para evitar conflitos desnecessários.
    
- Utilize seletores mais específicos apenas quando necessário.
    

## Calculando a especificidade

A especificidade pode ser representada por um sistema de pontos:

- **Inline:** (1,0,0,0)
    
- **ID:** (0,1,0,0)
    
- **Classe, atributo e pseudoclasse:** (0,0,1,0)
    
- **Elemento e pseudoelemento:** (0,0,0,1)
    

O seletor com a pontuação mais alta será aplicado.

### Exemplo de cálculo

```css
#cabecalho p.destaque {
  color: orange;
}
```

Especificidade: (0,1,1,1)

```css
h1 {
  color: blue;
}
```

Especificidade: (0,0,0,1)

O primeiro seletor será aplicado por ter maior especificidade.

---

Compreender a especificidade ajuda a escrever CSS mais eficiente e previsível!