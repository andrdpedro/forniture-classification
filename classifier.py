import numpy as np
import tensorflow as tf


class Classifier:
    def __init__(self, model, image_path, class_names):
        self.model = model
        self.image_path = image_path
        self.class_names = class_names
        self.img_height = 180
        self.img_width = 180
        self.image = None
        self.score = None
        self.classified_class = None

    def classifie_image(self):
        self.load_image()
        self.make_classification()

    def load_image(self):
        self.image = tf.keras.utils.load_img(
        self.image_path,
        target_size=(self.img_height, self.img_width)
        )
    
    def make_classification(self):
        img_array = tf.keras.utils.img_to_array(self.image)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        self.classified_class = self.class_names[np.argmax(score)]
        self.score = round(100 * np.max(score), 2)

        classification = f"This image most likely belongs to {self.classified_class} with a {self.score} percent confidence."
        print(classification)
        