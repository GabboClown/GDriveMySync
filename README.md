# Google Cloud MySync

## Project Purpose
This project aims to sync a remote Google Drive folder to your device.

## Program Setup

### 1. Google Cloud Console Setup
First, you need to create an app on Google Cloud Console to access your Google Drive API. Follow this tutorial by Google to get started: [Google Cloud API Setup](https://developers.google.com/workspace/guides/get-started).

### 2. Install dependencies
To install the needed dependencies, run 
```bash 
pip install -r dependencies.txt
```
you can delete the file later.


### 3. Create `.env` File
Next, create an `.env` file by following the structure of `.env.example`. This file will store the required credentials for accessing your Google Drive API.

### 4. Fill the Variables
Inside the `.env` file, you will need to provide the following variables: `CLIENT_SECRET`, `CLIENT_ID`

- Fill in the `CLIENT_ID` and `CLIENT_SECRET` with the values from your Google Cloud project.
- Set the `REDIRECT_URI` to a URI of your choice (for example, `localhost` works fine).

### 5. Run the Code
After setting up the environment variables, run the following command to start the sync:

```bash
python GDriveMySync.py
```

### 6. Help command
If you need any help, run
```bash
python GDriveMySync.py -h
```
or
```bash
python GDriveMySync.py -help
```
