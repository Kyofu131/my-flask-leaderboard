from operator import truediv
import pygame
import random
import os
import tkinter as tk
from tkinter import filedialog
import requests
import json
import portalocker

def lock_file(file_path):
    with open(file_path, 'r+') as file:
        portalocker.lock(file, portalocker.LOCK_EX)
        # Perform file operations
        portalocker.unlock(file)


# Initialize Pygame
pygame.init()

# Set up the font
font = pygame.font.Font(None, 36)  # You can adjust the size as needed

# Screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TANK COMMANDER: TACTICAL NEMESIS")
clock = pygame.time.Clock()

# Get the absolute path of the directory where the script is located
base_path = os.path.dirname(os.path.abspath(__file__))

# Define paths using relative paths
ASSET_PATH = os.path.join(base_path, "Assets")
FONT_PATH = os.path.join(ASSET_PATH, "Font")
PNG_PATH = os.path.join(ASSET_PATH, "PNG", "Yellow", "Double")

# Load the images and font
button_image = pygame.image.load(os.path.join(PNG_PATH, 'button_square_depth_line.png')).convert_alpha()
button_image = pygame.transform.scale(button_image, (100, 100))  # Resize if necessary
kenney_font_36 = pygame.font.Font(os.path.join(FONT_PATH, 'Kenney Future.ttf'), 36)
kenney_font_48 = pygame.font.Font(os.path.join(FONT_PATH, 'Kenney Future.ttf'), 48)
kenney_font_72 = pygame.font.Font(os.path.join(FONT_PATH, 'Kenney Future.ttf'), 72)

# Load, resize, and rotate the images
normal_front_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_dark_gray_red.png')).convert_alpha()
normal_behind_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_dark_gray_red (1).png')).convert_alpha()
normal_front_image = pygame.transform.scale(normal_front_image, (110, 60))
normal_behind_image = pygame.transform.scale(normal_behind_image, (120, 70))

fast_front_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_navy_blue_white.png')).convert_alpha()
fast_behind_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_navy_blue_white (1).png')).convert_alpha()
fast_front_image = pygame.transform.scale(fast_front_image, (110, 60))
fast_behind_image = pygame.transform.scale(fast_behind_image, (120, 70))

tanky_front_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_brown_beige.png')).convert_alpha()
tanky_behind_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'Helicopter_brown_beige (1).png')).convert_alpha()
tanky_front_image = pygame.transform.scale(tanky_front_image, (110, 60))
tanky_behind_image = pygame.transform.scale(tanky_behind_image, (120, 70))

# Load and resize the kamikaze enemy image
kamikaze_image = pygame.image.load(os.path.join(ASSET_PATH, 'helicopter', 'plane_2_yellow.png')).convert_alpha()
kamikaze_image = pygame.transform.scale(kamikaze_image, (110, 60))

# Load and resize background images in the correct order
background_images = {
    "city1plan": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'city1plan.png')).convert_alpha(), (screen_width, screen_height)),
    "light": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'light.png')).convert_alpha(), (screen_width, screen_height)),
    "smog1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'smog1.png')).convert_alpha(), (screen_width, screen_height)),
    "smog2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'smog2.png')).convert_alpha(), (screen_width, screen_height)),
    "city2plan": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'city2plan.png')).convert_alpha(), (screen_width, screen_height)),
    "city3plan": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'city3plan.png')).convert_alpha(), (screen_width, screen_height)),
    "city4plan": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'city4plan.png')).convert_alpha(), (screen_width, screen_height)),
    "sun": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'sun.png')).convert_alpha(), (300, 300)),  # Adjust size as needed
    "background": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'Backgroundlvl', 'background.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 2
level_2_background_images = {
    "a1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 1', 'a1.png')).convert_alpha(), (screen_width, screen_height)),
    "a2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 1', 'a2.png')).convert_alpha(), (screen_width, screen_height)),
    "a3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 1', 'a3.png')).convert_alpha(), (screen_width, screen_height)),
    "a4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 1', 'a4.png')).convert_alpha(), (screen_width, screen_height)),
    "a5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 1', 'a5.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 3
level_3_background_images = {
    "b1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b1.png')).convert_alpha(), (screen_width, screen_height)),
    "b2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b2.png')).convert_alpha(), (screen_width, screen_height)),
    "b3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b3.png')).convert_alpha(), (screen_width, screen_height)),
    "b4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b4.png')).convert_alpha(), (screen_width, screen_height)),
    "b5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b5.png')).convert_alpha(), (screen_width, screen_height)),
    "b6": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 2', 'b6.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 4
level_4_background_images = {
    "c1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 3', 'c1.png')).convert_alpha(), (screen_width, screen_height)),
    "c2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 3', 'c2.png')).convert_alpha(), (screen_width, screen_height)),
    "c3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 3', 'c3.png')).convert_alpha(), (screen_width, screen_height)),
    "c4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 3', 'c4.png')).convert_alpha(), (screen_width, screen_height)),
    "c5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 3', 'c5.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 5
level_5_background_images = {
    "d1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 4', 'd1.png')).convert_alpha(), (screen_width, screen_height)),
    "d2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 4', 'd2.png')).convert_alpha(), (screen_width, screen_height)),
    "d3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 4', 'd3.png')).convert_alpha(), (screen_width, screen_height)),
    "d4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 4', 'd4.png')).convert_alpha(), (screen_width, screen_height)),
    "d5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 4', 'd5.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 6
level_6_background_images = {
    "e1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 5', 'e1.png')).convert_alpha(), (screen_width, screen_height)),
    "e2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 5', 'e2.png')).convert_alpha(), (screen_width, screen_height)),
    "e3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 5', 'e3.png')).convert_alpha(), (screen_width, screen_height)),
    "e4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 5', 'e4.png')).convert_alpha(), (screen_width, screen_height)),
    "e5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 5', 'e5.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 7
level_7_background_images = {
    "f1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f1.png')).convert_alpha(), (screen_width, screen_height)),
    "f2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f2.png')).convert_alpha(), (screen_width, screen_height)),
    "f3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f3.png')).convert_alpha(), (screen_width, screen_height)),
    "f4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f4.png')).convert_alpha(), (screen_width, screen_height)),
    "f5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f5.png')).convert_alpha(), (screen_width, screen_height)),
    "f6": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 6', 'f6.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 8
level_8_background_images = {
    "g1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 7', 'g1.png')).convert_alpha(), (screen_width, screen_height)),
    "g2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 7', 'g2.png')).convert_alpha(), (screen_width, screen_height)),
    "g3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 7', 'g3.png')).convert_alpha(), (screen_width, screen_height)),
    "g4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 7', 'g4.png')).convert_alpha(), (screen_width, screen_height)),
    "g5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 7', 'g5.png')).convert_alpha(), (screen_width, screen_height))
}

# Load and resize the images for level 9
level_9_background_images = {
    "h1": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 8', 'h1.png')).convert_alpha(), (screen_width, screen_height)),
    "h2": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 8', 'h2.png')).convert_alpha(), (screen_width, screen_height)),
    "h3": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 8', 'h3.png')).convert_alpha(), (screen_width, screen_height)),
    "h4": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 8', 'h4.png')).convert_alpha(), (screen_width, screen_height)),
    "h5": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'Assets', 'city 8', 'h5.png')).convert_alpha(), (screen_width, screen_height))
}

# Define initial positions for background layers including level 2 images
background_positions = {
    "background": 0,
    "sun": 0,
    "city4plan": 0,
    "city3plan": 0,
    "city2plan": 0,
    "smog2": 0,
    "smog1": 0,
    "light": 0,
    "city1plan": 0,
    "a1": 0,  # Add these lines
    "a2": 0,
    "a3": 0,
    "a4": 0,
    "a5": 0,
    "b1": 0,
    "b2": 0,
    "b3": 0,
    "b4": 0,
    "b5": 0,
    "b6": 0,
    "c1": 0,
    "c2": 0,
    "c3": 0,
    "c4": 0,
    "c5": 0,
    "d1": 0,
    "d2": 0,
    "d3": 0,
    "d4": 0,
    "d5": 0,
    "e1": 0,
    "e2": 0,
    "e3": 0,
    "e4": 0,
    "e5": 0,
    "f1": 0,
    "f2": 0,
    "f3": 0,
    "f4": 0,
    "f5": 0,
    "f6": 0,
    "g1": 0,
    "g2": 0,
    "g3": 0,
    "g4": 0,
    "g5": 0,
    "h1": 0,
    "h2": 0,
    "h3": 0,
    "h4": 0,
    "h5": 0
}

# Original speeds: { "background": 1, "sun": 2, "city4plan": 3, "city3plan": 4, "city2plan": 5, "smog2": 6, "smog1": 7, "light": 8, "city1plan": 9 }
background_speeds = {
    "background": 0.5,
    "sun": 1,
    "city4plan": 1.5,
    "city3plan": 2,
    "city2plan": 2.5,
    "smog2": 3,
    "smog1": 3.5,
    "light": 4,
    "city1plan": 4.5,
    "a1": 2,
    "a2": 2.5,
    "a3": 3,
    "a4": 3.5,
    "a5": 4,
    "b1": 2,
    "b2": 2.5,
    "b3": 3,
    "b4": 3.5,
    "b5": 4,
    "b6": 4.5,
    "c1": 2,
    "c2": 2.5,
    "c3": 3,
    "c4": 3.5,
    "c5": 4,
    "d1": 2,
    "d2": 2.5,
    "d3": 3,
    "d4": 3.5,
    "d5": 4,
    "e1": 2,
    "e2": 2.5,
    "e3": 3,
    "e4": 3.5,
    "e5": 4,
    "f1": 2,
    "f2": 2.5,
    "f3": 3,
    "f4": 3.5,
    "f5": 4,
    "f6": 4.5,
    "g1": 2,
    "g2": 2.5,
    "g3": 3,
    "g4": 3.5,
    "g5": 4,
    "h1": 2,
    "h2": 2.5,
    "h3": 3,
    "h4": 3.5,
    "h5": 4
}

# Define the path to assets
ASSET_PATH = os.path.join(base_path, "Assets")
PNG_PATH = os.path.join(ASSET_PATH, "PNG", "Yellow", "Default")
TANK_PATH = os.path.join(ASSET_PATH, "tankPNG", "Retina")
BULLET_PATH = os.path.join(ASSET_PATH, "tankPNG", "Default size")
BACKGROUND_PATH = os.path.join(ASSET_PATH, "Backgroundlvl")

# Increase the width of the button rectangle image for the level select screen
select_level_width = kenney_font_48.size("Select Level")[0] + 120  # Increase width by additional 20 pixels

button_rectangle_image_select = pygame.image.load(os.path.join(PNG_PATH, 'button_rectangle_depth_line.png')).convert_alpha()
button_rectangle_image_select = pygame.transform.scale(button_rectangle_image_select, (select_level_width, 100))  # Adjust size as needed

# Load and resize tank images to smaller sizes
tank_body_image = pygame.image.load(os.path.join(TANK_PATH, 'tanks_tankDesert_body1.png')).convert_alpha()
tank_body_image = pygame.transform.scale(tank_body_image, (50, 40))  # Adjust to a smaller size

tank_tracks_image = pygame.image.load(os.path.join(TANK_PATH, 'tanks_tankTracks1.png')).convert_alpha()
tank_tracks_image = pygame.transform.scale(tank_tracks_image, (47, 20))  # Adjust to a smaller size

tank_turret_image = pygame.image.load(os.path.join(TANK_PATH, 'tanks_turret2.png')).convert_alpha()
tank_turret_image = pygame.transform.scale(tank_turret_image, (25, 25))  # Adjust to a smaller size

# Rotate the turret image
tank_turret_image = pygame.transform.rotate(tank_turret_image, -90)  # Rotate 90 degrees to face upwards

# Load the new bullet image
bullet_image = pygame.image.load(os.path.join(BULLET_PATH, 'tank_bullet2.png')).convert_alpha()
# Rotate the bullet image
bullet_image = pygame.transform.rotate(bullet_image, -90)  # Rotate 90 degrees to face the right side up

# Load and rotate the red bomb image
red_bomb_image = pygame.image.load(os.path.join(TANK_PATH, 'tank_bullet3.png')).convert_alpha()
red_bomb_image = pygame.transform.rotate(red_bomb_image, -90)  # Rotate 90 degrees to face the right side down

# Load and rotate the blue bomb image
blue_bomb_image = pygame.image.load(os.path.join(TANK_PATH, 'tank_bulletFly4.png')).convert_alpha()
blue_bomb_image = pygame.transform.rotate(blue_bomb_image, -90)  # Rotate 90 degrees to face the right side down

# Resize the red bomb image
red_bomb_image = pygame.transform.scale(red_bomb_image, (20, 30))

# Resize the blue bomb image
blue_bomb_image = pygame.transform.scale(blue_bomb_image, (20, 60))

# Load the image
ground_image = pygame.image.load(os.path.join(BACKGROUND_PATH, 'castle.png')).convert_alpha()

# Scale the image to fit the screen width and half its original height
ground_image = pygame.transform.scale(ground_image, (screen_width, ground_image.get_height() // 2))

music_directory = None

def choose_music_directory():
    global music_directory
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    directory = filedialog.askdirectory(initialdir="D:/music", title="Select Music Folder")
    return directory

# Set music directory at the start
if music_directory is None:
    music_directory = choose_music_directory()

# Function to load music files
def load_music_files(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp3") or file.endswith(".wav"):
            music_files.append(file)
    return music_files

# Function to play selected music
def play_music(music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)  # Loop indefinitely

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Choose music directory and load music files
music_directory = choose_music_directory()
music_files = load_music_files(music_directory)

# Music buttons list
music_buttons = []

# Create buttons for each music file
for i, music_file in enumerate(music_files):
    music_buttons.append({
        "text": music_file,
        "rect": pygame.Rect(50, 50 + i * 40, 700, 30)
    })

class Enemy:
    def __init__(self, x, y, image, enemy_type):
        self.rect = pygame.Rect(x, y, enemy_width, enemy_height)
        self.image = image
        self.original_image = image  # Store the original image
        self.enemy_type = enemy_type
        self.explosion_index = 0
        self.dead = False
        self.explosion_timer = 0
        self.remove_flag = False  # Add a flag to mark the enemy for removal
        self.direction = 1  # Default direction

    def die(self):
        self.dead = True
        self.explosion_timer = pygame.time.get_ticks()

    def update(self):
        if self.dead:
            if self.explosion_index < len(explosion_images):
                if pygame.time.get_ticks() - self.explosion_timer > 100:
                    self.image = explosion_images[self.explosion_index]
                    self.explosion_index += 1
                    self.explosion_timer = pygame.time.get_ticks()
            else:
                self.remove_flag = True  # Mark for removal
        else:
            # Update enemy movement logic here
            pass

    def update_image(self):
        if self.direction == 1:  # Moving right
            angle = -10  # Tilt forward to the right
            mirrored = True  # Mirror the image
        else:  # Moving left
            angle = 10  # Tilt forward to the left
            mirrored = False  # Do not mirror the image

        if mirrored:
            image = pygame.transform.flip(self.original_image, True, False)  # Mirror horizontally
        else:
            image = self.original_image

        # Apply rotation
        self.image = pygame.transform.rotate(image, angle)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tank settings
tank_width = 60
tank_height = 20
tank_speed = 9
tank = pygame.Rect(screen_width // 2 - tank_width // 2, screen_height - tank_height - 10, tank_width, tank_height)

# Bullet settings
bullet_width = 8
bullet_height = 10
bullet_speed = 18
bullets = []
bullet_cooldown = 50  # Cooldown in milliseconds (1 bullet per second)
last_bullet_time = 0  # Time when the last bullet was fired

# Laser dimensions
laser_width = 20  # Set the width of the laser beam
laser_height = screen_height

# Bomb settings
bomb_width = 10
bomb_height = 20
bomb_speed = 6  #bomb speed
blue_bomb_speed = bomb_speed * 2
bombs = []

# Enemy settings
enemy_width = 110
enemy_height = 60
enemy_speeds = [2, 4, 6]  # Different enemy speeds (slow, normal, fast)
enemy_health = [1, 2, 3]  # Different enemy health
enemy_types = ["normal", "fast", "tanky"]  # Define different types of enemies
enemies = []  # List for enemies

# Define the path to assets
ASSET_PATH = os.path.join(base_path, "Assets")
BULLET_PATH = os.path.join(ASSET_PATH, "tankPNG", "Default size")

# Load and resize the explosion images
explosion_images = [
    pygame.transform.scale(pygame.image.load(os.path.join(BULLET_PATH, 'tank_explosion1.png')).convert_alpha(), (enemy_width, enemy_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(BULLET_PATH, 'tank_explosion2.png')).convert_alpha(), (enemy_width, enemy_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(BULLET_PATH, 'tank_explosion3.png')).convert_alpha(), (enemy_width, enemy_height)),
    pygame.transform.scale(pygame.image.load(os.path.join(BULLET_PATH, 'tank_explosion4.png')).convert_alpha(), (enemy_width, enemy_height))
]

# Game variables
lives = 3
score = 0
level = 1
game_over = False
enemy_spawn_timer = 0  # To track enemy spawn time
bomb_spawn_timer = 0  # To track bomb spawn time for enemies
enemies_spawned = 0  # Count of enemies spawned
shield_radius = 40  # Radius of the shield
shield_max_hits = 3  # Maximum hits the shield can take
shield_hits = shield_max_hits  # Current hit points of the shield
shield_active = True  # Shield is always active now
shield_regen_timer = 0  # Timer for regeneration
shield_regen_cooldown = 60  # 60 frames = 1 second
laser_kills_needed = 30  # Kills required to activate the laser
kills_for_laser = 0  # Current number of kills towards the laser
laser_active = False  # Track if the laser is active
laser_timer = 0  # Timer for how long the laser has been active
laser_duration = 180  # Number of frames the laser is active

ammo = 30
reload_time = 2000  # Reload time in milliseconds
last_shot_time = pygame.time.get_ticks()  # Initialize last shot time
reloading = False  # Track if reloading is in progress
total_score = 0
enemy_rects = [pygame.Rect(100, 50, 50, 50), pygame.Rect(200, 50, 50, 50), pygame.Rect(300, 50, 50, 50)]
player_side_history = []
best_score = 0
player_name = "Player1"
player_score = 0

level_start_time = 0
AI_CYCLE_DURATION = 10000  # 10 seconds
NORMAL_DURATION = 2000     # 2 seconds
ai_cycle_timer = 0
ai_state = "initial"
mimic_active = False

# Jump settings
jump_height = 300  # Height of the jump
jump_speed = 10  # Speed at which the tank rises
gravity = 1  # Gravity effect
is_jumping = False  # Whether the tank is currently jumping
jump_velocity = 0  # The current velocity for the jump

# Kamikaze settings
kamikaze_color = (255, 165, 0)  # Orange
kamikaze_speed = 4
kamikaze_spawn_chance = 1

def update_background_positions():
    global background_positions
    for key in background_positions:
        background_positions[key] -= background_speeds[key]
        # Reset position if the image moves off screen
        if background_positions[key] <= -screen_width:
            background_positions[key] = 0

def draw_ground():
    screen.blit(ground_image, (0, screen_height - ground_image.get_height()))

def draw_background(screen, background_type, level=None):
    if background_type == "quack_attack":
        layers = ["background", "sun", "city4plan", "city3plan", "city2plan", "light", "smog2", "smog1", "city1plan"]
        for key in layers:
            if key == "sun":
                screen.blit(background_images[key], (background_positions[key] + screen_width // 6, screen_height // 10))  # Positioning the sun
            else:
                screen.blit(background_images[key], (background_positions[key], 0))
                screen.blit(background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_2" and level == 2:
        layers = ["a1", "a2", "a3", "a4", "a5"]
        for key in layers:
            screen.blit(level_2_background_images[key], (background_positions[key], 0))
            screen.blit(level_2_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_3" and level == 3:
        layers = ["b1", "b2", "b3", "b4", "b5", "b6"]
        for key in layers:
            screen.blit(level_3_background_images[key], (background_positions[key], 0))
            screen.blit(level_3_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_4" and level == 4:
        layers = ["c1", "c2", "c3", "c4", "c5"]
        for key in layers:
            screen.blit(level_4_background_images[key], (background_positions[key], 0))
            screen.blit(level_4_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_5" and level == 5:
        layers = ["d1", "d2", "d3", "d4", "d5"]
        for key in layers:
            screen.blit(level_5_background_images[key], (background_positions[key], 0))
            screen.blit(level_5_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_6" and level == 6:
        layers = ["e1", "e2", "e3", "e4", "e5"]
        for key in layers:
            screen.blit(level_6_background_images[key], (background_positions[key], 0))
            screen.blit(level_6_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_7" and level == 7:
        layers = ["f1", "f2", "f3", "f4", "f5", "f6"]
        for key in layers:
            screen.blit(level_7_background_images[key], (background_positions[key], 0))
            screen.blit(level_7_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_8" and level == 8:
        layers = ["g1", "g2", "g3", "g4", "g5"]
        for key in layers:
            screen.blit(level_8_background_images[key], (background_positions[key], 0))
            screen.blit(level_8_background_images[key], (background_positions[key] + screen_width, 0))
    elif background_type == "level_9" and level == 9:
        layers = ["h1", "h2", "h3", "h4", "h5"]
        for key in layers:
            screen.blit(level_9_background_images[key], (background_positions[key], 0))
            screen.blit(level_9_background_images[key], (background_positions[key] + screen_width, 0))
    else:
        for key in ["background", "sun", "city4plan", "city3plan", "city2plan", "smog2", "smog1", "light", "city1plan"]:
            screen.blit(background_images[key], (background_positions[key], 0))
            screen.blit(background_images[key], (background_positions[key] + screen_width, 0))

def handle_jump():
    global is_jumping, jump_velocity, tank
    if is_jumping:
        # If jumping, apply velocity to move the tank upwards
        tank.y -= jump_velocity
        jump_velocity -= gravity  # Apply gravity to slow down the jump

        # If the tank has reached the peak or ground level
        if tank.y >= screen_height - tank_height - 10:  # Tank reaches the ground
            tank.y = screen_height - tank_height - 10
            is_jumping = False  # End the jump
            jump_velocity = 0  # Reset jump velocity

def draw_laser_counter():
    laser_counter_text = f"Laser - {kills_for_laser}/{laser_kills_needed}"
    laser_counter_surface = font.render(laser_counter_text, True, (255, 255, 255))  # White color for text
    screen.blit(laser_counter_surface, (10, 50))  # Adjust the position as needed

def handle_shield():
    global shield_hits, shield_regen_timer, shield_active  # Declare shield_active as global if needed

    # Check if shield should regenerate
    if shield_hits < shield_max_hits:
        if shield_regen_timer >= 3:  # Wait 3 seconds after not taking damage
            shield_hits += 1  # Regenerate 1 hit point
            shield_regen_timer = 0  # Reset the regen timer after regenerating
            if shield_hits > 0:
                shield_active = True  # Reactivate shield when regeneration starts
        else:
            # Only increment timer if it's not time to regenerate
            shield_regen_timer += 1 / 60  # Increase by 1/60 if your frame rate is 60 FPS

    # Placeholder for damage detection logic (e.g., collision with enemies)
    damage_taken = False  # Set this to True when shield takes damage

    # If the shield is active and damage is taken, reduce hits and reset the timer
    if shield_hits > 0 and damage_taken:
        shield_hits -= 1
        shield_regen_timer = 0  # Reset regen timer on taking damage

def draw_shield():
    """Draw the shield if active and hit points remain."""
    if shield_active and shield_hits > 0:
        # Set the shield color based on hit points
        if shield_hits == 3:
            shield_color = (0, 255, 0)  # Green
        elif shield_hits == 2:
            shield_color = (255, 255, 0)  # Yellow
        elif shield_hits == 1:
            shield_color = (255, 0, 0)  # Red
        else:
            shield_color = (0, 255, 0)  # Default to green (in case of unexpected value)

        # Draw the shield with the appropriate color
        pygame.draw.circle(screen, shield_color, (tank.x + tank_width // 4, tank.y + tank_height // 5), shield_radius, 2)

def fire():
    global ammo, last_bullet_time, reloading
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

    if current_time - last_bullet_time >= bullet_cooldown and not reloading:  # Check cooldown and reloading
        if ammo > 0:
            # Calculate the turret's end position
            turret_x = tank.x + (tank_body_image.get_width() - tank_turret_image.get_width()) // 2
            turret_y = tank.y - 23  # Adjusting y position to match the turret's position

            bullet_x = turret_x + tank_turret_image.get_width() // 2
            bullet_y = turret_y + tank_turret_image.get_height() // 2

            # Create a bullet at the calculated position
            bullet_rect = bullet_image.get_rect(center=(bullet_x, bullet_y))
            bullets.append(bullet_rect)

            ammo -= 1
            last_bullet_time = current_time  # Update the last bullet time
        else:
            print("Out of ammo! Reloading...")
            reloading = True  # Set reloading flag to True
            last_shot_time = pygame.time.get_ticks()  # Set the reload start time

def reload_ammo():
    global ammo, reloading
    current_time = pygame.time.get_ticks()

    # Reload ammo if enough time has passed
    if reloading and current_time - last_shot_time >= reload_time:
        ammo = 30  # Reset ammo to full
        reloading = False  # Reset reloading flag
        print("Ammo reloaded!")

def draw_reloading_text():
    if reloading:
        text = font.render("Reloading...", True, RED)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)  # Draw the reloading text in the middle

def draw_laser(kills_for_laser, laser_kills_needed):
    global screen  # Use global screen

    # Create a rect for the laser text
    laser_rect = pygame.Rect(screen_width // 2 - 100, 20, 200, 40)  # Adjust position as needed

    # Draw the laser text using the rect
    draw_text(f"Laser - {kills_for_laser}/{laser_kills_needed}", kenney_font_36, BLACK, laser_rect.centerx, laser_rect.centery)

def draw_tank(position):
    x, y = position
    y -= 10
    x -= 10

    # Draw the turret first, positioned behind the body
    turret_x = x + (tank_body_image.get_width() - tank_turret_image.get_width()) // 2
    turret_y = y - 23  # Adjusting y position to be 3 pixels higher
    screen.blit(tank_turret_image, (turret_x, turret_y))

    # Draw the body next, positioned above the tracks
    screen.blit(tank_body_image, (x, y - 10))  # Adjusting y position to fit with the tracks

    # Draw the tracks last (top layer), aligned with the ground
    screen.blit(tank_tracks_image, (x, y + 12))  # Adjusting y position to be 2 pixels lower

def draw_bullets():
    for bullet in bullets:
        bullet.y -= 10  # Adjust bullet speed as needed to move straight up
        screen.blit(bullet_image, bullet.topleft)  # Draw the new bullet image

def draw_bombs():
    for bomb in bombs:
        screen.blit(bomb["image"], bomb["rect"].topleft)

def draw_enemies():
    for enemy_data in enemies:
        enemy_type = enemy_data["type"]
        x, y = enemy_data["rect"].topleft
        direction = enemy_data["direction"]

        # Determine the rotation angle based on direction
        if direction == 1:  # Moving right
            angle = -10  # Tilt forward to the right
            mirrored = True  # Mirror the image
        else:  # Moving left
            angle = 10  # Tilt forward to the left
            mirrored = False  # Do not mirror the image

        if enemy_type == "normal":
            front_image = pygame.transform.rotate(normal_front_image, angle)
            behind_image = pygame.transform.rotate(normal_behind_image, angle)
            if mirrored:
                front_image = pygame.transform.flip(front_image, True, False)  # Mirror horizontally
                behind_image = pygame.transform.flip(behind_image, True, False)  # Mirror horizontally
            screen.blit(behind_image, (x - 0.5, y - 0.5))  # Draw the behind image slightly offset
            screen.blit(front_image, (x, y))  # Draw the front image

        elif enemy_type == "fast":
            front_image = pygame.transform.rotate(fast_front_image, angle)
            behind_image = pygame.transform.rotate(fast_behind_image, angle)
            if mirrored:
                front_image = pygame.transform.flip(front_image, True, False)  # Mirror horizontally
                behind_image = pygame.transform.flip(behind_image, True, False)  # Mirror horizontally
            screen.blit(behind_image, (x - 0.5, y - 0.5))  # Draw the behind image slightly offset
            screen.blit(front_image, (x, y))  # Draw the front image

        elif enemy_type == "tanky":
            front_image = pygame.transform.rotate(tanky_front_image, angle)
            behind_image = pygame.transform.rotate(tanky_behind_image, angle)
            if mirrored:
                front_image = pygame.transform.flip(front_image, True, False)  # Mirror horizontally
                behind_image = pygame.transform.flip(behind_image, True, False)  # Mirror horizontally
            screen.blit(behind_image, (x - 0.5, y - 0.5))  # Draw the behind image slightly offset
            screen.blit(front_image, (x, y))  # Draw the front image

        elif enemy_type == "kamikaze":
            # Mirror the kamikaze plane to face the correct direction
            if direction == 1:  # Moving right, face right
                plane_image = kamikaze_image  # No mirroring needed
            else:  # Moving left, face left
                plane_image = pygame.transform.flip(kamikaze_image, True, False)  # Mirror horizontally
            screen.blit(plane_image, (x, y))

def draw_text(text, font, color, center_x, center_y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    screen.blit(text_surface, text_rect)

def draw_score(score):
    # Create a rect for the score text
    score_rect = pygame.Rect(10, 50, 200, 40)  # Adjust size as needed

    # Draw the score text using the rect
    draw_text(f"Score: {score}", kenney_font_36, BLACK, score_rect.centerx, score_rect.centery)

def draw_lives(lives):
    global screen  # Use global screen

    # Create a rect for the lives text
    lives_rect = pygame.Rect(10, 10, 200, 40)  # Adjust position as needed

    # Draw the lives text using the rect
    draw_text(f"Lives: {lives}", kenney_font_36, BLACK, lives_rect.centerx, lives_rect.centery)

def start_screen():
    screen.fill(WHITE)
    draw_background(screen, "quack_attack")  # Use the specific background
    draw_text("TANK COMMANDER: TACTICAL NEMESIS", kenney_font_72, BLACK, screen_width // 2, screen_height // 2)

    pygame.display.flip()  # Update the screen

    # Wait for user input to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def level_selection_screen():
    global total_score  # Use global variables

    selected_level = None
    level_boxes = []  # Initialize level_boxes outside the loop

    # Load music files from the pre-selected directory
    music_files = load_music_files(music_directory)

    # Randomly select up to 20 music files
    if len(music_files) > 20:
        music_files = random.sample(music_files, 20)

    # Music buttons list
    music_buttons = []

    # Resize button background image to fit text
    button_image_height = 30
    button_image_width = 300  # Adjust width to fit better
    button_rectangle_image_resized = pygame.transform.scale(button_rectangle_image_select, (button_image_width, button_image_height))

    # Create smaller buttons for each music file
    for i, music_file in enumerate(music_files):
        displayed_text = music_file[:20] + '...' if len(music_file) > 20 else music_file  # Limit to 20 characters
        music_buttons.append({
            "text": displayed_text,
            "full_text": music_file,  # Store the full text to play the correct file
            "rect": pygame.Rect(50, 50 + i * (button_image_height + 5), button_image_width, button_image_height)  # Adjust size and spacing
        })

    scroll_offset = 0
    max_scroll = max(0, len(music_buttons) * (button_image_height + 5) - screen_height + 100)

    best_score = load_best_score()  # Load the best score

    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a level was selected
                for i, box in enumerate(level_boxes):
                    if box.collidepoint(event.pos):
                        selected_level = i + 1
                # Check if a music file was selected
                for button in music_buttons:
                    adjusted_rect = button["rect"].move(0, -scroll_offset)
                    if adjusted_rect.collidepoint(event.pos):
                        selected_music_file = button["full_text"]  # Use the full text to get the correct file path
                        music_path = os.path.join(music_directory, selected_music_file)
                        play_music(music_path)
                # Check if Endless Mode was selected
                if endless_mode_box.collidepoint(event.pos):
                    selected_level = "Endless Mode"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scroll_offset = max(0, scroll_offset - 20)
                elif event.key == pygame.K_DOWN:
                    scroll_offset = min(max_scroll, scroll_offset + 20)

        screen.fill(WHITE)
        draw_background(screen, "quack_attack")  # Use the specific background

        # Draw the best score label
        best_score_text = f"Best Score: {best_score}"
        draw_text(best_score_text, kenney_font_48, BLACK, screen_width // 2, screen_height // 4 - 100)

        # Draw the resized rectangle image behind the "Select Level" label
        screen.blit(button_rectangle_image_select, (screen_width // 2 - select_level_width // 2, screen_height // 4 - 50))

        # Calculate position to center the text
        select_level_text = "Select Level"
        draw_text(select_level_text, kenney_font_48, BLACK, screen_width // 2, screen_height // 4)

        # Set up level boxes using the loaded button image
        level_boxes = []  # Reinitialize level_boxes within the drawing loop
        for i in range(10):
            x = screen_width // 2 - (5 * 60) + (i % 5) * 120  # Adjusted for centering
            y = screen_height // 2 - 60 + (i // 5) * 120
            level_box = pygame.Rect(x, y, 100, 100)
            screen.blit(button_image, (x, y))
            draw_text(str(i + 1), kenney_font_48, BLACK, x + 50, y + 50)  # Change text color to black
            level_boxes.append(level_box)

        # Draw music buttons with the resized background image
        for button in music_buttons:
            adjusted_rect = button["rect"].move(0, -scroll_offset)
            if adjusted_rect.top <= screen_height and adjusted_rect.bottom >= 0:  # Only draw visible buttons
                screen.blit(button_rectangle_image_resized, adjusted_rect.topleft)  # Use the resized image as background
                text_surface = font.render(button["text"], True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=adjusted_rect.center)  # Center the text within the button
                screen.blit(text_surface, text_rect.topleft)

        # Add Endless Mode Box next to Level 10 box
        endless_mode_box = pygame.Rect(screen_width // 2 + 5 * 60, screen_height // 2 - 60, 100, 100)
        screen.blit(button_image, endless_mode_box.topleft)
        draw_text("?!", kenney_font_48, BLACK, endless_mode_box.centerx, endless_mode_box.centery)

        pygame.display.flip()  # Update the screen

    return selected_level

def show_message(text, level):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        update_background_positions()  # Update background positions
        if level == 2:
            draw_background(screen, "level_2", level)  # Use the specific background for level 2
        elif level in [1, 10]:
            draw_background(screen, "quack_attack")  # Use the specific background for levels 1 and 10
        elif level == 3:
            draw_background(screen, "level_3", level)  # Use the specific background for level 3
        elif level == 4:
            draw_background(screen, "level_4", level)  # Use the specific background for level 4
        elif level == 5:
            draw_background(screen, "level_5", level)  # Use the specific background for level 5
        elif level == 6:
            draw_background(screen, "level_6", level)  # Use the specific background for level 6
        elif level == 7:
            draw_background(screen, "level_7", level)  # Use the specific background for level 7
        elif level == 8:
            draw_background(screen, "level_8", level)  # Use the specific background for level 8
        elif level == 9:
            draw_background(screen, "level_9", level)  # Use the specific background for level 9
        else:
            draw_background(screen, "default")  # Use default behavior
        draw_text(text, kenney_font_72, BLACK, screen_width // 2, screen_height // 2)
        pygame.display.flip()
        pygame.time.delay(100)  # Small delay to update the display

def show_game_result(result_text):
    global screen  # Use global screen

    screen.fill(WHITE)

    # Create a rect for the result text
    result_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 100, 300, 100)

    # Draw the result text using the rect
    draw_text(result_text, kenney_font_72, BLACK, result_rect.centerx, result_rect.centery)

    pygame.display.flip()

    pygame.time.wait(3000)  # Pause for 3 seconds

def show_level_cleared():
    screen.fill(WHITE)
    # Center the "Level Cleared!" text
    level_cleared_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 - 100, 300, 100)
    draw_text("Level Cleared!", kenney_font_72, BLACK, level_cleared_rect.centerx, level_cleared_rect.centery)
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before returning to menu

def spawn_bomb(enemy, color=RED, speed=5):
    bomb = pygame.Rect(enemy.centerx, enemy.bottom, 10, 20)  # Adjust size to fit the image
    bomb_image = red_bomb_image if color == RED else blue_bomb_image
    return {"rect": bomb, "image": bomb_image, "speed": speed}

def spawn_enemy(side):
    enemy_type = random.choices(
        enemy_types + ["kamikaze"],  # Add "kamikaze" to enemy types
        [1, 1, 1, kamikaze_spawn_chance]  # Assign lower weight to "kamikaze"
    )[0]

    if side == "left":
        x = -enemy_width  # Start off the left side
        direction = 1  # Move right
    else:
        x = screen_width  # Start off the right side
        direction = -1  # Move left

    y = random.randint(0, screen_height // 2 - enemy_height)

    speed, health = enemy_speeds[1], enemy_health[0]  # Normal settings for simplicity

    if enemy_type == "kamikaze":
        speed = kamikaze_speed
        health = 1  # Kamikaze enemies typically have low health
        behavior_type = "kamikaze"  # Set kamikaze behavior
    else:
        behavior_type = random.choice(["follow", "dodge", "flee", "block", "follow_player"])

    enemy_data = create_enemy(x, y, enemy_type)  # Use create_enemy function
    enemy_data.update({
        "direction": direction,
        "speed": speed,
        "health": health,
        "behavior": behavior_type,
        "spawn_time": pygame.time.get_ticks(),
        "ai_enabled": False,
        "last_position": (x, y),
        "stuck_timer": 0,
        "resetting": False,
        "last_bomb_time": pygame.time.get_ticks(),  # Initialize last_bomb_time
        "last_blue_bomb_time": pygame.time.get_ticks()  # Initialize last_blue_bomb_time
    })
    return enemy_data

def move_and_spawn_enemies(total_stock, max_enemies_on_screen, player_state):
    global enemy_spawn_timer, enemies_spawned, bomb_spawn_timer, score  # Add score to global variables

    # Ensure we keep spawning new enemies if below the total stock and screen limit
    if enemies_spawned < total_stock and len(enemies) < max_enemies_on_screen:
        if enemy_spawn_timer % 20 == 0:  # Control the spawn rate
            side = "left" if enemies_spawned % 2 == 0 else "right"
            new_enemy = spawn_enemy(side)
            if new_enemy:
                enemies.append(new_enemy)
                enemies_spawned += 1

    current_time = pygame.time.get_ticks()
    ai_activation_delay = 3000  # 3 seconds delay

    # Track enemies to remove after iteration
    enemies_to_remove = []

    # Move existing enemies
    for enemy_data in enemies:
        enemy = enemy_data["rect"]
        behavior = enemy_data["behavior"]
        spawn_time = enemy_data["spawn_time"]
        direction = enemy_data["direction"]

        if behavior == "kamikaze":
            # Direct kamikaze movement towards the player
            if enemy.x < tank.x:
                enemy.x += enemy_data["speed"]
                direction = 1  # Moving right
            elif enemy.x > tank.x:
                enemy.x -= enemy_data["speed"]
                direction = -1  # Moving left

            # Move downwards towards the player
            enemy.y += enemy_data["speed"]

            # Check for collision with ground or player
            if enemy.colliderect(tank):
                handle_collisions()
            if enemy.y >= screen_height - enemy_height:
                enemies_to_remove.append(enemy_data)  # Mark for removal
                score += 10  # Increment score when kamikaze enemy collides with ground
        else:
            # Enable AI behaviors after the delay
            if current_time - spawn_time > ai_activation_delay:
                if not enemy_data["ai_enabled"]:
                    enemy_data["ai_enabled"] = True

                if behavior == "follow":
                    if tank.x < enemy.x:
                        enemy.x -= enemy_data["speed"]
                        direction = -1  # Moving left
                    elif tank.x > enemy.x:
                        enemy.x += enemy_data["speed"]
                        direction = 1  # Moving right
                elif behavior == "dodge":
                    dodge_direction = None
                    for bullet in bullets:
                        if bullet.y - enemy.y < 100 and abs(bullet.x - enemy.x) < 50:
                            if bullet.x < enemy.x:
                                dodge_direction = 1  # Move right
                            elif bullet.x > enemy.x:
                                dodge_direction = -1  # Move left

                    if dodge_direction is not None:
                        enemy.x += dodge_direction * enemy_data["speed"]
                        direction = dodge_direction  # Set the dodging direction
                    else:
                        enemy.x += enemy_data["direction"] * enemy_data["speed"]  # Continue moving in set direction

                elif behavior == "flee":
                    # Ensure enemies flee when the laser is active
                    if laser_active and abs(tank.centerx - enemy.centerx) < 300:
                        if tank.x < enemy.x:
                            enemy.x += enemy_data["speed"]
                            direction = 1  # Moving right
                        elif tank.x > enemy.x:
                            enemy.x -= enemy_data["speed"]
                            direction = -1  # Moving left
                    else:
                        enemy.x += enemy_data["direction"] * enemy_data["speed"]
            else:
                enemy.x += enemy_data["direction"] * enemy_data["speed"]  # Move right or left initially

        # Ensure enemy stays within screen boundaries
        if enemy.left < 0:
            direction = 1
        elif enemy.right > screen_width:
            direction = -1

        if direction != enemy_data["direction"]:
            enemy_data["direction"] = direction
            enemy_data["instance"].update_image()

        # Bomb spawning logic for non-kamikaze enemies
        if enemy_data["type"] != "kamikaze":
            if "last_bomb_time" not in enemy_data:
                enemy_data["last_bomb_time"] = current_time

            if "next_bomb_time" not in enemy_data:
                enemy_data["next_bomb_time"] = current_time + random.randint(1000, 5000)  # Random interval between 1 to 5 seconds

            if "last_blue_bomb_time" not in enemy_data:
                enemy_data["last_blue_bomb_time"] = current_time

            # Drop red bomb randomly
            if current_time - enemy_data["last_bomb_time"] >= 1000:  # Ensure at least 1 second has passed since the last bomb
                if random.random() <= 0.8:  # 80% chance to drop a red bomb
                    bombs.append(spawn_bomb(enemy, color=RED, speed=5))  # Drop red bomb
                    enemy_data["last_bomb_time"] = current_time
                    enemy_data["next_bomb_time"] = current_time + random.randint(1000, 5000)  # Set next bomb time
            else:
                # Check for blue bomb drop if player is directly below and cooldown of 5 seconds
                if abs(tank.x - enemy.x) < enemy.width:  # Check if player is directly below
                    if current_time - enemy_data["last_blue_bomb_time"] >= 5000:  # Ensure 5 seconds have passed since the last blue bomb
                        if random.random() <= 0.5:  # 50% chance to drop a blue bomb
                            bombs.append(spawn_bomb(enemy, color=BLUE, speed=blue_bomb_speed))  # Drop blue bomb
                            enemy_data["last_blue_bomb_time"] = current_time
                elif current_time - enemy_data["last_blue_bomb_time"] >= 1000:  # Ensure at least 1 second has passed since the last try
                    enemy_data["next_bomb_time"] = current_time + 300  # Retry after 0.3 seconds if no bomb is dropped

    # Remove enemies marked for removal after the loop
    for enemy_data in enemies_to_remove:
        if enemy_data in enemies:
            enemies.remove(enemy_data)

    enemy_spawn_timer += 1
    bomb_spawn_timer += 1

def handle_laser():
    global laser_timer, laser_active, score  # Add score to the global scope

    laser_rect = pygame.Rect(tank.centerx - laser_width // 1, tank.top - laser_height, laser_width, laser_height)
    pygame.draw.rect(screen, (0, 255, 0), laser_rect)

    for enemy_data in enemies[:]:
        if enemy_data["rect"].colliderect(laser_rect):
            enemies.remove(enemy_data)
            score += 10  # Update the score

    for bomb in bombs[:]:
        if bomb["rect"].colliderect(laser_rect):
            bombs.remove(bomb)

    laser_timer += 1
    if laser_timer >= laser_duration:
        laser_active = False
        laser_timer = 0

def update_bombs():
    for bomb in bombs[:]:
        bomb["rect"].y += bomb["speed"]
        if bomb["rect"].y > screen_height:
            bombs.remove(bomb)  # Remove the bomb if it goes off screen

def update_bullets():
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)  # Remove the bullet if it goes off screen

def handle_collisions():
    global lives, shield_hits, shield_active, enemies, bombs, score, kills_for_laser

    for enemy_data in enemies[:]:
        enemy = enemy_data["instance"].rect

        # Check for collision with tank
        if enemy.colliderect(tank):
            if enemy_data["type"] == "kamikaze":
                if shield_active and shield_hits > 0:
                    shield_hits -= 1
                    enemies.remove(enemy_data)
                    if shield_hits <= 0:
                        shield_active = False
                else:
                    lives -= 1
                    enemies.remove(enemy_data)
                    enemy_data["instance"].die()  # Trigger explosion animation for kamikaze enemy
            else:
                # Existing logic for non-kamikaze enemies
                if shield_active and shield_hits > 0:
                    shield_hits -= 1
                    enemies.remove(enemy_data)
                    if shield_hits <= 0:
                        shield_active = False
                else:
                    lives -= 1
                    enemies.remove(enemy_data)
                    enemy_data["instance"].die()  # Trigger explosion animation for regular enemy

        # Check for bullet collisions with enemies
        for bullet in bullets[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                score += 10  # Increment score for hitting an enemy
                kills_for_laser += 1  # Increment kills for laser activation
                enemy_data["health"] -= 1  # Decrease enemy health
                if enemy_data["health"] <= 0:
                    enemy_data["instance"].die()  # Trigger explosion animation
                break

    for bomb in bombs[:]:
        if bomb["rect"].colliderect(tank):
            if shield_active and shield_hits > 0:
                shield_hits -= 1
                bombs.remove(bomb)
                if shield_hits <= 0:
                    shield_active = False
            else:
                lives -= 1
                bombs.remove(bomb)

def create_enemy(x, y, enemy_type="normal"):
    if enemy_type == "normal":
        image = normal_front_image
    elif enemy_type == "fast":
        image = fast_front_image
    elif enemy_type == "tanky":
        image = tanky_front_image
    elif enemy_type == "kamikaze":
        image = kamikaze_image

    enemy_instance = Enemy(x, y, image, enemy_type)
    enemy_data = {"rect": enemy_instance.rect, "instance": enemy_instance, "type": enemy_type, "direction": 1}
    enemies.append(enemy_data)
    return enemy_data

def save_best_score(score):
    global best_score
    if score > best_score:
        best_score = score
        try:
            with open("best_score.txt", "w") as file:
                portalocker.lock(file, portalocker.LOCK_EX)  # Lock the file
                file.write(str(score))
                portalocker.unlock(file)  # Unlock the file
        except IOError:
            print("Failed to save the best score.")

def load_best_score():
    try:
        with open("best_score.txt", "r") as file:
            return int(file.read())
    except (IOError, ValueError):
        return 0  # Return 0 if there's an error or the file doesn't exist

load_best_score()


# Function to handle text input on screen using Kenney font
def text_input(screen, prompt, font, clock, background_type=None, level=None):
    input_box = pygame.Rect(200, 300, 400, 50)  # Fixed width for the input box
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Draw the current background
        if background_type:
            draw_background(screen, background_type, level)

        # Render the prompt and input text
        prompt_surface = font.render(prompt, True, color)
        txt_surface = font.render(text, True, color)

        # Adjust positioning
        prompt_x = screen_width // 2 - prompt_surface.get_width() // 2
        prompt_y = screen_height // 2 - 100
        input_box.center = (screen_width // 2, screen_height // 2)

        # Draw the prompt text
        screen.blit(prompt_surface, (prompt_x, prompt_y))

        # Draw the input text within the fixed-size input box
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Draw the text box
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

    return text

def submit_score(name, score):
    url = 'https://my-flask-leaderboard.onrender.com/submit_score'
    data = {'name': name, 'score': score}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Score submitted successfully!")
    else:
        print("Failed to submit score.")


def game_over_screen(current_level):
    global score, best_score

    # Determine the background type for the current level
    background_type = "default"
    if current_level in range(1, 10):
        background_type = f"level_{current_level}"
    elif current_level == 10:
        background_type = "quack_attack"

    # Draw the background for the current level
    draw_background(screen, background_type, current_level)

    # Skip name input for levels 1 to 10 and only show input in Endless Mode
    name = None
    if current_level == "Endless Mode":
        draw_background(screen, selected_background)  # Ensure selected_background is defined in the endless_game_loop
        name = text_input(screen, "Enter your name: ", kenney_font_36, clock, background_type=selected_background)

    if name:  # If a name is entered
        submit_score(name, score)  # Submit the score to the server

    # Display "Game Over" message
    show_message("Game Over", current_level)
    pygame.display.update()  # Update the display to show the background and message
    pygame.time.wait(2000)  # Wait for 2 seconds to show the message

    if score > best_score:
        save_best_score(score)
    pygame.time.wait(2000)  # Wait for 2 seconds to show the message

    return "menu"

def game_loop(level):
    global level_start_time, ai_cycle_timer, ai_state
    global lives, score, game_over, enemy_spawn_timer, bomb_spawn_timer, enemies_spawned, total_score, shield_regen_timer, enemies
    global shield_hits, shield_active, laser_active, laser_timer, kills_for_laser, laser_kills_needed, ammo, is_jumping, jump_velocity
    global total_enemies_spawned, laser_duration, last_shot_time, game_over

    level_start_time = pygame.time.get_ticks()  # Set the start time of the level
    ai_cycle_timer = level_start_time  # Initialize AI cycle timer
    ai_state = "initial"  # Set initial AI state

    lives, score, game_over = 3, 0, False
    laser_active, laser_timer, kills_for_laser = False, 0, 0
    clock = pygame.time.Clock()
    shield_regen_timer += 1 / 60
    enemies.clear()
    bombs.clear()
    enemies_spawned, total_enemies_spawned = 0, 0

    total_stock, max_enemies_on_screen = 30 + (level - 1) * 10, 16 + 3 * (level - 1)  # Increase enemies more per level

    # Player state dictionary
    player_state = {
        "rect": tank,
        "moving_right": False,
        "speed": tank_speed
    }

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not is_jumping:
                    is_jumping, jump_velocity = True, jump_speed
                elif event.key == pygame.K_SPACE:
                    fire()
                elif event.key == pygame.K_e and kills_for_laser >= laser_kills_needed and not laser_active:
                    laser_active, laser_timer, kills_for_laser = True, 0, 0

        reload_ammo()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and tank.left > 0:
            player_state["rect"].x -= player_state["speed"]
            player_state["moving_right"] = False
        elif keys[pygame.K_d] and tank.right < screen_width:
            player_state["rect"].x += player_state["speed"]
            player_state["moving_right"] = True

        handle_shield()
        handle_jump()
        move_and_spawn_enemies(total_stock, max_enemies_on_screen, player_state)
        update_bombs()  # Update bomb positions
        update_bullets()  # Update bullet positions
        handle_collisions()  # Call collision handler

        screen.fill(WHITE)
        update_background_positions()  # Ensure background positions are updated here
        if level == 2:
            draw_background(screen, "level_2", level)  # Use the specific background for level 2
        elif level == 3:
            draw_background(screen, "level_3", level)  # Use the specific background for level 3
        elif level == 4:
            draw_background(screen, "level_4", level)  # Use the specific background for level 4
        elif level == 5:
            draw_background(screen, "level_5", level)  # Use the specific background for level 5
        elif level == 6:
            draw_background(screen, "level_6", level)  # Use the specific background for level 6
        elif level == 7:
            draw_background(screen, "level_7", level)  # Use the specific background for level 7
        elif level == 8:
            draw_background(screen, "level_8", level)  # Use the specific background for level 8
        elif level == 9:
            draw_background(screen, "level_9", level)  # Use the specific background for level 9
        elif level in [1, 10]:
            draw_background(screen, "quack_attack")  # Use the specific background for levels 1 and 10
        else:
            draw_background(screen, "default")  # Use default behavior

        draw_ground()  # Draw the ground image

        draw_tank(player_state["rect"].topleft)  # Draw the resized tank
        draw_bullets()
        draw_bombs()

        # Update and draw enemies
        for enemy_data in enemies:
            enemy_data["instance"].update()
            enemy_data["instance"].draw(screen)

        # Remove enemies flagged for removal
        enemies = [enemy for enemy in enemies if not enemy["instance"].remove_flag]

        draw_lives(lives)
        draw_score(score)
        draw_shield()
        draw_laser(kills_for_laser, laser_kills_needed)
        draw_reloading_text()

        if laser_active:
            handle_laser()  # Call the handle_laser function

        # Check for level completion
        if enemies_spawned >= total_stock and len(enemies) == 0:
            show_message("Day Cleared", level)  # Display "Day Cleared" message
            pygame.time.wait(2000)  # Wait for 2 seconds to show the message
            return "menu"
        if lives <= 0:
            game_over = True
            return game_over_screen(level)  # Pass the current level

        pygame.display.flip()
        clock.tick(60)

def endless_game_loop():
    global level_start_time, ai_cycle_timer, ai_state
    global lives, score, game_over, enemy_spawn_timer, bomb_spawn_timer, enemies_spawned, total_score, shield_regen_timer, enemies
    global shield_hits, shield_active, laser_active, laser_timer, kills_for_laser, laser_kills_needed, ammo, is_jumping, jump_velocity
    global total_enemies_spawned, laser_duration, last_shot_time, game_over, selected_background  # Add selected_background

    lives, score, game_over = 3, 0, False
    laser_active, laser_timer, kills_for_laser = False, 0, 0
    clock = pygame.time.Clock()
    shield_regen_timer += 1 / 60
    enemies.clear()
    bombs.clear()
    enemies_spawned, total_enemies_spawned = 0, 0

    initial_max_enemies_on_screen = 5
    max_enemies_on_screen = initial_max_enemies_on_screen

    enemy_spawn_rate_timer = 0  # Timer to track enemy spawn rate increase

    best_score = load_best_score()

    # Define the list of backgrounds for levels 1 to 10
    backgrounds = ["level_1", "level_2", "level_3", "level_4", "level_5", "level_6", "level_7", "level_8", "level_9", "level_10"]

    # Randomly select a background for this endless game session
    selected_background = random.choice(backgrounds)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not is_jumping:
                    is_jumping, jump_velocity = True, jump_speed
                elif event.key == pygame.K_SPACE:
                    fire()
                elif event.key == pygame.K_e and kills_for_laser >= laser_kills_needed and not laser_active:
                    laser_active, laser_timer, kills_for_laser = True, 0, 0

        reload_ammo()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and tank.left > 0:
            tank.x -= tank_speed
        elif keys[pygame.K_d] and tank.right < screen_width:
            tank.x += tank_speed

        handle_shield()
        handle_jump()
        move_and_spawn_enemies(float("inf"), max_enemies_on_screen, {"rect": tank, "moving_right": False, "speed": tank_speed})
        update_bombs()  # Update bomb positions
        update_bullets()  # Update bullet positions
        handle_collisions()  # Call collision handler

        screen.fill(WHITE)
        update_background_positions()  # Ensure background positions are updated here

        # Draw the selected random background
        if selected_background == "level_2":
            draw_background(screen, "level_2", 2)
        elif selected_background == "level_3":
            draw_background(screen, "level_3", 3)
        elif selected_background == "level_4":
            draw_background(screen, "level_4", 4)
        elif selected_background == "level_5":
            draw_background(screen, "level_5", 5)
        elif selected_background == "level_6":
            draw_background(screen, "level_6", 6)
        elif selected_background == "level_7":
            draw_background(screen, "level_7", 7)
        elif selected_background == "level_8":
            draw_background(screen, "level_8", 8)
        elif selected_background == "level_9":
            draw_background(screen, "level_9", 9)
        elif selected_background == "level_10":
            draw_background(screen, "quack_attack")  # Use the background for level 10
        else:
            draw_background(screen, "default")  # Use default background for level 1

        draw_ground()  # Draw the ground image

        draw_tank((tank.x, tank.y))  # Draw the resized tank
        draw_bullets()
        draw_bombs()

        # Update and draw enemies
        for enemy_data in enemies:
            enemy_data["instance"].update()
            enemy_data["instance"].draw(screen)

        # Remove enemies flagged for removal
        enemies = [enemy for enemy in enemies if not enemy["instance"].remove_flag]

        draw_lives(lives)
        draw_score(score)
        draw_shield()
        draw_laser(kills_for_laser, laser_kills_needed)
        draw_reloading_text()

        if laser_active:
            handle_laser()  # Call the handle_laser function

        # Check for level completion
        if lives <= 0:
            game_over = True
            return game_over_screen("Endless Mode")  # Pass "Endless Mode" as the level

        # Increase enemy spawn rate every minute
        if pygame.time.get_ticks() - enemy_spawn_rate_timer >= 30000:  # Every 60 seconds
            max_enemies_on_screen += 2
            enemy_spawn_rate_timer = pygame.time.get_ticks()  # Reset the timer

        pygame.display.flip()
        clock.tick(60)

# Main game loop
while True:
    start_screen()
    selected_level = level_selection_screen()
    if selected_level == "Endless Mode":
        endless_game_loop()
    else:
        game_loop(selected_level)

pygame.quit()