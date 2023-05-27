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
try:
    recaptcha_id = rev2_response['data']['RecaptchaId']
except:
    print('error!')
    print(rev2_response)
    exit()

# ------------------------------ GET RESULT ----------------------------------

# print('wait 10 seconds to get reCAPTCHA result')
for i in range(6):
    # wait 10 seconds to get result
    time.sleep(10)

    result = solver.getResult(recaptcha_id)

    try:
        if result:
            # print(json.dumps(response))
            break
    except:
        print(f"error! {result}")
        pass

    # print("reCAPTCHA result not ready. wait 10 seconds again ...");
print(result)
