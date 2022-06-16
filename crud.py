# Class to perform user CRUD operations on the sqlte database
import sqlite3

class CRUD:
    def __init__(self):
        self.db = self.connect()
        self.c = self.db.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS USERS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT);""")
        self.db.commit()
    
    def connect(self):
        return sqlite3.connect("users.db")
    
    def create(self, name, email):
        #check if user already exists
        self.c.execute("SELECT * FROM USERS WHERE email=?", (email,))
        if self.c.fetchone():
            print('-'*40)
            print("Account already exists !!!")
            print('-'*40)
        else:
            self.c.execute("INSERT INTO USERS (name, email) VALUES (?, ?)", (name, email))
            self.db.commit()
            print('-'*40)
            print("Account created successfully")
            print('-'*40)
          
    def read(self):
        self.c.execute("SELECT * FROM USERS")
        #display all users in a table
        print("ID\t\tName\t\tEmail")
        print("-"*50)
        for row in self.c.fetchall():
            print(row[0], "\t", row[1], "\t", row[2])
        # return self.c.fetchall()
    def read_emails(self):
        self.c.execute("SELECT email FROM USERS")
        return self.c.fetchall()

    def update(self, id, name, email):
        self.c.execute("UPDATE USERS SET name=?, email=? WHERE id=?", (name, email, id))
        self.db.commit()
        print('-'*40)
        print("Account updated successfully")
        print('-'*40)
    def delete(self, id):
        self.c.execute("DELETE FROM USERS WHERE id=?", (id,))
        self.db.commit()
        print('-'*40)
        print("Account deleted successfully")
        print('-'*40)
    def close(self):
        self.db.close()

class Registration:
    def __init__(self):
        self.db = self.connect()
        self.c = self.db.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS REGISTRATION (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            program TEXT);""")
        self.db.commit()
    
    def connect(self):
        return sqlite3.connect("users.db")
    
    def create(self, name, email, program):
        #check if user already registered for that program
        self.c.execute("SELECT * FROM REGISTRATION WHERE email=? AND program=?", (email, program))
        if self.c.fetchone():
            print('-'*40)
            print("User already registered for that program")
            print('-'*40)
        else:
            self.c.execute("INSERT INTO REGISTRATION (name, email, program) VALUES (?, ?, ?)", (name, email, program))
            self.db.commit()
            print('-'*40)
            print(name, " successfully registered for program ", program)
            print('-'*40)
    def read(self):
        #display all registered users in a table
        print("ID\t\tName\t\tEmail\t\tProgram")
        print("-"*70)
        self.c.execute("SELECT * FROM REGISTRATION")
        for row in self.c.fetchall():
            print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
        # return self.c.fetchall()
    def update(self, id, program):
        self.c.execute("UPDATE REGISTRATION SET program=? WHERE id=?", (program, id))
        self.db.commit()
        print('-'*40)
        print("User Registered Program updated successfully")
        print('-'*40)

    def delete(self, id):
        self.c.execute("DELETE FROM REGISTRATION WHERE id=?", (id,))
        self.db.commit()
        print('-'*40)
        print("User Registration deleted successfully")
        print('-'*40)
    def close(self):
        self.db.close()