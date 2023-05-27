from metabypass import MetaBypass

CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******
solver=MetaBypass(CLIENT_ID,CLIENT_SECRET,EMAIL,PASSWORD)
captcha_response = solver.image_captcha('YOUR_CAPTCHA_IMAGE_PATH')
print(captcha_response)
