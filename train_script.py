# MIT License
#
# Copyright (c) 2020 Leandro Handal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



from matplotlib import pyplot as plt
from random import shuffle
import os
from PIL import Image
import numpy as np
from numpy import loadtxt
from keras.models import load_model
import glob
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D, Conv2D, BatchNormalization


path = ""   # Path of training pictures
            # Rename the likes as "yay_" and dislikes as "nay_" for training

def label_img(name):
    word_label = name.split('_')[0]
    if word_label == 'yay' : return np.array([1])
    elif word_label == 'nay' : return np.array([0])


IMG_SIZE = 300
def load_data(DIR):
    train_data = []
    print(f'Loading {len(glob.glob1(DIR,"*.jpg"))} images...')
    for img in (os.listdir(DIR)):
        try:
            label = label_img(img)
            path = os.path.join(DIR, img)
            img = Image.open(path)
            img = img.convert('L')
            img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
            train_data.append([np.array(img), label])

        except:
            pass
    shuffle(train_data)
    return train_data

data = load_data(path)

train = data[:int(round(len(data)*.8,0))]
test = data[int(round(len(data)*.8,0)):]

trainImages = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
trainLabels = np.array([i[1] for i in train])

testImages = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
testLabels = np.array([i[1] for i in test])

model = Sequential()
model.add(Convolution2D(32, kernel_size = (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Convolution2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Convolution2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Convolution2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Convolution2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation = 'sigmoid'))

# model = load_model('/Users/leandro.handal/Documents/Fun_Projects/tinder_bot/model_02.h5')

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics = ['accuracy'])

model.fit(trainImages, trainLabels, batch_size=50, epochs=20, verbose=1)
loss, acc = model.evaluate(testImages, testLabels, verbose = 0)
print(f"Test Accuracy: {round(acc * 100,2)}%")

model.save("model_05.h5")
print("Saved model to disk")


