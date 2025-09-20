import tensorflow as tf
from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.callbacks import EarlyStopping
from keras._tf_keras.keras.applications import MobileNetV2
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import GlobalAveragePooling2D, Dense, Dropout, BatchNormalization
from keras._tf_keras.keras.regularizers import l2
import matplotlib.pyplot as plt  

train_path = 'dataset/train'
valid_path = 'dataset/valid'

train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=90,
    width_shift_range=0.5,
    height_shift_range=0.5,
    shear_range=0.5,
    zoom_range=0.5,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1.0/255.0)

train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary'
)

validation_generator = val_datagen.flow_from_directory(
    valid_path,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary'
)

base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
base_model.trainable = True
for layer in base_model.layers[:-30]:  
    layer.trainable = False


model = Sequential([
    base_model,
    GlobalAveragePooling2D(), 
    Dense(128, activation='relu', kernel_regularizer=l2(0.02)),  
    Dropout(0.5), 
    Dense(1, activation='sigmoid')  
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

class_weights = {0: 1.0, 1: 1.0}
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=100,
    batch_size=20,
    callbacks=[early_stopping]
)

model.save('parkinson_model.h5')

# Plot accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plot loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()