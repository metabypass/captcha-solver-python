# call reCAPTCHA v2 API
from metabypass import MetaBypass
import time

CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******

solver=MetaBypass(CLIENT_ID,CLIENT_SECRET,EMAIL,PASSWORD)

site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******


rev2_response = solver.reCAPTCHAV2(url=site_url, site_key=site_key)  
print(rev2_response)
