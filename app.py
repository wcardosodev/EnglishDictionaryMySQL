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
        #for item in results:
            #print(item[1])
        return results
    else:
        #cursor.execute("SELECT DISTINCT Expression, Definition FROM Dictionary")
        cursor.execute("SELECT DISTINCT Expression FROM Dictionary")
        results = cursor.fetchall()
        expressions = [item[0] for item in results]
        close_matches = get_close_matches(word, expressions, 4)
        for item in close_matches:
            yn = input(f"Did you mean {item}? Enter Y or N: ").lower()
            if yn == 'y':
                cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{item}'")
                results = cursor.fetchall()
                #for item in results:
                    #print(item[1])
                return results
                #break
            elif yn == 'n':
                continue
            else:
                return "I didn't understand that command. \n"
        return "Couldn't find that word."

def Format_Definitions(def_list):
    for item in def_list:
        print(item[1])

conn = Connect_To_Database("108.167.140.122", "ardit700_pm1database", "ardit700_student", "ardit700_student")

cursor = conn.cursor()

print("""
Welcome to Will's online dictionary.
Enter a word and I'll give you any and all definitions for it.
When you are done type 'Exit' to quit.doc
Have fun!
""")

while True:
    word = input("Enter a word: ")
    word = word.lower()
    if word != 'exit':
        definitions = Get_Definition(word)
        if isinstance(definitions, str):
            print(definitions)
        else:
            Format_Definitions(definitions)
        print(" ")
    else:
        print("Thank you for using me, see you soon.")
        break