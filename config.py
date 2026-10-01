import os
import cv2

# Base Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Asset & Data Paths
EMOJI_DIR = os.path.join(BASE_DIR, 'emojis')
TRAIN_DIR = os.path.join(BASE_DIR, 'data', 'train')
VAL_DIR = os.path.join(BASE_DIR, 'data', 'test')
MODEL_WEIGHTS_PATH = os.path.join(BASE_DIR, 'model.weights.h5')
LOGO_PATH = os.path.join(BASE_DIR, 'logo.png')

# Model & Image Configurations
IMAGE_SIZE = (48, 48)
INPUT_SHAPE = (48, 48, 1)
BATCH_SIZE = 64
EPOCHS = 50
LEARNING_RATE = 0.0001
DECAY = 1e-6

# Emotion Class Mapping (Alphabetical order matching subfolders)
EMOTION_DICT = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprise"
}

# Emoji Image Asset Mapping
EMOJI_DIST = {
    0: os.path.join(EMOJI_DIR, "angry.png"),
    1: os.path.join(EMOJI_DIR, "disgusted.png"),
    2: os.path.join(EMOJI_DIR, "fearful.png"),
    3: os.path.join(EMOJI_DIR, "happy.png"),
    4: os.path.join(EMOJI_DIR, "neutral.png"),
    5: os.path.join(EMOJI_DIR, "sad.png"),
    6: os.path.join(EMOJI_DIR, "surpriced.png")
}

def get_haar_cascade():
    """Returns the OpenCV default frontal face Haar Cascade classifier dynamically."""
    cascade_path = getattr(cv2, 'data', None)
    if cascade_path and hasattr(cascade_path, 'haarcascades'):
        xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    else:
        xml_path = os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml')
        
    cascade = cv2.CascadeClassifier(xml_path)
    if cascade.empty():
        print(f"Warning: Failed to load Haar Cascade from {xml_path}")
    return cascade