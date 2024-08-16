# Respostas do laboratório Troubleshooting Common SQL Errors with BigQuery (Como solucionar problemas comuns de SQL com o BigQuery)

## Tarefa 2: encontrar o número total de clientes que concluíram uma compra

### What's wrong with the previous query to view 1000 items?
- There is a typo in the dataset name
- ***We have not specified any columns in the SELECT***
- ***There is a typo in the table name***
- We are using legacy SQL

### What's wrong with the new previous query to view 1000 items?
- There is a typo in the dataset name
- ***We are using legacy SQL***
- We have not specified any columns in the SELECT
- There is a typo in the table name

### What is wrong with the previous query?
- SELECT clause is returning all columns which leads to poor performance
- We are still using legacy SQL
- ***Still no columns defined in SELECT***
- We are missing an ORDER BY clause

### What is wrong with the previous query?
- We are missing a LIMIT clause
- ***Without aggregations, limits, or sorting, this query is not insightful***
- We are missing a column alias
- ***The page title is missing from the columns in SELECT***

### How many columns will the previous query return?
- ***1, a column named hits_page_pageTitle***
- 3 columns will be returned since we are missing a comma
- 2, columns named fullVisitorId and hits_page_pageTitle
- 0, the query will return an error

### What is wrong with the previous query?
- ***It is missing a GROUP BY clause***
- A COUNT() function is used when SUM() should be used instead
- Nothing, it executes correctly
- ***The COUNT() function does not de-deduplicate the same fullVisitorId***

## Tarefa 3: listar as cidades com mais transações no site de e-commerce

### Which city had the most distinct visitors? Ignore the value: 'not available in this demo dataset'
- ***Mountain View***
- San Jose
- Los Angeles
- Austin

### What is wrong with the previous query?
- You cannot divide non-similar aggregate functions
- ***You cannot filter on aliased fields within the `WHERE` clause***
- Nothing, it executes correctly
- ***You cannot filter aggregated fields in the `WHERE` clause (use `HAVING` instead)***

## Tarefa 4: encontrar o número total de produtos em cada categoria

### What is wrong with the previous query?
- ***No aggregate functions are used***
- There is a typo in the column name
- ***Large GROUP BYs really hurt performance (consider filtering first and/or using aggregation functions)***
- Nothing, it executes correctly

### What is wrong with the previous query which lists products?
- Nothing, the query executes correctly
- ***The COUNT() function is not the distinct number of products in each category***
- The GROUP BY contains an incorrect column
- The WHERE clause should include NULL Product Names

### Which category has the most distinct number of products offered?
- Electronics
- Office
- ${productitem.product.origCatName}
- ***(not set)***

