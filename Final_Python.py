# %%
import numpy as np
import matplotlib.pyplot as plt
# 1) Input and Output with Numpy
# We already saw how to read file in Python 
# However, the creators of numpy have made it even easier
'''
# Fill in 
Data = np.genfromtxt('ReadFile.csv', delimiter=',')
print(Data)

# Write the file using numpy
# Fill in 
np.savetxt('DataFile.csv',Data)

# %%
# If we have a more complex array, we can use another  
# type of file format, called pickle file format
# It is a binary file format, so it is not human    
# readable but it is very fast to read and write
# numpy has it's own version of pickle, called .npy    
# and .npz
np.save('WriteFile.npy', Data)
X = np.load('Data/WriteFile.npy')
# npy is for single array, npz is for multiple arrays
Y = np.vstack((Data,Data))
np.savez('WriteFile.npz', X, Y)
X,Y = np.load('WriteFile.npz')
# %%
# 2) Plotting with Matplotlib
# Matplotlib is the most popular plotting library in Python
# Basic Plotting 
# PLot a cos function and a sin function from 0 to 2pi

# Plot a cos function and a sin function from 0 to 2pi
# Fill in
end=2*np.pi
x=np.arange(0,end,0.1)
y=np.sin(x)
#plt.plot(x,y)

# Change the color of the lines
# Fill in
#plt.plot(x,y,color='m')

# change the line style
# Fill in
plt.plot(x,y,color='b',linestyle='dashdot')
plt.show()


# %%

# Histogram
# Let's plot a histogram of random numbers
# For a uniform distribution
# Fill in
x = np.random.uniform(0,100,10000)
plt.hist(x)
plt.show()
# For a normal distribution
x = np.random.normal(0,100,10000)
# Fill in 
plt.hist(x)
plt.show()
# For an exponential distribution
x = np.random.exponential(10,10000)
# Fill in
plt.hist(x)
plt.show()

# %%
# 3-D Plotting
# We can also plot 3-D plots
ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)

zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# Plot a 3-D line
# Fill in
ax.plot3D(xline,yline,zline, 'red')
plt.show()

# Data for three-dimensional scattered points
# Fill in
ax1 = plt.axes(projection='3d')
ax1.scatter3D(xdata,ydata,zdata,c=zdata)
plt.show()

# Animation
from matplotlib.animation import FuncAnimation
# Make an animation of a particle moving in a circle
# Fill in 
plt.rcParams["figure.figsize"] = 4,3
r=1 #radius 
def circle(phi):
    return np.array([r*np.cos(phi),r*np.sin(phi)])
fig,ax2 = plt.subplots() #creating figure and axis
ax2.axis([-2,2,-2,2]) #axis limits 
point,=ax2.plot(0,1,marker='o')
def anim(phi):
    x, y = circle(phi)
    point.set_data([x],[y])
    return point,
ani = FuncAnimation(fig, anim, interval=10, blit=True, repeat=True, frames=np.linspace(0,2*np.pi,360, endpoint=False))
plt.show()
'''
# %%
# Read Images in Python
# Let's read 'Image1.png' in Python
# We will use the PIL library
# to install PIL, use the following command pip install pillow
from PIL import Image, ImageOps
# Fill in 
im=Image.open('Image1.png')
#im.show()

# PIL also has also image processing functions
# Let's convert the image to grayscale
# Fill in
im1=im.convert("L")
#im1.show()
im1.save('image_greyscale.png')

# There are many other functions, such as resize, rotate, crop, etc.
# You can convert the image to numpy array using np.array
# Fill in
img_np_array= np.array(im)
print(img_np_array)

# %%
# The opposite is also possible
# You can convert a numpy array to an image
# First load the Image2.txt file that I provided
# Then convert it to an image
# plot the image using plt.imshow 
# NOTE: The image is a grayscale image so
# you need to use cmap = 'Greys_r' option
# Then save it as a png file
# Fill in
img_array=np.loadtxt("Image2.txt",delimiter=',')
img_from_np_array= Image.fromarray(img_array)
img1= plt.imshow(img_from_np_array,cmap='Greys_r')
#plt.show()
plt.savefig('Image2.png')
# %%
