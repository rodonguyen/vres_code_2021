import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn import datasets

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()

torch.random.manual_seed(40)

X, y = datasets.load_diabetes(return_X_y=True)
X = torch.from_numpy(X).float()
y = torch.from_numpy(y).float()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(X.shape[1], 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net = Net()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

for t in range(8):
    y_pred = net(X)
    loss = criterion(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print('Predict:\n' + str(net(X[0:5])))
print('Actual:\n' + str(y[0:5]))
print(X.shape, y.shape)

function_end()
############################################

