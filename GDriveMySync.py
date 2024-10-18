from autoload import *

if __name__ == "__main__":
    ARGV = sys.argv
    ARGV_CONSTANTS = {
        'help': ['-h', '-help'],
        'config': ['-c', '-config'],
        'settings': ['-s', '-settings']
    }

    driveRepository = ServiceContainer.get("DriveRepository")

    # Checks if there's an option argument
    if len(ARGV) > 1:
        if ARGV[1] in ARGV_CONSTANTS['help']:
            print(HelpAccessor.access())
            exit()
        elif ARGV[1] in ARGV_CONSTANTS['config']:
            Configurator.config()
            exit()
        elif ARGV[1] in ARGV_CONSTANTS['settings']:
            Configurator.seeSettings()
            exit()
    else:
        if not os.path.exists('config.json'):
            Configurator.config()
            exit()

        with open("config.json", 'r') as f:
            CONFIG = json.loads(f.read())
        
        files = driveRepository.listFilesInFolder(CONFIG["folderID"], "id")
        for file in files:
            driveRepository.fileDownload(file["id"], CONFIG["localPath"])
