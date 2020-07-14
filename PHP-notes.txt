Places to look at for PHP tips and learning:
    -https://www.w3schools.com/sql/ 



Common Commands (It is good practice to use all caps, and also end each statement with a ';':

SELECT - extracts data from a databt, and click "Run SQL" to see the result.
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index

Details on specific commands:

SELECT:
    Syntax: 
            SELECT column1, column2, ... FROM table_name;
            (Where you are selecting column 1 and column 2 from the database table_name)SELECT CustomerName, City FROM Customers;
            
            SELECT * FROM table_name; 
            (To select all in a table/database)
            
    Uses:
            Simply selects the requested columns to be manipulated.

    Example:
            SELECT CustomerName, City FROM Customers;
            (Where you are selecting all of the data from CustomerName and City from the table Customers)

SELECT DISTINCT:
    Syntax:
            SELECT DISTINCT column1, column2, ... FROM table_name;SELECT CustomerName, City FROM CusSELECT CustomerName, City FROM Customers;tomers;
            (where you are selectig unique iterations from column 1 and column 2 from the database table_name)

            SELECT DISTINCT * FROM table_name;
            (To select all unique values in a table/database)SELECT CustomerName, City FROM Customers;
    Uses: 
            To selet unique iterations from a database, and also prevents duplicate data.

    Example:
            SELECT DISTINCT Country FROM Customers;
            (Where you are selecting distinct values from the column Country in the table Customers.)

WHERE

    Syntax:
            SELECT column1, column2, ... FROM table_name WHERE condition; 
            (Where you are selecting data from the columns while meeting set criteria)
            
    Uses: 
            To add some logic to the process, and this can allow for some easier sorting of data

    Example:
            SELECT * FROM Customers WHERE Country='Mexico';
            (Select all data from the table Customers that in the column Country has Mexico)Places to look at for PHP tips and learning:
    -https://www.w3schools.com/sql/ 



Common Commands (It is good practice to use all caps, and also end each statement with a ';':

SELECT - extracts data from a databt, and click "Run SQL" to see the result.

Update Readme.md
4 hours ago
ase
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index

Details on specific commands:

SELECT:
    Syntax: 
            SELECT column1, column2, ... FROM table_name;
            (Where you are selecting column 1 and column 2 from the database table_name)SELECT CustomerName, City FROM Customers;
            
            SELECT * FROM table_name; 
            (To select all in a table/database)
            
    Uses:
            Simply selects the requested columns to be manipulated.

    Example:
            SELECT CustomerName, City FROM Customers;
            (Where you are selecting all of the data from CustomerName and City from the table Customers)

SELECT DISTINCT:
    Syntax:
            SELECT DISTINCT column1, column2, ... FROM table_name;SELECT CustomerName, City FROM CusSELECT CustomerName, City FROM Customers;tomers;
            (where you are selectig unique iterations from column 1 and column 2 from the database table_name)

            SELECT DISTINCT * FROM table_name;
            (To select all unique values in a table/database)SELECT CustomerName, City FROM Customers;
    Uses: 
            To selet unique iterations from a database, and also prevents duplicate data.

    Example:
            SELECT DISTINCT Country FROM Customers;
            (Where you are selecting distinct values from the column Country in the table Customers.)

WHERE

    Syntax:
            SELECT column1, column2, ... FROM table_name WHERE condition; 
            (Where you are selecting data from the columns while meeting set criteria)
            
    Uses: 
            To add some logic to the process, and this can allow for some easier sorting of data

    Example:
            SELECT * FROM Customers WHERE Country='Mexico';
            (Select all data from the table Customers that in the column Country has Mexico)
