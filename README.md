# Google Cloud MySync

## Project purpose
This project aims to sync a remote Google Drive folder to your device

## Program setup
First thing first, create an app on Google Cloud Console to access your Google Drive API. You can follow [this] (https://developers.google.com/workspace/guides/get-started) tutorial made by Google on this topic.
Next, create an ```.env``` file following the ```.env.example```.
Then, fill the empty variables, such as ```CLIENT_ID``` and ````CLIENT_SECRET```.
Your ```.env``` file will look something like this:
```
CLIENT_ID = 
CLIENT_SECRET = 
AUTH_URI =  "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
REDIRECT_URI = 
SCOPE = "https://www.googleapis.com/auth/drive"
```
Of course, fill the ```REDIRECT_URI``` field by inserting the redirect_uri of your choice (localhost works just fine).
That's it! Now run the code with
```python GDriveMySync.py``` 
If you need help with anything, run
```python GDriveMySync.py -h``` or ```python GDriveMySync.py -help```