# CAPTCHA solver python
Free demo (no credit card required) -> https://app.metabypass.tech/application


## Configuration

Get the following credentials from the "Application" section of the MetaBypass website:

```
CLIENT_ID = 'YOUR_CLIENT_ID'  # ****CHANGE HERE WITH YOUR VALUE*******
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # ****CHANGE HERE WITH YOUR VALUE*******
EMAIL = 'YOUR_ACCOUNT_EMAIL'  # ****CHANGE HERE WITH YOUR VALUE*******
PASSWORD = 'YOUR_ACCOUNT_PASSWORD'  # ****CHANGE HERE WITH YOUR VALUE*******
```

1. Go to Application Section 
2. Click on Create Application Button
3. You can see credentials like below image


![Screenshot 2023-05-21 120957](https://github.com/metabypass/metabypass-python/assets/128980891/4420f7ed-1588-412a-b0e8-2876d4ae1854)


## There are 2 approaches for utilizing Metabypass-python:

### 1. __Easy Implementation__:

   **Notice:**
      You can simply download the following steps in 'MetaBypass_TestCodes'
      
   - Install the 'metabypass' package by executing the following command:
     ```
     pip install metabypass
     ```
     
   - Import 'MetaBypass' class from the package:
     ```
     from metabypass import MetaBypass
     ```
   - Define your credentials:
     ```
     solver=MetaBypass(CLIENT_ID,CLIENT_SECRET,EMAIL,PASSWORD)
     ```
   - To obtain the results for each type of captcha, you can use the following codes:
   
      - **Text_Captcha**
      
        ```
        captcha_response = solver.image_captcha('YOUR_CAPTCHA_IMAGE_PATH')
        print(captcha_response)
        ```  
        
      - **ReCaptcha V2**

        ```
        rev2_response = solver.reCAPTCHAV2(url=site_url, site_key=site_key)  
        print(rev2_response)
        ```  
        
      - **ReCaptcha V3**

        ```
        rev3_response = solver.reCAPTCHAV3(url=site_url, site_key=site_key)
        print(rev3_response)
        ```  


 ------------------------------------------------------------------------------------------------------------------------------------------------------------------

 ### 2. __Raw Implementation__:

  - **Text_Captcha**
    
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

    The following code prints the result of your captcha image

    ```
    image_base64 = image_to_base64('YOUR_CAPTCHA_IMAGE_PATH')  # ****CHANGE HERE WITH YOUR VALUE*******
    captcha_rsponse = image_captcha(image_base64)
    print(captcha_rsponse)
    ```


   - **ReCaptcha V2**

     To obtain a token, replace the placeholders "site_url" and "site_key" in the following code with the actual values of your site's URL and site key
    
      ```
      site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
      site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******
      rev2_response = reCAPTCHAV2(url=site_url, site_key=site_key)
      ```
      
      **Notice:**
      If you receive a status_code of 201 and a 'False' result, you should wait for 10 seconds and then retry the operation.



   - **ReCaptcha V3**

      In the following code, replace your "site_url" and "site_key" values with your actual values to obtain a token

      ```
      # call reCAPTCHA v2 API
      site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
      site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******
      rc3 = reCAPTCHAV3(url=site_url, site_key=site_key)
      print(rc3)
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
   | 401	        |  Error   | your access token expired, create another application|

 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

