# -*- coding: utf-8 -*-
"""MNIST Data-CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TmroHaSWQtr3AOhN_d4QgcdhXYnb3Fbf
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing all the necessary libraries


#Loading the mnist dataset from keras library 
#The mnist dataset contains grayscaled handwritten single digits from 0-9
from keras.datasets import mnist 
# from mnist.loader import MNIST

import matplotlib.pyplot as plt #For visualizing the hand-written images
# %matplotlib inline

from keras.utils.np_utils import to_categorical  #To convert y_labels to one-hot encoding
from keras.models import Sequential #To build the neural network
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten #To add dense and convolutional layers
from sklearn.metrics import classification_report #To know how good the model is

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt #For visualizing the hand-written images
# %matplotlib inline

"""Scalar = 3 (A number)


Vectors = [1,2,3] (A list of numbers)


Matrix = [[1,2],[3,4]] (A list of vectors)


Tensor = [

  [[1,2],[3,4]],

  [[1,2],[3,4]],

  [[1,2],[3,4]]

  ]

  Tensors are nD array of numbers
"""

#Dividing the dataset into trainig and testing 
#We can think of the entitre training dataset as a 4D np array or a tensor(No.of.images(Samples),length of an image(x),Width of an image(y),color-channel)
(X_train,y_train),(x_test,y_test) = mnist.load_data()

X_train.shape

x_test.shape

"""y_test.shape"""

plt.imshow(X_train[0],cmap = 'gray_r') #To get the inverse (gray_reverse)

#Converting the label to categorical one-hot encoding
y_cat_test = to_categorical(y_test,10)
y_cat_train = to_categorical(y_train,10)

y_cat_test.shape

#Processing the X_data or the featured data
print(X_train[0].max())
print(x_test[0].max())
#Standardizing the X_data(Normalizing)
X_train = X_train/X_train.max()
x_test = x_test/x_test.max()

print(x_test[0].max())
print(X_train[0].max())

X_train = X_train.reshape((60000, 28, 28,1))
X_train.shape

x_test = x_test.reshape((10000, 28, 28,1))
x_test.shape

#Building the neural network
model = Sequential()

#Convolutional layer
model.add(Conv2D(filters = 64,kernel_size = (4,4),input_shape = (28, 28, 1),activation='relu',))

#Pooling layer
model.add(MaxPool2D(pool_size = (3,3)))

#Flattening 2D image --> 1D image
model.add(Flatten())

#Now,adding the Dense layers
model.add(Dense(256,activation = 'relu'))

#Output layer
model.add(Dense(10,activation = 'softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.summary()

model.fit(X_train,y_cat_train,epochs = 2)

#Evaluating the model 
model.metrics_names

model.evaluate(x_test,y_cat_test)

predictions = model.predict_classes(x_test)

print(classification_report(y_test,predictions))