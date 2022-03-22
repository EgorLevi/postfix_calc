import sqlite3

connection = sqlite3.connect("history.db")
cursor = connection.cursor()
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS calcss(input TEXT, result TEXT)""")
    connection.commit()
    return

def insert_calc(expersion, result):
    try:
        cursor.execute(f"""INSERT INTO calcss VALUES({expersion},{result})""")
        connection.commit()
    except:
        create_table()
        cursor.execute(f"""INSERT INTO calcss VALUES(?,?)""", (expersion, result))
        connection.commit()
    return


def show_history():
    print(cursor.execute("""SELECT * FROM calcss""").fetchall())

insert_calc("asd", "4")
show_history()
