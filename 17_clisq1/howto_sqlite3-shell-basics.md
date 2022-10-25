# how-to :: Use sqlite3
---
## Overview
sqlite3 enables use to set up databases to organize our data.

### Estimated Time Cost: 0.5 hrs

### Prerequisites:

- Data
- Terminal Session

1. Open an sqlite session by typing
```
sqlite3 name
```
into the terminal.
Notes:
- If the file named exists, it will be opened as an sqlite3 database.
- If the named file does not exist, a new file with the specified name will be created.
  - sqlite3 files are NOT human readable when cat'ed, so open them via sqlite3 to see their contents.
- Creating a table with no name creates a temporary database, which is deleted once you terminate the sqlite3 session.
- Opening the file and then using the command ```.databases``` will display the path to the file.

2. Create a table by typing
```
create table name (value1, value2);
```
Notes:
- name can be replaced with whatever you want to name the table.
- As many values can be specified in each entry as needed, and their types do not have to be declared, but they CAN be.
  - Values can be typed by putting a space and the variable type (ie: TEXT, INT, FLOAT, char) after the value name.
    - A list of sqlite3 data types: (https://www.sqlite.org/datatype3.html)
  - If a value is not typed, any data type can be stored under it without issue.
  - Even if a value is typed, the are still few restrictions as to what data types can actually be stored under it.

3. Add a value to a table by typing
```
insert into table_name values(value1, value2);
```
OR
Add a column to a table by typing
```
ALTER TABLE table_name
add new_column_name column_definition;
```
Notes:
- As previously mentioned, values with no specified type can have any data types stored under them without incident.
- Values with specified data types can still accept many different kinds of data types.
- A value MUST be provided for every column with each entry, but a column can be filled by NULL.
- Adding a column will require that all future entries have a value for the new column, but will not modify old entries.

4. To delete a table, type
```
drop table table_name;
```
Notes:
- Although entire tables can be deleted from databases, individual columns from tables cannot be.


### Resources
* sqlite data types: (https://www.sqlite.org/datatype3.html)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Flying Karate Masters:
Matthew Yee, pd7  
Joseph Wu, pd7  
Kevin Li, pd7  
