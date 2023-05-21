# metabypass-python
## Configuration

Get the following credentials from the "Application" section of the MetaBypass website:
1- Go to Application Section 
2- Click on Create Application Button
3- You can see your credentials like below image
![image](https://github.com/metabypass/metabypass-python/assets/128980891/7e5e4518-719a-4561-97bd-2ff94a4dc217)

```
CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******
```
## Access Token
Input Parameters :

|     Name	  |   Type    |  Required   | Description |
| ----------- | --------- | ----------- | ----------- |
| grant_type	|  string	  |    Yes	    | in this case you should pass the grant_type by type "password" |
| client_id	  |  string	  |    Yes	    | first you need to create an application in your dashboard then you should pass your client_id here |
| client_secret |	string	|    Yes	    | at first you need to create an application in your dashboard then you should pass your client_secret here |
| username	    | string	|    Yes	    | pass your email |
| password	    | string	|    Yes	    | pass your password |

Response :

| Status_code	|  Status  |  Access_token_description  | 
| ----------- | -------- | -------------- |
| 200	        | Success  | your access token |
| 401	        |  Error	 | your access token expired, create another application

## Text_Captcha
Using the  base64.b64encode function to get a bytes object for transferring images as text in API requests
```
def image_to_base64(image_file_path):
    import base64
    with open(image_file_path, "rb") as image_file:
        image_data = image_file.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')
        image_file.close()
        return base64_data
```

