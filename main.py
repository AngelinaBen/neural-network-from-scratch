from neurons import Neuron

weights=[0.2,0.7,0.4]
bias=4

inputs=[5,4,8]

neuron=Neuron(weights,bias)
output=neuron.forward(inputs)

print(output)