# import sqlite3
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM events WHERE band='tigers'")
# result = cursor.fetchall()
# print(result)
#
# cursor.execute("SELECT band,date FROM events WHERE band='tigers'")
# result = cursor.fetchall()
# print(result)
#
# # inserting new rows
# new_rows = [('cats', 'kochi', '2025.10.15'), ('dog', 'amz', '2025.11.14')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
# connection.commit()
