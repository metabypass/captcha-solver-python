# call reCAPTCHA v2 API
from metabypassrecaptcha3 import *

CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******
cred=getCredentials(CLIENT_ID,CLIENT_SECRET,EMAIL,PASSWORD)

site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******
rc3 = reCAPTCHAV3(url=site_url, site_key=site_key,cred=cred)
print(rc3)