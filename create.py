from firebase_admin.auth import create_user

import auth
import json

# To create user

user = create_user(
    email='priyanshjha@gmail.com',
    email_verified=False,
    phone_number='+911234567891',
    password='priyanka1234',
    display_name='Ritesh',
    disabled=False)
print('Sucessfully created new user: {0}'.format(user.uid))


