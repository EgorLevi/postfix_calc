import sqlite3

db = sqlite3.connect("history.db")
cursor =  db.cursor()

def create_database():
    cursor.execute("""CREATE TABLE If NOT EXISTS calcs(input_text TEXT, result TEXT)""")
    db.commit()
    return

def add_new_data(input_text, result):
    cursor.execute("INSERT INTO calcs VALUES(?, ?)", (input_text, result))
    db.commit()
    return

def show_all_data():
    a = cursor.execute("SELECT * FROM calcs").fetchall()
    print(a)
    return a

#create_database()
#add_new_data("test input text", "test result")
#show_all_data()

