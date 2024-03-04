import numpy as np

input_vector = np.array([2, 1.5])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

target = 0

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2

prediction = make_prediction(input_vector, weights_1, bias)

mse = np.square(prediction - target)
print(f"the result is: {prediction}; Error: {mse}")

derivative = 2*(prediction - target)
print(f"the derivative is {derivative}")

weight_1 = weights_1 -derivative
prediction = make_prediction(input_vector, weight_1, bias)
error = (prediction-target)**2
print(f"prediction: {prediction}; error:{error}")

