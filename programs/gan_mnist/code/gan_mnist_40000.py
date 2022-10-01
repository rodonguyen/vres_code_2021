
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

batch_size = 40000
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
