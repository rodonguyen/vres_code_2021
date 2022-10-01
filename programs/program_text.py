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
mnist_3layers = \
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

mnist_program_4layers = \
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



mnist_13layers = \
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
        self.conv1 = nn.Conv2d(1, 8, 3, 1, 1)
        self.conv2 = nn.Conv2d(8, 8, 3, 1, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.batchnorm1 = nn.BatchNorm2d(8)
        self.conv3 = nn.Conv2d(8, 16, 3, 1, 1)
        self.conv4 = nn.Conv2d(16, 16, 3, 1, 1)
        self.batchnorm2 = nn.BatchNorm2d(16)
        self.dropout2 = nn.Dropout(0.25)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(3136, 256)
        self.linear2 = nn.Linear(256, 32)
        self.linear3 = nn.Linear(32, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.batchnorm1(x)
        x = self.dropout1(x)
        x = F.max_pool2d(x, 2)

        x = self.conv3(x)
        x = F.relu(x)
        x = self.conv4(x)
        x = F.relu(x)
        x = self.batchnorm2(x)
        x = self.dropout2(x)

        x = self.flatten(x)
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

print('Train on %d images')
train_loader = list(torch.utils.data.DataLoader(dataset1))[:%d]
test_loader = list(torch.utils.data.DataLoader(dataset2))[:10]

# Initialise and Train
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


mnist_6layers = \
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
        self.conv1 = nn.Conv2d(1, 4, 3, 1, 1)
        self.conv2 = nn.Conv2d(4, 8, 3, 1, 1)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(6272, 256)
        self.linear2 = nn.Linear(256, 32)
        self.linear3 = nn.Linear(32, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        
        x = self.flatten(x)
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

print('Train on %d images')
train_loader = list(torch.utils.data.DataLoader(dataset1))[:%d]
test_loader = list(torch.utils.data.DataLoader(dataset2))[:10]

# Initialise and Train
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


program_gan_mnist = \
"""
import torch
from torchvision import datasets, transforms

def function_start():
    print('-----')

def function_end():
    print('-----')

############################################
function_start()

torch.manual_seed(10)

def denorm(x):
    out = (x + 1) / 2
    return out.clamp(0, 1)

# Prepare data
transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
    ])
mnist = datasets.MNIST(root='data', 
                train=True, 
                # download=True,
                transform=transform)

batch_size = %d
data_loader = torch.utils.data.DataLoader(mnist, batch_size)
device = torch.device('cpu')    #'cuda'

image_size = 784
hidden_size = 256

Discriminator = torch.nn.Sequential(
    torch.nn.Linear(image_size, hidden_size),
    torch.nn.LeakyReLU(0.2),
    torch.nn.Linear(hidden_size, hidden_size),
    torch.nn.LeakyReLU(0.2),
    torch.nn.Linear(hidden_size, 1),
    torch.nn.Sigmoid())
Discriminator.to(device)

latent_size = 64
Generator = torch.nn.Sequential(
            torch.nn.Linear(latent_size, hidden_size),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_size, image_size),
            torch.nn.Tanh())
Generator.to(device)

######################################################################################
# Discriminator training functions

criterion = torch.nn.BCELoss()
disciminator_optimizer = torch.optim.Adam(Discriminator.parameters(), lr=0.0002)
generator_optimizer = torch.optim.Adam(Generator.parameters(), lr=0.0002)


def reset_grad():
    disciminator_optimizer.zero_grad()
    generator_optimizer.zero_grad()

def train_discriminator(images):
    # Create the labels which are later used as input for the BCE loss
    real_labels = torch.ones(batch_size, 1).to(device)
    fake_labels = torch.zeros(batch_size, 1).to(device)
        
    # Loss for real images
    outputs = Discriminator(images)
    d_loss_real = criterion(outputs, real_labels)
    real_score = outputs

    # Loss for fake images
    z = torch.randn(batch_size, latent_size).to(device)
    fake_images = Generator(z)
    outputs = Discriminator(fake_images)
    d_loss_fake = criterion(outputs, fake_labels)
    fake_score = outputs

    # Combine losses
    d_loss = d_loss_real + d_loss_fake
    # Reset gradients
    reset_grad()
    # Compute gradients
    d_loss.backward()
    # Adjust the parameters using backprop
    disciminator_optimizer.step()
    
    return d_loss, real_score, fake_score

def train_generator():
    # Generate fake images and calculate loss
    z = torch.randn(batch_size, latent_size).to(device)
    fake_images = Generator(z)
    labels = torch.ones(batch_size, 1).to(device)
    g_loss = criterion(Discriminator(fake_images), labels)

    # Backprop and optimize
    reset_grad()
    g_loss.backward()
    generator_optimizer.step()
    return g_loss, fake_images

###############################################################################
# Training
num_epochs = 10  
total_step = len(data_loader)

for epoch in range(num_epochs):
    for i, (images, _) in enumerate(data_loader):
        # Load a batch & transform to vectors
        images = images.reshape(batch_size, -1).to(device)
        # Train the discriminator and generator
        d_loss, real_score, fake_score = train_discriminator(images)
        g_loss, fake_images = train_generator()
        
        # Inspect the losses
        print('Epoch [{}/{}], Step [{}/{}], d_loss: {:.4f}, g_loss: {:.4f}, D(x): {:.2f}, D(G(z)): {:.2f}' 
                .format(epoch+1, num_epochs, i+1, total_step, d_loss.item(), g_loss.item(), 
                        real_score.mean().item(), fake_score.mean().item()))
        break

function_end()
"""