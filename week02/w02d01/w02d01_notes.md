# Week 2 Day 1 Notes

# Compass 

## PostgreSQL
[Postgres_Intro](https://www.postgresqltutorial.com/postgresql-getting-started/what-is-postgresql/)
* supports SQL (relational) and JSON (non-relational)
* postgres

### Common uses
* RDMS 
* robust database in lapp stack (linux, apache, postgres, php (python))
* general purpose transaction database - for apps and products
* geospatial database - for geographic information
* language support - many different 
* extensible - defines own data types, index, and functional languages
* used by many big companies


* When running Postgres queries in VScode, the file extension of your query file has to be .psql not .sql.


* host: lhl-data-bootcamp.crzjul5qln0e.ca-central-1.rds.amazonaws.com
* port: 5432
* user and pw: lhl_student 

* uses postgres (management tool) extension in VScode 
* add server on the left and "+" 
* will have different run query for SQL and Postgres

## Window Functions 
* performing functions/calculations accross columns for a single row
* can be value, ranking, aggregate 
[windowFunc](https://www.sqlitetutorial.net/sqlite-window-functions/)

* specified as with SELECT AVG(price) __OVER__ (PARTITION BY group_name)
    * each set of rows is a window
    * PARTITION BY distributes the rows of the result set into groups and the AVG() is applied to each group

* Diff syntax in PostgreSQL -
``` Postgres
window_function(arg1, arg2, ..) OVER (
    [PARTITION BY partition_expression]
    [ORDER BY sort_expression [ASC | DESC] [NULLS {FIRST | LAST}]
)
```
* partition by is optional - if not specified (group name) will do the whole set as one big partiiton

``` SQL
SELECT
    wf1() OVER(PARTITION BY c1 ORDER BY c2),
    wf2() OVER(PARTITION BY c1 ORDER BY c2)
FROM table_name;

/* Shortens the query can be done with one or more */
SELECT 
   wf1() OVER w,
   wf2() OVER w,
FROM table_name
WINDOW w AS (PARTITION BY c1 ORDER BY c2);
```
* aggregate functions link AVG, MIN, MAX, SUM, COUNT 
### Row/Rank/Dense_Rank
* use ROW_NUMBER(), RANK(), DENSE_RANK() to assign integer for each row based on order in the result test
* rank gives an ordered partition, same values - get assigned the same, will skip if doubled 
* dense_rank ranks have no gap, same gets the same rank, and next gets the next rank

### First/Last Value
* FIRST_VALUE(), LAST_VALUE() used to select max or min usually
* must specify unbounded RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

### Lag and Lead
* access data from previous or next row 
``` SQL
LAG  (expression [,offset] [,default]) over_clause;
LEAD (expression [,offset] [,default]) over_clause;
```
* expression - column, offset - number of rows to offset by
* default - if offset is beyond the scope of window
* can be used to calculate differences from current and previous row for example 


### Examples from SQL zoo
[WindowFuncs](https://sqlzoo.net/wiki/Window_functions)
``` SQL
SELECT yr,party, votes,
      RANK() OVER (PARTITION BY yr ORDER BY votes DESC) as posn
  FROM ge
 WHERE constituency = 'S14000021'
ORDER BY party,yr
/* Ranks each party for each year  */
``` 

* When nesting you need to assign an alias to the sub SELECT 
* e.g.
```SQL 
SELECT subject, MAX(salary_by_subject.avg_salary) AS max_salary
FROM (
    SELECT subject, AVG(monthly_salary) AS avg_salary
    FROM teachers
    GROUP BY subject) salary_by_subject;

/* Paired with a window function */
SELECT constituency, party
FROM (
SELECT constituency,party, votes, RANK() OVER (PARTITION BY constituency ORDER BY votes DESC) AS posn
FROM ge
WHERE constituency BETWEEN 'S14000021' AND 'S14000026'
AND yr  = 2017) edin_win
WHERE edin_win.posn = 1

/* another example */
SELECT party, COUNT(1)
FROM (SELECT constituency,party, votes, 
RANK() OVER (PARTITION BY constituency ORDER BY votes DESC) AS posn 
FROM ge
WHERE constituency LIKE 'S%'
AND yr  = 2017) q
WHERE q.posn = 1
GROUP BY party
```

## SQL in PYTHON 
* different packages can be used to access
* popular:
    * sqlite3 - for sql
    * psycopg2 - for postgreSQL
* other oeptions: SQLAlchemy, Pyodbc Turbodbc
* turbodbc is fastest - good for pulling and inserting huge amount of data
* all installed through conda
* see ipynb for using sqlite3

[turbodbc](https://turbodbc.readthedocs.io/en/latest/pages/getting_started.html)


---------------------------------------------------------

# Lecture Notes
* database makes sure everything is clean
* don't have to access locally, centralized, integration with software tools

* SQL - a type of programming language, common format
<br> 

* NoSQL databases
    * retrieved in other ways, not relational database, less structured 
    * mongoDB, more like JSON 
    * mongodb.com/nosql-explained

* Challenges when writing in SQL
    * declarative - no control flow vs python which is imperative and goes line by line
    * can end up having long, nested queries
    * harder to debug
    * w3schools.com/sql/ for reviewing fundamentals

* Database schemas
    * Star or Snowflake 
    * mostly job of data engineers
    * for analysts - more redundancies to get it easier
    * look at ERD, MYSQL workbench usually does it, can do it manually 
    * fact table - contains the most uniques? 

* Star Schema
    * one central linked to many
    * one fact table with linked to dimension tables

* Snowflake 
    * one fact table, with dimension tables but also linked dimension tables together 
    * more efficient and nonrepeating 


### RDBMS 
* stores data - converts SQL
* SQL programming language that interacts with RDBMS
* closed source (paid) and open source (MySQL, postgreSQL) - can be paid too for features like cloud storage 


### DEMO
* psycopg2 - for connecting in python? 
* pd.read_sql_query(query #query text,con #connection)
* cursor = object that connectrs 
* order of operations: from > where > group by > having > select > order by > limit 

* Window Function: 
<br> SELECT person, bar, date, row_number() 
<br> OVER (PARTITION BY person order by date DESC as vist_num
<br> FROM orders
<br> GROUP BY date
<br> ORDER BY 