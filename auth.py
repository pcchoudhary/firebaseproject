import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json

from google.oauth2 import id_token

cred = credentials.Certificate("config\learning-6044c.json") #cred is json file which is in config folder which we downloaded fromm google console settings.
default_app = firebase_admin.initialize_app(cred)

# #create token id -
uid = 'EES2Pxck9ta0GazGsKxHQYGpBQy1'
custom_token = auth.create_custom_token(uid)
print(custom_token)

# verify token ID -

decoded_token = auth.verify_id_token(str(custom_token),'learning-6044c')
#uid = decoded_token['EES2Pxck9ta0GazGsKxHQYGpBQy1']
print(decoded_token)