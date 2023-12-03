import numpy as np

class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = np.array(weights)
        self.threshold = threshold
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        linear_output = np.dot(inputs, self.weights) + self.bias
        y_predicted = self.activation_function(linear_output)
        return y_predicted

class AND:
    def __init__(self):
        self.perceptron = Perceptron([1, 1], 2)

    def predict(self, inputs):
        return self.perceptron.predict(inputs)

class OR:
    def __init__(self):
        self.perceptron = Perceptron([1, 1], 1)

    def predict(self, inputs):
        return self.perceptron.predict(inputs)

class NAND:
    def __init__(self):
        self.perceptron = Perceptron([-1, -1], -2)

    def predict(self, inputs):
        return self.perceptron.predict(inputs)

class XOR:
    def __init__(self):
        self.and_gate = AND()
        self.or_gate = OR()
        self.nand_gate = NAND()

    def predict(self, inputs):
        return self.or_gate.predict([self.and_gate.predict(inputs), self.nand_gate.predict(inputs)])

if __name__ == "__main__":
    and_gate = AND()
    or_gate = OR()
    nand_gate = NAND()
    xor_gate = XOR()

    print("AND Gate:")
    print(and_gate.predict(np.array([0, 0])))  # Saída esperada: 0
    print(and_gate.predict(np.array([0, 1])))  # Saída esperada: 0
    print(and_gate.predict(np.array([1, 0])))  # Saída esperada: 0
    print(and_gate.predict(np.array([1, 1])))  # Saída esperada: 1

    print("\nOR Gate:")
    print(or_gate.predict(np.array([0, 0])))   # Saída esperada: 0
    print(or_gate.predict(np.array([0, 1])))   # Saída esperada: 1
    print(or_gate.predict(np.array([1, 0])))   # Saída esperada: 1
    print(or_gate.predict(np.array([1, 1])))   # Saída esperada: 1

    print("\nNAND Gate:")
    print(nand_gate.predict(np.array([0, 0])))  # Saída esperada: 1
    print(nand_gate.predict(np.array([0, 1])))  # Saída esperada: 1
    print(nand_gate.predict(np.array([1, 0])))  # Saída esperada: 1
    print(nand_gate.predict(np.array([1, 1])))  # Saída esperada: 0

    print("\nXOR Gate:")
    print(xor_gate.predict(np.array([0, 0])))   # Saída esperada: 0
    print(xor_gate.predict(np.array([0, 1])))   # Saída esperada: 1
    print(xor_gate.predict(np.array([1, 0])))   # Saída esperada: 1
    print(xor_gate.predict(np.array([1, 1])))   # Saída esperada: 0
