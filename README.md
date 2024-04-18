# Algoritmos de Escalonamento de Disco

Este projeto implementa e avalia os algoritmos de escalonamento de disco FCFS (First-Come-First-Served) e SCAN (e C-SCAN). O objetivo é simular o movimento do braço de leitura/gravação de um disco para diferentes sequências de acessos.

## Descrição

O programa foi desenvolvido em Python e utiliza uma sequência aleatória de acessos a cilindros em um disco de 5.000 cilindros numerados de 0 a 4.999. A sequência de 1.000 acessos é a mesma para todas as análises.

### Algoritmos Implementados

- **FCFS (First-Come-First-Served)**: Esse algoritmo processa os acessos na ordem em que chegam, sem considerar a localização atual do braço de leitura/gravação.
  
- **SCAN**: Também conhecido como algoritmo "elevador", o SCAN move o braço de leitura/gravação na direção atual até o final do disco, depois muda de direção e retorna, atendendo aos acessos no caminho de ida e volta.
  
- **C-SCAN**: Semelhante ao SCAN, mas após alcançar o final do disco, o braço retorna imediatamente para o início do disco, sem atender a acessos no caminho de volta.

## Execução

Para executar o programa, certifique-se de ter Python instalado em sua máquina. Clone o repositório e execute o arquivo `main.py`.

\`\`\`bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python main.py
\`\`\`

## Resultados

Os resultados são reportados para tamanhos de fila de 10, 20, 50, 100, 200, 500 e 1.000 acessos. A saída exibe o número de cilindros percorridos pelo braço de leitura/gravação para cada algoritmo e tamanho de fila.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.
