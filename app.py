import mysql.connector
from difflib import get_close_matches

def Connect_To_Database(host_name, database_name, username, passw):
    conn = mysql.connector.connect(
        user = username,
        password = passw,
        host = host_name,
        database = database_name
    )
    return conn

def Get_Definition(word):
    ##cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()
    if results:
        for item in results:
            print(item[1])
    else:
        cursor.execute("SELECT DISTINCT Expression, Definition FROM Dictionary")
        results = cursor.fetchall()
        expressions = [item[0] for item in results]
        close_matches = get_close_matches(word, expressions, 4)
        for item in close_matches:
            yn = input(f"Did you mean {item}? Enter Y or N: ").lower()
            if yn == 'y':
                cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{item}'")
                results = cursor.fetchall()
                for item in results:
                    print(item[1])
            elif yn == 'n':
                continue
            else:
                print("I didn't understand that command.")

conn = Connect_To_Database("108.167.140.122", "ardit700_pm1database", "ardit700_student", "ardit700_student")

cursor = conn.cursor()

word = input("Enter a word: ")
Get_Definition(word)