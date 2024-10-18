import json

class Configurator:
    @staticmethod
    def config():
        link = input("Insert the link of the folder you want to sync onto your device: ")

        splittedLink = link.split('/')
        # The folderID is located after the 'folders' path, so the index of 'folders' is found
        # to get the folderID
        folderID = splittedLink[splittedLink.index('folders') + 1]
        localPath = input("Now, insert the full path of the folder you want to sync to: ")

        config = {
            'folderID':folderID,
            'localPath':localPath
        }
        with open('config.json', 'w') as f:
            f.write(json.dumps(config))
        
        print("\nGreat, you've successfully configured the application!")
        print(f"The data you've given the application is:\n\tRemote folder ID: \"{folderID}\"\n\tLocal folder path: \"{localPath}\"")

    @staticmethod
    def seeSettings():
        with open('config.json', 'r') as f:
            config = json.loads(f.read())
        
        print(f"The data you've given the application is:\n\tRemote folder ID: \"{config["folderID"]}\"\n\tLocal folder path: \"{config["localPath"]}\"")
        print("Use \"python GDriveMySync.py -c\" to change the configurations")
