from metabypasscaptcha import *
CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******
cred=getCredentials(CLIENT_ID,CLIENT_SECRET,EMAIL,PASSWORD)
image_base64 = image_to_base64('YOUR_CAPTCHA_IMAGE_PATH')  # ****CHANGE HERE WITH YOUR VALUE*******
captcha_rsponse = image_captcha(image_base64,cred)
print(captcha_rsponse)