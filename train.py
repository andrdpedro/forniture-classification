import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


class Training:
    def __init__(self):
        self.dataset = "Data"
        self.batch_size = 32
        self.img_height = 180
        self.img_width = 180
        self.train_data = None
        self.val_data = None
        self.class_names = None
        self.model = None

        self.start_training()

    def start_training(self):
        self.load_dataset()
        self.create_model()
        self.compile_model()
        self.train_model()

    def load_dataset(self):
        self.train_data, self.val_data = tf.keras.utils.image_dataset_from_directory(
            self.dataset,
            validation_split=0.2,
            subset="both",
            seed=42,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size
        )
        self.class_names = self.train_data.class_names

    def create_model(self):
        data_augmentation = keras.Sequential(
            [
                layers.RandomFlip(
                    "horizontal",
                    input_shape=(
                        self.img_height,
                        self.img_width,
                        3
                    )
                ),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
            ]
        )

        AUTOTUNE = tf.data.AUTOTUNE
        self.train_data = self.train_data.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        self.val_data = self.val_data.cache().prefetch(buffer_size=AUTOTUNE)

        num_classes = len(self.class_names)
        self.model = Sequential([
            data_augmentation,
            layers.Rescaling(1./255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes, name="outputs")
        ])

    def compile_model(self):
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy']
        )

    def train_model(self):
        epochs = 10
        self.model.fit(
            self.train_data,
            validation_data=self.val_data,
            epochs=epochs
        )
