

def generate(program_content, row_nums):
    for col_num in col_nums:
        for row_num in row_nums:
            filename = f"{filename_head}_{col_num}col_{row_num:08d}.py"
            dataset_filename = f"{filename_head}_{col_num}col_{row_num}.csv"
            full_path = destination_dir + filename
            f = open(full_path, "w") 
            f.write(program_content % (dataset_filename))
        f.close()

def generate_nn_code(program_content, row_nums):
    for row_num in row_nums:
        filename = f"{filename_head}_{row_num}.py"
        full_path = destination_dir + filename
        f = open(full_path, "w") 
        f.write(program_content % (row_num, row_num))
    f.close()

destination_dir = "programs/neural_network/mnist/code_test/"
filename_head = 'mnist' # w_IntegerX100Temp # w_Float2DigitsTemp
# row_nums = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
#             10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
#             1000_000,1250_000,1500_000,1750_000,2000_000]
# row_nums = [i*(10**power) for power in range(1, 5) 
#                 for i in range(1, 10)] + [100_000]
# row_nums = (1234,2300,15151,22000,43000,48000,74000,82820,94444)
# row_nums = [str(i*(10**power)) for power in range(1, 3) 
#                 for i in range(1, 10)] + [str(i*1000) for i in range(1, 6)]
# row_nums = [i*(10**power) for power in range(1, 4) 
                # for i in range(1, 10)] + [i*10000 for i in range(1, 7)]
row_nums_test = [26, 97, 150, 373, 642, 1234, 4880, 7601, 7899, 11890, 33333, 53011]
col_nums = (0,)


program_activity_content = \
"""
import pandas
import sklearn
import sklearn.model_selection
from sklearn.naive_bayes import GaussianNB


def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()
RANDOM_STATE = 10

df = pandas.read_csv('data/activity/%s')

# Split data
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.2, random_state=RANDOM_STATE)
gnb = GaussianNB()
gnb.fit(X_train, Y_train)

# Evaluate
pred = gnb.predict(X_test)
print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))


function_end()
############################################
"""
program_weather_content = \
"""
import pandas
import sklearn
import sklearn.model_selection
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()
RANDOM_STATE = 10

df = pandas.read_csv('data/weather/%s')

# Split data
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

# Train
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
                                    X, Y, test_size=0.2, random_state=RANDOM_STATE)
regression = linear_model.LinearRegression()
regression.fit(X_train, Y_train)

# Evaluate
pred = regression.predict(X_test)
print('Test Set RMSE: ' + str(mean_squared_error(Y_test, pred)))

function_end()
############################################
"""
mnist_program = \
"""
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

    print('\\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%%)\\n'.format(
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

print('Train on', int(%d), 'images')
train_loader = list(torch.utils.data.DataLoader(dataset1))[:%d]
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
"""

mnist_program_3layers = \
"""
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
        self.linear1 = nn.Linear(784, 128)
        self.linear2 = nn.Linear(128, 32)
        self.linear3 = nn.Linear(32, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = self.linear1(x)
        x = torch.sigmoid(x)
        x = self.linear2(x)
        x = torch.sigmoid(x)
        x = self.linear3(x)
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

    print('\\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%%)\\n'.format(
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

print('Train on', int(%d), 'images')
train_loader = list(torch.utils.data.DataLoader(dataset1))[:%d]
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
"""


generate_nn_code(mnist_program, row_nums_test)
# print(row_nums)