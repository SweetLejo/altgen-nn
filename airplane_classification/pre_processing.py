import numpy as np
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K
from tensorflow.keras.saving import register_keras_serializable
import tensorflow as tf


@tf.keras.utils.register_keras_serializable()
class StochasticDepth(tf.keras.layers.Layer):
    def __init__(self, drop_prob=0.2, **kwargs):
        super().__init__(**kwargs)
        self.drop_prob = drop_prob

    def call(self, inputs, training=None):
        if training:
            keep_prob = 1.0 - self.drop_prob
            batch_size = tf.shape(inputs)[0]
            random_tensor = keep_prob + tf.random.uniform([batch_size, 1, 1, 1], dtype=inputs.dtype)
            binary_tensor = tf.floor(random_tensor)  # Convert to 0 or 1
            return inputs * binary_tensor / keep_prob  # Scale for variance correction
        return inputs
    


def preprocess_image(image_path :str):
    """
    Preprocess an image to match the input format of the neural network.
    Args:
        image_path (str): Path to the image file.
    Returns:
        np.ndarray: Preprocessed image with shape (1, height, width, channels).
    """
    # Load the image

    img_size = (448,448)

    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)  # Ensure 3 color channels (RGB)

    # Resize the image to the expected size
    img = tf.image.resize(img, img_size)

    # Normalize pixel values to [0, 1]
    img = img / 255.0

    # Add a batch dimension (for a single image)
    img = tf.expand_dims(img, axis=0)

    return img.numpy()







