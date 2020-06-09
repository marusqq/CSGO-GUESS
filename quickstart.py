# from pydrive.auth import GoogleAuth

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()

from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
print(auth_url)
