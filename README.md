# Perceptron e portas lógicas

## Enunciado 
Atividade para implementar um perceptron capaz de ser treinado para reproduzir o comportamento das seguintes portas lógicas:
- AND
- OR
- NAND
- XOR

# Explicação do código

#### Classe `Perceptron`:
- Um perceptron é uma unidade básica de uma rede neural, composta por pesos, um limiar e uma função de ativação.
- `__init__`: Inicializa os pesos, o limiar e o viés (bias) do perceptron.
- `activation_function`: Define uma função degrau como função de ativação.
- `predict`: Realiza a predição do perceptron com base nas entradas dadas.

#### Implementação de Portas Lógicas:
- São criadas quatro classes (`AND`, `ORG`, `NAND`, `XOR`) para representar as portas lógicas.
- Cada classe usa um perceptron com pesos e limiares específicos para implementar a função da porta lógica correspondente.
- `XOR` combina perceptrons de AND, OR e NAND para implementar a função XOR.

### Uai, por que o XOR não funcionou?
O resultado que encontramos exemplifica as restrições de um perceptron simple. A porta XOR representa um dilema não separável linearmente, indicando que não é viável estabelecer uma única linha reta que consiga delimitar de maneira precisa as saídas 0 e 1. 

Ou seja, precisamos de um trem melhor pra resolver ele...

## Video demonstração:
[Screencast from 03-12-2023 20:06:41.webm](https://github.com/Bianca-Cassemiro/Perceptron/assets/99203402/7c9d9f34-cd3d-41ad-830e-f4eb4ca949eb)
