"""
This program completes the exercise shown on Section 17.2 in the book.
A simple '~~~~~' is inserted between each print statement to make separation
clearer.

Name: Randy
"""

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10

## SELECT statement.
# Display all the rows from table authors in the database, ordered by the id.
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))
print("~~~~~")

# Display the table titles.
print(pd.read_sql('SELECT * FROM titles', connection))
print("~~~~~")

# Create a new DataFrame from the contents of the table author_ISBN.
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(df.head())
print("~~~~~")

# Display the full name of all the authors in the authors table.
print(pd.read_sql('SELECT first, last FROM authors', connection))
print("~~~~~")


## WHERE statement.
# Display all titles in the table titles newer than 2016.
print(pd.read_sql("""SELECT title, edition, copyright FROM titles
            WHERE copyright > '2016'""", connection))
print("~~~~~")

# Display all the authors with a last name beginning with D.
print(pd.read_sql("""SELECT id, first, last FROM authors
            WHERE last LIKE 'D%'""", connection, index_col=['id']))
print("~~~~~")


## ORDER BY statement.
# Display all titles in ascending order of title.
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print("~~~~~")


# Display all the authors in the database in ascending order of their last name,
# then of their first name.
print(pd.read_sql("""SELECT id, first, last FROM authors
            ORDER BY last, first""", connection, index_col=['id']))
print("~~~~~")
   
# Display all authors like last time, but sort by last names Descending
# and the first names Ascending after that.
print(pd.read_sql("""SELECT id, first, last FROM authors
            ORDER BY last DESC, first ASC""", connection, index_col=['id']))
print("~~~~~")

# Display all the books in the database ending with "How to Program" and
# ordered by title.
print(pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles
            WHERE title LIKE '%How to Program'
            ORDER BY title""", connection))
print("~~~~~")


## INNER JOIN statement.
# Join the author_ISBN and authors tables and display all the authors' full names
# and ISBN's sorted by last and then first name.
print(pd.read_sql("""SELECT first, last, isbn FROM authors
            INNER JOIN author_ISBN ON authors.id = author_ISBN.id
            ORDER BY last, first""", connection).head())
print("~~~~~")

## INSERT INTO statement.
# Create a cursor object to access rows and columns of the database.
cursor = connection.cursor()

# Insert a new name into the authors table: Sue Red.
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Sue','Red')""")

# Display the new authors table.
print(pd.read_sql('SELECT id, first, last FROM authors', connection,
                  index_col=['id']))
print("~~~~~")


## UPDATE statement.
# Update the row containing the name Sue Red to change the name to Sue Black.
cursor = cursor.execute("""UPDATE authors SET last='Black'
                        WHERE last='Red' AND first='Sue'""")

# Display the cursor.rowcount field that shows how many rows were updated.
print(cursor.rowcount)
print("~~~~~")

# List the new authors table.
print(pd.read_sql('SELECT id, first, last FROM authors', connection,
                  index_col=['id']))
print("~~~~~")


## DELETE FROM statement.
# Delete the row that has id 6.
cursor = cursor.execute('DELETE FROM authors WHERE id=6')

# Display the rowcount again to show how many rows were modified.
print(cursor.rowcount)
print("~~~~~")

# Display the new table.
print(pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id']))
print("~~~~~")


## EXERCISE 1
# Select the titles and edition columns from the table titles and sort
# in descending order by edition. Then, display the 3 first results.
print(pd.read_sql('SELECT title, edition FROM titles ORDER BY edition DESC',
            connection).head(3))
print("~~~~~")


## EXERCISE 2
# Select all authors from table authors whose name starts with A.
print(pd.read_sql("SELECT * FROM authors WHERE first LIKE 'A%'", connection))
print("~~~~~")


## EXERCISE 3
# Select all titles from table titles where the title does not end with the
# phrase "How to Program".
print(pd.read_sql("""SELECT * FROM titles
                  WHERE title NOT LIKE '%How to Program'""", connection))
print("~~~~~")

# Close connection to database.
connection.close()