from PIL import Image
from captcha.image import ImageCaptcha
import random

# Initialize ImageCaptcha object with static values width=350, height=60
img = ImageCaptcha(width=350, height=60)

# Generate random captcha text


def generate_random_captcha_text(length=8):
    # # Define characters with many various combinations
    characters = "abcdefgh1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
    # Generate captcha text by selecting random characters from the defined set
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text


captcha_text = generate_random_captcha_text()

# Generate captcha in PNG format
data = img.generate(captcha_text)
# Save captcha as a PNG image
img.write(captcha_text, "captcha.png")

# Convert captcha to JPEG format
image_jpeg = ImageCaptcha(width=350, height=60)
data = image_jpeg.generate(captcha_text)
# Save captcha as a JPEG image
image_jpeg.write(captcha_text, "captcha.jpg")

# Open and display captchas in different formats
Image.open('captcha.png').show()
Image.open('captcha.jpg').show()
