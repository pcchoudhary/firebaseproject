from firebase_admin.auth import update_user

import auth

# To delete user record

user = update_user(
    'EES2Pxck9ta0GazGsKxHQYGpBQy1',
    email='priyankaritshjha@gmail.com',
    email_verified=False,
    phone_number='+918374638046',
    password='priyanka1234',
    display_name='priyanka',
    disabled=True)
print('Sucessfully updated user: {0}'.format(user.uid))