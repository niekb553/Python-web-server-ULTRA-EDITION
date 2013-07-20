try:
    import sys
    import os
    import sqlite3
    import base64
    from configparser import SafeConfigParser
    try:
        sys.path.insert(0, (os.getcwd()+"/modules"))
    except exception as e:
        print("Exception while importing from /module: %s" % e)
    import database
except Exception as e:
    print("EXCEPTION WHILE IMPORTING: %s" % e)

class SettingsParser:

    def __init__(self):
        self.parser = SafeConfigParser()
        self.parser.read("settings.cfg")
        self.read_all()

    def read_all(self):
        for section_name in parser.sections():
            print("\nSection: %s" % section_name)
            print("Options: %s" % parser.options(section_name))
            for name, value in self.parser.items(section_name):
                print("%s = %s" % (name, value))		


class Database:
    def __init__(self):
        self.path = (os.getcwd()+"/database/centralSQL.db")
        


if __name__ == "__main__":
    #parser = SettingsParser()
    database.create()
            
