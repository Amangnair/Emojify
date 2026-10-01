# 🎭 Emojify — Real-Time Facial Expression to Emoji

A real-time deep learning desktop application that detects human facial expressions through a webcam and maps them to corresponding emoji avatars.

Built with **Python, OpenCV, TensorFlow/Keras, CustomTkinter, and Pillow**.

---

## 📌 Overview

Emojify combines **computer vision** and **deep learning** to recognize facial expressions in real time.

The application:

1. 📷 Captures frames from a webcam.
2. 🔍 Detects faces using OpenCV's Haar Cascade classifier.
3. 🖼️ Extracts and preprocesses the detected facial region as a **48×48 grayscale image**.
4. 🧠 Classifies the expression using a trained CNN model.
5. 🎭 Displays the corresponding emoji in the desktop dashboard.

The model recognizes **7 emotion classes**:

`Angry` · `Disgust` · `Fear` · `Happy` · `Neutral` · `Sad` · `Surprise`

---

## ✨ Features

* **Real-Time Face Detection** using OpenCV Haar Cascade.
* **7-Class Emotion Recognition** using a custom CNN.
* **Live Webcam Processing** with continuous emotion prediction.
* **Modern Desktop UI** built with CustomTkinter.
* **High-Resolution Emoji Assets** using 512×512 transparent PNG images.
* **Custom Emoji Generation** using Pillow.
* **Configurable Project Structure** with centralized paths, classes, and model settings.

---

## 📂 Project Structure

```text
Emojify/
├── data/
│   ├── train/                          # Training images by emotion class
│   └── test/                           # Test/validation images by emotion class
│
├── emojis/                             # Emoji image assets
│   ├── angry.png
│   ├── disgusted.png
│   ├── fearful.png
│   ├── happy.png
│   ├── neutral.png
│   ├── sad.png
│   └── surpriced.png
│
├── config.py                           # Paths, classes, and configuration
├── model.py                            # CNN model architecture
├── train.py                            # Model training pipeline
├── gui.py                              # Real-time desktop application
├── generate_512_emojis.py              # Emoji asset generator
├── haarcascade_frontalface_default.xml # OpenCV face detection cascade
├── model.weights.h5                    # Trained model weights
├── .gitignore
└── README.md
```

---

## 🧠 Model Architecture

The application uses a **Convolutional Neural Network (CNN)** trained on 48×48 grayscale facial images.

### Network

```text
Input: 48×48×1

Conv2D  32 filters  → ReLU
Conv2D  64 filters  → ReLU
MaxPooling
Dropout 0.25

Conv2D 128 filters  → ReLU
MaxPooling
Conv2D 128 filters  → ReLU
MaxPooling
Dropout 0.25

Flatten
Dense 1024          → ReLU
Dropout 0.5
Dense 7             → Softmax
```

### Training Configuration

| Setting             | Value                      |
| ------------------- | -------------------------- |
| Loss Function       | `categorical_crossentropy` |
| Optimizer           | Adam                       |
| Learning Rate       | `0.0001`                   |
| Input Size          | `48×48`                    |
| Image Format        | Grayscale                  |
| Output Classes      | 7                          |
| Pixel Normalization | `[0, 255] → [0.0, 1.0]`    |

---

## 💻 Prerequisites

Before running the project, make sure you have:

* Python **3.9–3.11**
* A working webcam
* Windows 10/11, macOS, or Linux
* Microsoft Visual C++ Redistributable 2015–2022 on Windows

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Emojify.git
cd Emojify
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it using the appropriate command.

**Windows — Command Prompt**

```bash
venv\Scripts\activate.bat
```

**Windows — PowerShell**

```bash
.\venv\Scripts\Activate.ps1
```

**macOS / Linux / Git Bash**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install tensorflow "opencv-python<5.0" customtkinter pillow
```

> 💡 OpenCV 4.x is recommended for compatibility with the Haar Cascade `CascadeClassifier` used by the application.

### 4. Add the Dataset

The project uses the FER2013 (Facial Expression Recognition 2013) dataset for training and testing the emotion recognition model.

The dataset is publicly available through Kaggle and contains 48×48 grayscale facial images across 7 emotion classes: Angry, Disgust, Fear, Happy, Neutral, Sad, and Surprise.

Download the FER2013 dataset from Kaggle: [FER-2013](https://www.kaggle.com/datasets/msambare/fer2013?utm_source=chatgpt.com)

The training dataset is **not included in the repository**.

After cloning the repository, create a `data` folder in the **project root directory** and place the dataset directories inside it.

The expected structure is:

```text
Emojify/
├── data/
│   ├── train/
│   │   ├── angry/
│   │   ├── disgust/
│   │   ├── fear/
│   │   ├── happy/
│   │   ├── neutral/
│   │   ├── sad/
│   │   └── surprise/
│   │
│   └── test/
│       ├── angry/
│       ├── disgust/
│       ├── fear/
│       ├── happy/
│       ├── neutral/
│       ├── sad/
│       └── surprise/
```

> 📁 Make sure the `train` and `test` directories are placed directly inside `data/`, and that each emotion has its own subdirectory containing the corresponding facial-expression images.

The directory names should match the emotion classes expected by the training configuration.

### 5. Generate Emoji Assets

Generate the high-resolution emoji PNG assets:

```bash
python generate_512_emojis.py
```

The generated images are saved in the `emojis/` directory.

### 6. Train the Model

Train the CNN using the images in the `data/` directory:

```bash
python train.py
```

After successful training, the trained weights are exported as:

```text
model.weights.h5
```

### 7. Run the Application

Launch the real-time desktop application:

```bash
python gui.py
```

Allow the application to access your webcam when prompted.

---

## 🎨 Emoji Assets

Emoji images are stored in the `emojis/` directory as transparent PNG files.

The project includes a Pillow-based generator:

```bash
python generate_512_emojis.py
```

The generator creates **512×512 RGBA PNG assets**, providing higher-quality images when displayed in the CustomTkinter interface.

Custom emoji images can also be used, provided their filenames match the mappings defined in `config.py`.

---

## 🔧 Troubleshooting

### `AttributeError: module 'cv2' has no attribute 'CascadeClassifier'`

This can occur when an incompatible or incomplete OpenCV package is installed.

Remove conflicting OpenCV packages:

```bash
pip uninstall opencv-python opencv-python-headless opencv-contrib-python -y
```

Then install OpenCV 4.x:

```bash
pip install "opencv-python<5.0"
```

### `model.weights.h5` Not Found

Run the training script first:

```bash
python train.py
```

The `model.weights.h5` file must be generated before launching the application.

### Emojis Appear Blurry

Regenerate the high-resolution assets:

```bash
python generate_512_emojis.py
```

Make sure the generated PNG files are present in the `emojis/` directory.

---

## 📸 GitHub Showcase

For a better project showcase, the repository can include screenshots or a short demonstration GIF showing:

* Live webcam feed
* Face detection
* Detected emotion
* Corresponding emoji
* Application dashboard

If screenshots contain webcam footage, avoid publishing identifiable personal images without consent. A non-identifying demonstration source can be used instead.

---

## 🛠️ Tech Stack

| Category         | Technology                    |
| ---------------- | ----------------------------- |
| Language         | Python                        |
| GUI              | CustomTkinter / Tkinter       |
| Computer Vision  | OpenCV                        |
| Deep Learning    | TensorFlow / Keras            |
| Image Processing | Pillow (PIL)                  |
| Model            | Convolutional Neural Network  |
| Face Detection   | Haar Cascade                  |
| Input            | Webcam                        |
| Data             | Grayscale 48×48 facial images |

---

## 📌 Project Status

**Beta / Development**

The core functionality is implemented, including model training, real-time face detection, emotion classification, and emoji mapping.

The UI and visual design can be further refined in future iterations.
