import os
import cv2
import numpy as np
from PIL import Image, ImageTk
import customtkinter as ctk

import config
from model import build_emotion_model

# Appearance & Theme Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class EmotionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Emojify — Real-time Emotion Recognition")
        self.geometry("1100x680")
        self.resizable(False, False)

        # AI Model & Cascade Loader
        self.emotion_model = build_emotion_model()
        if os.path.exists(config.MODEL_WEIGHTS_PATH):
            self.emotion_model.load_weights(config.MODEL_WEIGHTS_PATH)
            print(f"Loaded weights from {config.MODEL_WEIGHTS_PATH}")
        else:
            print(f"Warning: '{config.MODEL_WEIGHTS_PATH}' not found. Ensure trained weights exist.")

        self.bounding_box = config.get_haar_cascade()
        cv2.ocl.setUseOpenCL(False)

        # Video Stream Initialization
        self.cap = cv2.VideoCapture(0)
        self.current_emotion_index = 4  # Default Neutral

        # Build Modern Interface
        self._build_ui()

        # Protocol & Loops
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.update_webcam()
        self.update_emoji()

    def _build_ui(self):
        # 1. Header Navigation Bar
        self.header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1A1A1A", height=70)
        self.header_frame.pack(side="top", fill="x")

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="EMOJIFY", 
            font=ctk.CTkFont(family="Inter", size=24, weight="bold"),
            text_color="#3B82F6"
        )
        self.title_label.pack(side="left", padx=25, pady=15)

        self.subtitle_label = ctk.CTkLabel(
            self.header_frame, 
            text="Real-time Facial Emotion Expression Generator", 
            font=ctk.CTkFont(size=13),
            text_color="#9CA3AF"
        )
        self.subtitle_label.pack(side="left", padx=0, pady=15)

        self.btn_quit = ctk.CTkButton(
            self.header_frame, 
            text="Exit App", 
            width=100,
            fg_color="#EF4444", 
            hover_color="#DC2626",
            command=self.on_close
        )
        self.btn_quit.pack(side="right", padx=25)

        # 2. Main Content Grid Dashboard
        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_container.pack(side="top", fill="both", expand=True, padx=25, pady=20)
        self.grid_container.grid_columnconfigure((0, 1), weight=1, uniform="group1")
        self.grid_container.grid_rowconfigure(0, weight=1)

        # Left Card: Live Camera Feed
        self.cam_card = ctk.CTkFrame(self.grid_container, corner_radius=12, fg_color="#242424")
        self.cam_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.cam_title = ctk.CTkLabel(
            self.cam_card, 
            text="LIVE VIDEO FEED", 
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#9CA3AF"
        )
        self.cam_title.pack(anchor="nw", padx=15, pady=(15, 5))

        self.lbl_webcam = ctk.CTkLabel(self.cam_card, text="", corner_radius=8)
        self.lbl_webcam.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        # Right Card: Detected Emoji & Output
        self.emoji_card = ctk.CTkFrame(self.grid_container, corner_radius=12, fg_color="#242424")
        self.emoji_card.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.emoji_title = ctk.CTkLabel(
            self.emoji_card, 
            text="EXPRESSION MATCH", 
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#9CA3AF"
        )
        self.emoji_title.pack(anchor="nw", padx=15, pady=(15, 5))

        self.lbl_emoji = ctk.CTkLabel(self.emoji_card, text="")
        self.lbl_emoji.pack(expand=True, pady=(10, 0))

        self.lbl_emotion_text = ctk.CTkLabel(
            self.emoji_card, 
            text="NEUTRAL", 
            font=ctk.CTkFont(family="Inter", size=28, weight="bold"),
            text_color="#3B82F6"
        )
        self.lbl_emotion_text.pack(pady=(0, 30))

        # 3. Footer / Status Bar
        self.status_bar = ctk.CTkFrame(self, corner_radius=0, height=30, fg_color="#18181B")
        self.status_bar.pack(side="bottom", fill="x")

        self.lbl_status = ctk.CTkLabel(
            self.status_bar, 
            text="● System Active — Hardware Stream Connected", 
            font=ctk.CTkFont(size=11),
            text_color="#10B981"
        )
        self.lbl_status.pack(side="left", padx=15, pady=4)

    def update_webcam(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (480, 360))
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.bounding_box.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (59, 130, 246), 2)
                roi_gray = gray_frame[y:y + h, x:x + w]

                cropped_img = cv2.resize(roi_gray, config.IMAGE_SIZE)
                cropped_img = np.expand_dims(np.expand_dims(cropped_img, -1), 0) / 255.0

                prediction = self.emotion_model.predict(cropped_img, verbose=0)
                self.current_emotion_index = int(np.argmax(prediction))

                cv2.putText(
                    frame, config.EMOTION_DICT[self.current_emotion_index], 
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (59, 130, 246), 2
                )

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgtk = ctk.CTkImage(light_image=img, dark_image=img, size=(480, 360))
            self.lbl_webcam.configure(image=imgtk)

        self.after(10, self.update_webcam)

    def update_emoji(self):
        emoji_path = config.EMOJI_DIST.get(self.current_emotion_index)
        if emoji_path and os.path.exists(emoji_path):
            frame2 = cv2.imread(emoji_path)
            if frame2 is not None:
                frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                img2 = Image.fromarray(frame2)
                imgtk2 = ctk.CTkImage(light_image=img2, dark_image=img2, size=(220, 220))
                self.lbl_emoji.configure(image=imgtk2)

        emotion_name = config.EMOTION_DICT.get(self.current_emotion_index, "NEUTRAL").upper()
        self.lbl_emotion_text.configure(text=emotion_name)
        self.after(100, self.update_emoji)

    def on_close(self):
        if self.cap.isOpened():
            self.cap.release()
        self.destroy()

if __name__ == '__main__':
    app = EmotionApp()
    app.mainloop()