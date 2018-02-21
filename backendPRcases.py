import sqlite3

class Database:

    def __init__(self):
        self.conn=sqlite3.connect("cases.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cases (id INTEGER PRIMARY KEY, location TEXT, name TEXT, year INTEGER, casenumber INTEGER) ")
        self.conn.commit()

    def insert(self,location, name, year, casenumber):
        self.cur.execute("INSERT INTO cases VALUES (NULL,?,?,?,?)",(location, name, year, casenumber))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM cases")
        rows=self.cur.fetchall()
        return rows

    def search(self,location="",name="",year="",casenumber=""):
        self.cur.execute("SELECT * FROM cases WHERE location=? OR name = ? OR year= ? OR casenumber= ?",(location, name, year, casenumber))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM cases WHERE id= ?",(id,))
        self.conn.commit()

    def update(self,id,location,name,year,casenumber):
        self.cur.execute("UPDATE cases SET location= ?, name= ?, year= ?, casenumber=? WHERE id =?",(location, name, year, casenumber, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
