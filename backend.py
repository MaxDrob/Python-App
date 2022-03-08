import sqlite3

def connect ():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, bookstack integer, shelf integer)")
    conn.commit()
    conn.close()


def insert(title,author,bookstack,shelf):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)",(title,author,bookstack,shelf))
    conn.commit()
    conn.close()


def view():
   conn=sqlite3.connect("books.db")
   cur=conn.cursor()
   cur.execute("SELECT * FROM book")
   rows=cur.fetchall()
   conn.close()
   return rows

def search(title="",author="",bookstack="",shelf=""):
   conn=sqlite3.connect("books.db")
   cur=conn.cursor()
   cur.execute("SELECT * FROM book WHERE title=? OR author=? OR bookstack=? OR shelf=?", (title,author,bookstack,shelf))
   rows=cur.fetchall()
   conn.close()
   return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,bookstack,shelf):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, bookstack=?, shelf=? WHERE id=?", (title,author,bookstack,shelf,id))
    conn.commit()
    conn.close()

connect()
#insert("Бестолковый словарь", "Ожегов",2,1)
#delete(5)
#update(6,"Еще один словарь","Обжогов",2,1)
#print(view())
print(search(title="Бестолковый словарь"))