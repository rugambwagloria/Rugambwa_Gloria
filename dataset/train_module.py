import os
import numpy as np# type: ignore
import tensorflow as tf # type: ignore building and training deep leaarning model
import tensorflow import keras #type:ignore -High level API for neural networks
from tensorflow.keras import layers, models # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore -Augmentation
from tensorflow.keras.modules import sequential # type: ignore # ignore #Linear stack of neural network layers
from  tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Droout # type: ignore Layer CNN
from tensorflow.keras.optimizers import Adam # type: ignore Optimizer for training
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping # type: ignore Callbacks for training
import matplotlib.pyplot as plt # type: ignore # for plotting training history line graphs

#set random seeds for reproducibility
tf.random.set_seed(42)
np .random.seed(42)

#define the constant value
IMAGE_SIZE=(256,256)  #inpput image size
BATCH_SIZE=32  #number of images process in a batch
EPOCHS=20  #number of full passes for training
NUM_CLASSES=2#number of output classes for crops(diseases, healthy)
ANIMAL_CLASSES = 3#Number of animal classes (cats, dogs, human)

#define the dataset director and the model save paths
DATASET_DIR = 'LEARN_ML'  # Directory containing training
MODEL_PATH= 'model.h5'  # Path to save the trained model


