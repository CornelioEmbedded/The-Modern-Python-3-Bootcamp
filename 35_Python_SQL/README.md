# 35 - Python + SQL

Work with SQLite3

To run sqlite3 in temrinal, it needs this command:
```cmd
set PATH=%PATH%;C:\sqlite;
```
- Create table

```sql
CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);
```

- Inserting
```sql
INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish",3);
```

- Selecting
```sql
SELECT * FROM dogs WHERE name IS *"Piggy"*;
```
- Connecting SQLite3 with Python
```python
import sqlite3

conn = sqlite3.connect("my_friends.db")
# CREATE CURSOR OBJECT
c = conn.cursor()
# EXECUTE SOME SQL
c.execute(CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)
# COMMIT CHANGES
conn.commit()
conn.close()
```
