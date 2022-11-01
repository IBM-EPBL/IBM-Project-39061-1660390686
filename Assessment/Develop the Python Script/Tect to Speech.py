Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ibm_watson import TextToSpeechV1
... from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
... import playsound
... 
... authenticator = IAMAuthenticator('v9n8Zn4r5VpcMVz_HyRY0DrS13jSzph2IEFioVj4-vmT')
... text_to_speech = TextToSpeechV1(
...     authenticator=authenticator
...     )
... 
... text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm')
... 
... with open('alert.mp3', 'wb') as audio_file:
...     audio_file.write(
...         text_to_speech.synthesize(
...             'Alert! Alert! Animal Detected.',
...             voice='en-US_ALLisonV3Voice',
...             accept='audio/mp3'
...             ).get_result().content)
