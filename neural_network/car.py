
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()

# df = pd.read_csv('dataset_real/car.csv')
# x = df.iloc[:,1:-1]
# y = df.iloc[:,-1:]

# X = torch.tensor(x.values.astype(np.float32))
# y = torch.tensor(y.values.astype(np.float32))
# print("Dataset shape: \n", df.shape)
torch.random.manual_seed(42)

data = np.loadtxt('dataset_real/car.csv', dtype=np.float32, delimiter=',', skiprows=1)
X = torch.from_numpy(data[:,1:-1])
y = torch.from_numpy(data[:,-1,None])

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

for t in range(100):
    y_pred = net(X)
    loss = criterion(y_pred, y)
    # print(t, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print('Predict row 1: ' + str(net(X[0])))
print(data.shape, X.shape, y.shape)

function_end()
############################################

