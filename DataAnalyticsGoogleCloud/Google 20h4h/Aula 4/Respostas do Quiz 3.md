# Respostas do Quiz 3 - Leveraging Data

### 1.What types of data sources are supported by AppSheet? (Select 2)
- IoT (Internet-of-things) devices
- ***Databases***
- check Spreadsheets

### 2.Which statements about the key column of a table that is used in AppSheet are correct? (Select 2)
- Values that are stored in a key column of a table must be numeric.
- It is acceptable for two or more rows in a table to have the same value in the key column. (duplicate keys)
- A key column is always optional in a table.
- ***Any table used in AppSheet must define a key column.***
- ***The value in a key column uniquely identifies each row in the table.***

### 3.What is a virtual column in AppSheet?
- It is a temporary column that is added to the underlying data source for use by AppSheet.
- It is a column that can only be added by the system and not by the app creator.
- It is a column that must have a type explicitly set when the column is created.
- ***It is a column that is usually populated using an app formula.***

### 4.What are some characteristics of AppSheet table references? (Select 2)
- ***A reference is a relationship between related tables that use a column of type Ref in one table that contains a value from a key column of a related row in the other table.***
- Only the app creator can create references when building an app.
- References are unidirectional, so an app can only traverse data from the table that contains the Ref column to the referenced table.
- ***A reference enables the app to easily retrieve information from a related row in another table.***
- A table that is used in AppSheet must contain at least one reference.
