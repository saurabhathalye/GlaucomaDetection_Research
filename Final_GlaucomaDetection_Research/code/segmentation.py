
import tensorflow as tf
from tensorflow.keras import layers, Model

def build_unet(input_shape):
    inputs = layers.Input(input_shape)
    conv1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    pool1 = layers.MaxPooling2D((2, 2))(conv1)
    up1 = layers.Conv2DTranspose(64, (3, 3), activation='relu', padding='same')(pool1)
    outputs = layers.Conv2D(1, (1, 1), activation='sigmoid')(up1)
    return Model(inputs, outputs)

if __name__ == "__main__":
    unet_model = build_unet((256, 256, 3))
    unet_model.summary()
