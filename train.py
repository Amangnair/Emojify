import cv2
from keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import config
from model import build_emotion_model

# Image preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    config.TRAIN_DIR,
    target_size=config.IMAGE_SIZE,
    batch_size=config.BATCH_SIZE,
    color_mode="grayscale",
    class_mode='categorical'
)

validation_generator = val_datagen.flow_from_directory(
    config.VAL_DIR,
    target_size=config.IMAGE_SIZE,
    batch_size=config.BATCH_SIZE,
    color_mode="grayscale",
    class_mode='categorical'
)

# Model setup
cv2.ocl.setUseOpenCL(False)
model = build_emotion_model()
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(learning_rate=config.LEARNING_RATE, decay=config.DECAY),
    metrics=['accuracy']
)

# Training execution (dynamic generator step sizing)
model_info = model.fit(
    train_generator,
    epochs=config.EPOCHS,
    validation_data=validation_generator
)

# Save weights
model.save_weights(config.MODEL_WEIGHTS_PATH)
print(f"Model training complete. Weights saved to {config.MODEL_WEIGHTS_PATH}")