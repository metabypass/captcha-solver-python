# MetaBypass-Python

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

 ------------------------------------------------------------------------------------------------------------------------


## There are 2 approaches for utilizing Metabypass-python:

1. Download the 'MetaBypass_Codes' folder and follow these steps for different types of Captchas:

    ### Text_Captcha ###
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


    ### ReCaptcha V2

    To obtain a token, replace the placeholders "site_url" and "site_key" in the following code with the actual values of your site's URL and site key
    ```
    # call reCAPTCHA v2 API
    site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
    site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******
    rev2_response = reCAPTCHAV2(url=site_url, site_key=site_key)
    ```
    #### Notice
    If you receive a status_code of 201 and a 'False' result, you should wait for 10 seconds and then retry the operation.


    ### ReCaptcha V3

    In the following code, replace your "site_url" and "site_key" values with your actual values to obtain a token

    ```
    # call reCAPTCHA v2 API
    site_url = "YOUR_SITE_URL"  # ****CHANGE HERE WITH YOUR VALUE*******
    site_key = "YOUR_SITE_KEY"  # ****CHANGE HERE WITH YOUR VALUE*******
    rc3 = reCAPTCHAV3(url=site_url, site_key=site_key)
    print(rc3)
    ```
2. To simplify the process, you can conveniently download the 'MetaBypass_Packages' folder, which includes separate Python packages for each captcha type, as well as accompanying test files. Here's a step-by-step guide:


   2.1. Start by downloading the 'MetaBypass_Packages' folder to a suitable location on your computer.

   2.2. Open your preferred command-line interface or terminal.

   2.3. Install the desired package for the specific captcha type you are interested in by executing the following command:
   ```
   pip install NAME_OF_PACKAGE
   ```

   2.4. Replace "NAME_OF_PACKAGE" with the actual name of the package you want to install.

 2.5. Once the installation is complete, navigate to the test files provided in the 'MetaBypass_Packages' folder. Run the test files associated with the installed package to evaluate and verify the functionality of the captcha-solving process.

