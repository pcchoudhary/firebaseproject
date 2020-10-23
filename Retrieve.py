import json

# To get(retrieve) user data -

from firebase_admin import auth

user = auth.get_user_by_email('priyankaritshjha@gmail.com')
jsonStr = json.dumps(user.__dict__)  # method of Convert Class Object to JSON so that we can get full data of user.
print('Successfully fetched user data:')
print(jsonStr)