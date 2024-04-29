#AUTOMATICALLY GENERATE IMAGE CAPTCHAs WITH PYTHON FOR ENHANCED SECURITY

import random
from captcha.image import ImageCaptcha


#specify the image size
image = ImageCaptcha(width = 280, height = 90)

#generate captcha
def generate_captcha(length = 6):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha_text = "".join(random.choice(characters) for i in range(length))
    return captcha_text

#get random captcha text
captcha_text = generate_captcha()

#generate image
data = image.generate(captcha_text)
image.write(captcha_text, 'captcha.png')


from PIL import Image
im = Image.open('captcha.png')


