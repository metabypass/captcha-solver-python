#------------- reCAPTCHA v2 ----------------
# change samples values with your correct values

import requests,json,time,os
TOKEN_FILE_PATH=os.path.dirname(__file__)+"/metabypass.token"


# Your Credentials
CLIENT_ID='YOUR_CLIENT_ID' #****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET='YOUR_CLIENT_SECRET' #****CHANGE HERE WITH YOUR VALUE*******
EMAIL='YOUR_ACCOUNT_EMAIL'#****CHANGE HERE WITH YOUR VALUE*******
PASSWORD='YOUR_ACCOUNT_PASSWORD' #****CHANGE HERE WITH YOUR VALUE*******

# -----------------------GET ACCESS TOKEN------------------------
def get_new_access_token():

    request_url = "https://app.metabypass.tech/CaptchaSolver/oauth/token"
    payload=json.dumps({
        "grant_type":"password" ,
        "client_id":CLIENT_ID,
        "client_secret":CLIENT_SECRET,
        "username":EMAIL,
        "password":PASSWORD
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", request_url, headers=headers, data=payload)
    
    if response.status_code ==200 :

        responseDict=json.loads(response.text)
        #store access token at cache file
        try:
            with open(TOKEN_FILE_PATH, 'w') as f:
                f.write(responseDict['access_token'])
                f.close()
                return responseDict['access_token']
        except Exception as e:
            print(f"Error writing token to file: {e}")
            exit()

    else:
        print('unauth!')
        exit()


#----------------------------CALL reCAPTCHA v2-------------------------------
def re_captcha_v2(url,site_key):
    request_url = "https://app.metabypass.tech/CaptchaSolver/api/v1/services/bypassReCaptcha"
    payload=json.dumps({
        "sitekey":f"{site_key}" ,
        "version":"2",
        "url":f"{url}",
    })
    #generate access token
    if os.path.exists(TOKEN_FILE_PATH):
        try:
            with open(TOKEN_FILE_PATH, 'r') as f:
                access_token=f.read()
                f.close()
        except Exception as e:
            print(f"Error writing token to file: {e}")
            exit()
    else:
        access_token=get_new_access_token()

    #prepare headers
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("POST", request_url, headers=headers, data=payload)

    if response.status_code==401:
        access_token=get_new_access_token()
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        response = requests.request("POST", request_url, headers=headers, data=payload)

    return json.loads(response.text)

def get_result(recaptcha_id):
        
    request_url = "https://app.metabypass.tech/CaptchaSolver/api/v1/services/getCaptchaResult"

    payload=json.dumps({
        'recaptcha_id': recaptcha_id ,
    })

    #generate access token
    if os.path.exists(TOKEN_FILE_PATH):
        try:
            with open(TOKEN_FILE_PATH, 'r') as f:
                access_token=f.read()
                f.close()
        except Exception as e:
            print(f"Error writing token to file: {e}")
            exit()
    else:
        access_token=get_new_access_token()

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
    }

    response = requests.request("GET", request_url, headers=headers, data=payload)

    if response.status_code==401:
        access_token=get_new_access_token()
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }
        response = requests.request("GET", request_url, headers=headers, data=payload)

    if response.status_code==200:
        response_dict=json.loads(response.text)
        if response_dict['status_code']==200:
            return response_dict['data']['RecaptchaResponse']
        elif response_dict['status_code']==201:
            # print(response_dict['message']+'. wait 10 seconds again ...')
            return False
        else:
            print(response_dict['message'])
        
    return False
    
# call reCAPTCHA v2 API
site_url="YOUR_SITE_URL" #****CHANGE HERE WITH YOUR VALUE*******
site_key="YOUR_SITE_KEY" #****CHANGE HERE WITH YOUR VALUE*******
rev2_response=re_captcha_v2(url=site_url,site_key=site_key)

try:
    recaptcha_id=rev2_response['data']['RecaptchaId']
except:
    print('error!')
    print(rev2_response)
    exit()


#------------------------------ GET RESULT ----------------------------------

# print('wait 10 seconds to get reCAPTCHA result')
for i in range(6):
    #wait 10 seconds to get result
    time.sleep(10)

    result=get_result(recaptcha_id)

    try:
        if result:
            # print(json.dumps(response))
            break
    except:
        print(f"error! {result}")
        pass

    # print("reCAPTCHA result not ready. wait 10 seconds again ...");


print(result)
