# Day 5 Notes
## Lecture
* N/A - Mock Programming Test and Presentations 

## Compass Notes
[relationalDatabases SQL](https://code.tutsplus.com/tutorials/relational-databases-for-dummies--net-30244)
* data bases split to 'entities' to contain separate information
* joined on specific attributes/entry in a row)
* lucidcharts to see relationships and can be converted to a sql code

###  remove repetitive data 
1. Columns
* removing repetitive data = 1NF (first normal form) Edgar Codd
* no repeating columns 

2. Rows 
* 2NF - second normal form
* for e.g. full name gets repeated twice for each tweet 
* separate full name from tweets - and link via username 

3. Link table with keys
* give each row a unique identifier 'primary key'
* e.g. 'username' or separate 'id' incase username changes

'normalization' of database

### SQL (Structured Query Language)
* see link for intro on syntax
* end query with ;
``` SQL
SELECT <variable> FROM <entity> ;
/* to specify the variable */
WHERE <variable> = <'name'>; 
/* to specify multiple variable names */
WHERE <variable> IN ('name1, name2, name3');
/* or NOT IN */
```

* Query in sub-queries
```SQL
SELECT * FROM <entity> WHERE <variable> IN (
    SELECT <variable> FROM <entity2>);

SELECT title FROM songs WHERE artist IN (
    SELECT name from artists WHERE genre="Pop");
/* can add where to the subquery */
```

* For non-exact query
```SQL
WHERE <variable> LIKE "%name%";
/* % is placeholder either match before or after or both*/
```

* Restricting group results with HAVING 
* aggregate query - can't use where because it filters by that first - rather than the aggregate
* aggregate: SUM,AVG, 
```SQL
SELECT type, SUM(calories) AS total_calories FROM exercise_logs
    GROUP BY type /*what is in select must be in group by*/
    HAVING total_calories > 150;
SELECT author, SUM(words) AS total_words FROM books 
    GROUP BY author 
    HAVING total_words > 1000000;
SELECT author, AVG(words) as avg_words FROM books
    GROUP BY author
    HAVING avg_words > 150000;


/* this selects more than one entries with that type  */
SELECT type FROM exercise_logs GROUP BY type HAVING COUNT(*) >= 2;

/* to get a count for number of instances */
SELECT COUNT(*) FROM Exercise_logs WHERE heart_rate >= ROUND(0.50) * (220-30)

/* using the CASE - works like an IF function, creates a new column */
SELECT type, heart_rate,
    CASE
        WHEN heart_rate > 220-30 THEN "above max" 
        WHEN heart_rate > ROUND(0.90) * (220-30) THEN "above target"
        WHEN heart_rate > ROUND(0.50) * (220-30) THEN "within target"
        ELSE "below target"
    END as "hr_zone"
FROM exercise_logs;

/* from there we can use a count on the heart_rate zone */
/* remove previous query or change select and add group by */
SELECT COUNT(*), type,
    CASE
        WHEN heart_rate > 220-30 THEN "above max" 
        WHEN heart_rate > ROUND(0.90) * (220-30) THEN "above target"
        WHEN heart_rate > ROUND(0.50) * (220-30) THEN "within target"
        ELSE "below target"
    END as "hr_zone"
FROM exercise_logs
GROUP BY hr_zone
```

[SQLpractice](https://www.khanacademy.org/computing/computer-programming/sql/more-advanced-sql-queries/pp/project-data-dig)

```SQL
/* more complex examples from sql zoo */ 
SELECT game.mdate, game.team1, 
SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) AS score1,
game.team2,
SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) AS score2

FROM game
LEFT OUTER JOIN goal
ON goal.matchid = game.id
GROUP BY id, mdate, team1, team2
```

### Relational Databases in SQL
* one column of data should be stored in a single location
* updating in one updates in all 
* usually primary key is an id not a name


* JOINing Related tables
``` SQL
/* cross join */
SELECT * FROM <entity1>, <entity2>;

/* implicit inner join, basing off columns */
SELECT * FROM student_grades, students
    WHERE student_grades.student_id = students.id;

/* explicit inner join - JOIN - specify the entity/table you want take the column from
only when there's matching in both tables */ 

SELECT students.first_name FROM students
    JOIN student_grades
    ON students.id = student_grades.student_id
    WHERE grade > 90;

/* challenge example */ 
SELECT persons.name, hobbies.name FROM persons
    JOIN hobbies
    ON persons.id = hobbies.person_id

/* LEFT OUTER JOINS 
- to include cases even if missing from the other 
- keeps from Left (FROM) - reports null if missing from second (entity in LEFT OUTER JOIN)
- (not in SQL) RIGHT outer join does the opposite, but just switch order to make less confusing
- (not in SQL) FULL outer join - tries to join left and right but fills null when missing in both sides
*/
SELECT students.first_name 
    FROM students
    LEFT OUTER JOIN student_grades
    ON students.id = student_grades.student_id
    WHERE grade > 90;

/* Doing self-joins joining tables to themselves
when a row is related to another e.g. id 1 has buddy_id 2
note that buddies email is getting made as you are self-joining
note also the JOIN self new syntax for initiating a self join */
SELECT students.name, buddies.email as buddy_email
    FROM students
    JOIN students buddies
    ON students.buddy_id = buddies.id;

SELECT movies.title, sequels.title as sequel_title
    FROM movies
    LEFT OUTER JOIN movies sequels
    ON movies.sequel_id = sequels.id;

/* JOIN and SELF-JOINS together 
- more joins slower queries
- e.g. one entity showing pairs assigned to project e.g. 
*/
SELECT a.title, b.title FROM project_pairs  
/* basically makes up dummy entities of a and b as place holders for a self join */
    JOIN student_projects a /* self joins */ 
    ON project_pairs.project1_id = a.id
    JOIN student_projects b
    ON project_pairs.project2_id = b.id 

/* Nesting SELECTS */
SELECT movie.title, actor.name
FROM movie
JOIN casting 
ON movie.id=movieid
JOIN actor   
ON actorid=actor.id
WHERE casting.ord = 1 AND movieid IN (
SELECT movieid FROM casting
JOIN actor
ON casting.actorid = actor.id
WHERE actor.name ='Julie Andrews')

SELECT actor.name FROM movie
JOIN casting ON movie.id = casting.movieid
JOIN actor ON actor.id = casting.actorid
WHERE movie.id IN 

(SELECT movieid FROM casting
JOIN actor ON actor.id = casting.actorid
WHERE actor.name = 'Art Garfunkel')
 
AND actor.name != 'Art Garfunkel';


```
* SQL goes parse-optimize-execute
* how SQL executes determines speed of query - and may need to be planned before hand 
* can see how SQL is doing the query with EXPLAIN QUERY PLAIN 



### ERD (Entity Relationship Diagrams)
* entity - the table, has an 'instance' (the row/entry for each entity) 
* attribute - the column/variables
* primary key - an attribute or attributes that is unique - the unique identifier for an instance in that entity e.g. id
* relationship - attribute that entities are linked
* cardinality - count of instances that are allowed/necessary between entity relationships. minimum number req, max number allowed. 
* crow's foot notation for mandatory/optional

* composite primary key - means more than one attribute as primary key. ID + phone number 

* when creating a many-to-many relationship
    * need a bridge table take primary key from 2 entities 
    * e.g. employee assigned to many projects, single project can have multiple employees assigned. 
    * bridge will have employee ID and project ID as keys 
