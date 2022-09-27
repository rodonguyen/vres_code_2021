# adapted from https://jovian.ai/aakashns/06-mnist-gan
import torch
import numpy
from torchvision import datasets, transforms

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

batch_size = 10
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


######################################################################################
# Training the Model

# sample_dir = 'programs/gan_mnist/samples'
# if not os.path.exists(sample_dir):
#     os.makedirs(sample_dir)

# # Save some real images
# for images, _ in data_loader:
#     images = images.reshape(images.size(0), 1, 28, 28)
#     utils.save_image(denorm(images), os.path.join(sample_dir, 'real_images.png'), nrow=10)
#     break
# Image(os.path.join(sample_dir, 'real_images.png'))


# sample_vectors = torch.randn(batch_size, latent_size).to(device)
# def save_fake_images(index):
#     fake_images = Generator(sample_vectors)
#     fake_images = fake_images.reshape(fake_images.size(0), 1, 28, 28)
#     fake_fname = 'fake_images_{0:0=4d}.png'.format(index)
#     print('Saving', fake_fname)
#     utils.save_image(denorm(fake_images), os.path.join(sample_dir, fake_fname), nrow=10)


######################################################################################
# # Before training
# save_fake_images(0)

# Training
num_epochs = 1      # 100 originally
total_step = len(data_loader)
d_losses, g_losses, real_scores, fake_scores = [], [], [], []

for epoch in range(num_epochs):
    for i, (images, _) in enumerate(data_loader):
        # Load a batch & transform to vectors
        print(numpy.shape(images))
        images = images.reshape(batch_size, -1).to(device)
        print(numpy.shape(images))
        # Train the discriminator and generator
        d_loss, real_score, fake_score = train_discriminator(images)
        g_loss, fake_images = train_generator()
        
        # Inspect the losses
        d_losses.append(d_loss.item())
        g_losses.append(g_loss.item())
        real_scores.append(real_score.mean().item())
        fake_scores.append(fake_score.mean().item())
        print('Epoch [{}/{}], Step [{}/{}], d_loss: {:.4f}, g_loss: {:.4f}, D(x): {:.2f}, D(G(z)): {:.2f}' 
                .format(epoch, num_epochs, i+1, total_step, d_loss.item(), g_loss.item(), 
                        real_score.mean().item(), fake_score.mean().item()))
        break

    # # Sample and save images
    # if epoch+1 % 10 == 0:
    #     save_fake_images(epoch+1)

# # Save the model checkpoints 
# torch.save(Generator.state_dict(), 'G.ckpt')
# torch.save(Discriminator.state_dict(), 'D.ckpt')















