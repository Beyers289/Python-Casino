import _sqlite3 
import bcrypt

# database.py
class CasinoDatabase:
    def __init__(self, db_path='python_casino.db'):
        self.db_path = db_path
    
    def create_user(self, username, password):
        with _sqlite3.connect(self.db_path) as conn:
            #Bcrypt hashing takes in the password encoded into bytes string then the salt which is a random data using in the hasing function
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            c = conn.cursor()
            try:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                return True
            except:
                return False
    def validate_user(self, username, password):
        with _sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = c.fetchone()
            if result:
                #password matching with the Bcrypt checking password method
                return bcrypt.checkpw(password.encode('utf-8'), result[0])
            return False
    
    def get_gambler(self, username):
        with _sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT balance, username, user_id FROM gamblers WHERE username = ?", (username,))
            result = c.fetchone()
            return result if result else (0, username, None)
    
    def update_gambler_balance(self, user_id, new_balance):
        with _sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("UPDATE gamblers SET balance = ? WHERE user_id = ?", (new_balance, user_id))

# Global instance for convenience
db = CasinoDatabase()


'''
Users Table
Primary KEY(ID) username password
example insert #c.execute("INSERT INTO users (username, password) VALUES ('Test2', 'Password')")

Gamblers Table
FOREIGN KEY(USERS(ID)) Username Balance


CREATED TRIGGER create_gambler_after_user
after each insert into users creates a gambler insert with the ID foreign key and the user name from the insert a default balance of 0
'''


'''
Datatypes
INTEGER
TEXT
NULL
REAL aka Float
BLOB aka imgs mp3

'''
