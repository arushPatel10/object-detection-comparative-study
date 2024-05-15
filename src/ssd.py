# src/ssd.py

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Conv2D, Activation, Reshape
from tensorflow.keras.models import Model

def build_ssd(input_shape=(300, 300, 3), num_classes=21):
    base_model = VGG16(input_shape=input_shape, include_top=False)
    
    x = base_model.output
    x = Conv2D(1024, (3, 3), padding='same')(x)
    x = Activation('relu')(x)
    x = Conv2D(num_classes, (1, 1))(x)
    x = Reshape((-1, num_classes))(x)
    x = Activation('softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=x)
    return model

if __name__ == "__main__":
    ssd_model = build_ssd()
    ssd_model.summary()
