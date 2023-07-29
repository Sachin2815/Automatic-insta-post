from instabot import Bot
from PIL import Image
import time

# Set your Instagram username and password
username = "python4873"
password = "python123456789"

# Create an instance of the Instabot class
bot = Bot()

# Log in to Instagram
bot.login(username=username, password=password, use_cookie=False, ask_for_code=True)

# Open the image and resize it to a square (1:1) aspect ratio
image_path = "vimal.jpg" # Use forward slashes in the path
image = Image.open(image_path)
width, height = image.size
min_dimension = min(width, height)
resized_image = image.crop((0, 0, min_dimension, min_dimension))

# Save the resized image to a temporary file
temp_image_path = "temp.jpg"
resized_image.save(temp_image_path)

# Upload the resized image with a caption
caption = "failure is the best teacher if you fail in right direction then you will acheive success!"
bot.upload_photo(temp_image_path, caption=caption)

# Logout from your account
bot.logout()
