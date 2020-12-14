"""
This program completes exercise #7.1 in chapter 17 of the class textbook.
A simple '~~~~~' has been put in between each print command to separate
the output.

Name: Randy
"""

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

# Create a cursor to execute future queries.
cursor = connection.cursor()

pd.options.display.max_columns = 10

# Sort the authors by descending order of last name.
print(pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection))
print("~~~~~")

# Sort the book titles by ascending order.
print(pd.read_sql("SELECT title FROM titles ORDER BY title", connection))
print("~~~~~")

# Display the title, copyright, and ISBN # of the author with ID 1 (Paul Deitel)
print(pd.read_sql("""SELECT title, copyright, author_ISBN.isbn FROM authors 
                  INNER JOIN author_ISBN ON authors.id = author_ISBN.id
                  INNER JOIN titles ON author_ISBN.isbn = titles.isbn
                  WHERE authors.id = 1
                  ORDER BY title""",
                  connection))
print("~~~~~")

# Create a new author (with auto-assigned ID 6): Randy Ha
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Randy', 'Ha')""")

# Display the updated table of authors.
print(pd.read_sql('SELECT * FROM authors', connection))
print("~~~~~")

# Insert a new book with ISBN 0123456789 and author ID 6 into the author_ISBN
# and titles tables. 
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                        VALUES ('6', '0123456789')""")
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                        VALUES ('0123456789', 'How To: Cure World Hunger',
                                '1', '2020')""")

# DIsplay the updated results.
print(pd.read_sql('SELECT * FROM author_ISBN WHERE id = 6', connection))
print("~~~~~")

print(pd.read_sql("SELECT * FROM titles WHERE isbn = '0123456789'", connection))
print("~~~~~")

# Close the connection to the database.
connection.close()