#------------- Text CAPTCHA ----------------

import requests,json,os
TOKEN_FILE_PATH=os.path.dirname(__file__)+"/metabypass.token"

# Your Credentials
CLIENT_ID='YOUR_CLIENT_ID' #****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET='YOUR_SECRET_KEY' #****CHANGE HERE WITH YOUR VALUE*******
EMAIL='YOUR_ACCOUNT_EMAIL' #****CHANGE HERE WITH YOUR VALUE*******
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

        response_dict=json.loads(response.text)

        #store access token at cache file
        try:
            with open(TOKEN_FILE_PATH, 'w') as f:
                f.write(response_dict['access_token'])
                f.close()
                return response_dict['access_token']
        except Exception as e:
            print(f"Error writing token to file: {e}")
            exit()

    else:
        print('unauth!')
        exit()

#----------------------------CALL CAPTCHA SOLVER-------------------------------
def image_captcha(image_base64):

    request_url = "https://app.metabypass.tech/CaptchaSolver/api/v1/services/captchaSolver"

    payload=json.dumps({
        "image":f"{image_base64}" ,  #PUT CORRECT BASE64 OF IMAGE
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
        
    if response.status_code==200:

        response_dict=json.loads(response.text)

        if response_dict['status_code']==200:
            return response_dict['data']['result']
        else:
            print(response_dict['message'])
            return False
    else:
        return False

def image_to_base64(image_file_path):
    import base64
    with open(image_file_path, "rb") as image_file:
        image_data = image_file.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')
        image_file.close()
        return base64_data


# usage

#if you have image file you can encode it with this function
#captcha.jpg
image_base64=image_to_base64('YOUR_CAPTCHA_IMAGE_PATH') #****CHANGE HERE WITH YOUR VALUE*******
captcha_response=image_captcha(image_base64)
print(captcha_response)
