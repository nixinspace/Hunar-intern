import random
import string

def generate_captcha(length=5):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choices(characters, k=length))
    return captcha

if __name__ == "__main__":
    print("Generated CAPTCHA:", generate_captcha())