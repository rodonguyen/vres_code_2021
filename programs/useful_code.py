model = Net()
print(model)
from torchsummary import summary
summary(model, input_size=(1,28,28), device='cpu')