class HelpAccessor:
    @staticmethod
    def access() -> str:
        return """
usage: python GDriveMySync.py [OPTION]

Available options:
-h, -help                            Shows this message.
-c, -config                          Starts config procedure.
-s, -settings                        Shows settings.

Use cases:
python GDriveMySync.py -h            Shows this message.
python GDriveMySync.py -help         Shows this message.
python GDriveMySync.py -c            Starts config procedure.
python GDriveMySync.py -config       Starts config procedure.
python GDriveMySync.py -s            Shows settings.
python GDriveMySync.py -settings     Shows settings.
python GDriveMySync.py               Starts the program with settings in config.json.
"""