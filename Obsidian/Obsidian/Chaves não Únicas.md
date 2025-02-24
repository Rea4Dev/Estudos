- **Definição:**  
    Uma chave não única é um atributo ou conjunto de atributos que pode identificar registros, mas não de forma exclusiva.
    
- **Permite Repetição dos Valores:**  
    Os mesmos valores podem ocorrer em múltiplos registros, permitindo que diversas linhas compartilhem a mesma informação nessa coluna ou conjunto de colunas.
    
- **Uso em Agrupamentos e Classificações:**  
    Geralmente utilizada para categorizar ou agrupar dados, ela não serve para identificar uma única linha, mas para organizar registros com características em comum.
    
- **Exemplo Prático:**  
    Em uma tabela de funcionários, a coluna “Departamento” pode ser uma chave não única, pois vários funcionários podem pertencer ao mesmo departamento.
    
- **Integridade Referencial:**  
    Embora não garanta a unicidade, chaves não únicas podem ser empregadas em relacionamentos—por exemplo, como parte de uma junção—desde que não sejam utilizadas para identificar exclusivamente registros.
    
- **Restrições:**  
    Diferente de uma chave única, não há restrição de repetição dos valores; ela pode inclusive permitir valores nulos, conforme definido pelas regras do modelo de dados.