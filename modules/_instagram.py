import instaloader

cursor = instaloader.Instaloader()

def downloadProfile(username):
    cursor.download_profile(username)

def userId(username):
    cursor.check_profile_id(username)