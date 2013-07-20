try:
	import sqlite3
	import os
	import sys
	import time
	import base64
	import hashlib
	from os import curdir, sep
	from time import strftime, gmtime
except Exception as e:
	print("IMPORT ERROR: %s" % e)

def create():
    """Create and set up the database file."""
    
    try:
        os.mkdir((os.getcwd() + '/database'))
        print("Created: /database")
    except Exception as e:
        print(e)
        
    try:
        con = sqlite3.connect((os.getcwd() + '/database/centralSQL.db'))
        print("Created: /database/centralSQL.db")
    except Exception as e:
        print(e)
        
    try:
        cur = con.cursor()
    except Exception as e:
        print(e)
        
    try:    
        cur.execute("""CREATE TABLE content
                            (date, user, post)""")
        print("Created: TABLE content")
    except Exception as e:
        print(e)
        
    try:            
        cur.execute("""CREATE TABLE datastore_user
                            (date, username, password)""")
        print("Created: TABLE datastore")
    except Exception as e:
        print(e)
    
    try:    
        cur.execute("""CREATE TABLE amounts
                            (file, visit, error, log, posts, users)""")
        print("Created: TABLE amounts")
    except Exception as e:
        print(e)
        
    try:
        with con:
            cur.execute("INSERT INTO amounts VALUES(0,0,0,0,0,0)")
        print("Inserted amounts")
    except Exception as e:
        print(e)

class Credentials:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		del username, password
		self.encode()

	def encode(self):
		"""Encode the credentials to base64."""
		self.encoded_username = self.username
		self.encoded_password = self.password
		try:
			self.encoded_username = base64.b64encode(self.encoded_username)
			self.encoded_password = base64.b64encode(self.encoded_password)
		except Exception as e:
			sys.stderr.write("EXCEPTION WHILE ENCODING: %s\n" % e)

		print("FINAL")
		print(self.encoded_username)
		print(self.encoded_password)
		self.decode()

	def decode(self):
		"""Decode base64 encodings."""
		self.decoded_username = self.encoded_username
		self.decoded_password = self.encoded_password
		try:
			self.decoded_username = base64.b64decode(self.decoded_username)
			self.decoded_username = base64.b64decode(self.decoded_username)
		except Exception as e:
			sys.stderr.write("EXCEPTION WHILE DECODING: %s\n" % e)
		print("FINAL")
		print(self.encoded_username)
		print(self.encoded_password)



if __name__ ==  "__main__":
	#create()
	instance = Credentials(b"admin", b"adminpassword")