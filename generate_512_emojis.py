import os
import math
from PIL import Image, ImageDraw

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMOJI_DIR = os.path.join(BASE_DIR, 'emojis')

def draw_base_face(draw):
    """Draws a smooth 512x512 yellow gradient face with antialiasing."""
    # Outer base circle
    draw.ellipse([16, 16, 496, 496], fill=(255, 204, 0, 255), outline=(230, 160, 0, 255), width=8)

def draw_eye(draw, cx, cy, rx=24, ry=32, fill=(40, 40, 40, 255)):
    """Draws an eye."""
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fill)

def create_angry(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # Slanted Angry Eyebrows
    draw.line([120, 150, 220, 200], fill=(40, 40, 40, 255), width=20)
    draw.line([392, 150, 292, 200], fill=(40, 40, 40, 255), width=20)
    
    # Eyes
    draw_eye(draw, 170, 230, 22, 22)
    draw_eye(draw, 342, 230, 22, 22)
    
    # Downward Frown Mouth
    draw.arc([170, 320, 342, 420], start=200, end=340, fill=(40, 40, 40, 255), width=18)
    img.save(path, 'PNG')

def create_disgusted(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([16, 16, 496, 496], fill=(138, 195, 74, 255), outline=(100, 150, 50, 255), width=8) # Sickly greenish
    
    # Squinting Eyes
    draw.line([130, 210, 210, 230], fill=(40, 40, 40, 255), width=16)
    draw.line([130, 230, 210, 210], fill=(40, 40, 40, 255), width=16)
    
    draw.line([302, 210, 382, 230], fill=(40, 40, 40, 255), width=16)
    draw.line([302, 230, 382, 210], fill=(40, 40, 40, 255), width=16)
    
    # Wavy Disgusted Mouth
    points = [(160, 360), (220, 330), (290, 380), (350, 340)]
    draw.line(points, fill=(40, 40, 40, 255), width=16, joint="curve")
    img.save(path, 'PNG')

def create_fearful(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # Raised Eyebrows
    draw.arc([120, 120, 220, 180], start=200, end=340, fill=(40, 40, 40, 255), width=14)
    draw.arc([292, 120, 392, 180], start=200, end=340, fill=(40, 40, 40, 255), width=14)
    
    # Wide Shocked Eyes
    draw_eye(draw, 170, 220, 32, 40)
    draw_eye(draw, 342, 220, 32, 40)
    
    # Open Worried Mouth
    draw.ellipse([216, 310, 296, 410], fill=(40, 40, 40, 255))
    img.save(path, 'PNG')

def create_happy(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # Smiling Curved Eyes
    draw.arc([130, 180, 210, 250], start=200, end=340, fill=(40, 40, 40, 255), width=16)
    draw.arc([302, 180, 382, 250], start=200, end=340, fill=(40, 40, 40, 255), width=16)
    
    # Big Open Smile
    draw.chord([150, 250, 362, 420], start=0, end=180, fill=(40, 40, 40, 255))
    draw.chord([180, 340, 332, 420], start=0, end=180, fill=(235, 87, 87, 255)) # Tongue
    img.save(path, 'PNG')

def create_neutral(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # Normal Eyes
    draw_eye(draw, 170, 220, 24, 24)
    draw_eye(draw, 342, 220, 24, 24)
    
    # Straight Line Mouth
    draw.line([170, 350, 342, 350], fill=(40, 40, 40, 255), width=18)
    img.save(path, 'PNG')

def create_sad(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # Sad Eyebrows
    draw.line([120, 180, 210, 150], fill=(40, 40, 40, 255), width=14)
    draw.line([392, 180, 302, 150], fill=(40, 40, 40, 255), width=14)
    
    # Eyes
    draw_eye(draw, 170, 230, 22, 22)
    draw_eye(draw, 342, 230, 22, 22)
    
    # Sad Frown
    draw.arc([170, 320, 342, 440], start=200, end=340, fill=(40, 40, 40, 255), width=18)
    
    # Tear Drop
    draw.ellipse([350, 270, 370, 310], fill=(86, 204, 242, 255))
    img.save(path, 'PNG')

def create_surprised(path):
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_base_face(draw)
    
    # High Eyebrows
    draw.arc([130, 110, 210, 160], start=200, end=340, fill=(40, 40, 40, 255), width=14)
    draw.arc([302, 110, 382, 160], start=200, end=340, fill=(40, 40, 40, 255), width=14)
    
    # Wide Round Eyes
    draw_eye(draw, 170, 210, 30, 30)
    draw_eye(draw, 342, 210, 30, 30)
    
    # Open 'O' Mouth
    draw.ellipse([216, 290, 296, 410], fill=(40, 40, 40, 255))
    img.save(path, 'PNG')

def generate_all():
    os.makedirs(EMOJI_DIR, exist_ok=True)
    
    generators = {
        "angry.png": create_angry,
        "disgusted.png": create_disgusted,
        "fearful.png": create_fearful,
        "happy.png": create_happy,
        "neutral.png": create_neutral,
        "sad.png": create_sad,
        "surpriced.png": create_surprised  # Matches project key name[cite: 1]
    }
    
    for filename, func in generators.items():
        file_path = os.path.join(EMOJI_DIR, filename)
        func(file_path)
        print(f"Generated 512x512 transparent PNG: {filename}")

if __name__ == "__main__":
    generate_all()