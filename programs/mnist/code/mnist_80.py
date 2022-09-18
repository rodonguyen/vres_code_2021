
# https://github.com/pytorch/examples/blob/main/mnist/main.py

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR

def function_start():
    print('-----')

def function_end():
    print('-----')

############################################
function_start()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(784, 32)
        self.linear2 = nn.Linear(32, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.linear1(x)
        x = torch.sigmoid(x)
        x = self.linear2(x)
        output = F.log_softmax(x, dim=1)
        return output


def train(model, train_loader, optimizer, epoch):
    model.train()
    for data, target in train_loader:
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()

def test(model, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader),
        100. * correct / len(test_loader)))

torch.manual_seed(10)

# Prepare data
transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
    ])
dataset1 = datasets.MNIST('data', train=True, # download=True,
                transform=transform)
dataset2 = datasets.MNIST('data', train=False,
                transform=transform)

print('Train on', int(80), 'images')
train_loader = list(torch.utils.data.DataLoader(dataset1))[:80]
test_loader = list(torch.utils.data.DataLoader(dataset2))[:10]

# Initialise and Train
log_interval = 10
epochs = 1
model = Net()
optimizer = optim.Adadelta(model.parameters(), lr=1)
scheduler = StepLR(optimizer, step_size=1, gamma=0.7)
for epoch in range(epochs):
    train(model, train_loader, optimizer, epoch)
    scheduler.step()

# Test
test(model, test_loader)

function_end()
