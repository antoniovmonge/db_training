# MySQL
In `terminal` with MySQL:
- **Create** Database (called projects) / Or **connect** to database that already exists.
```
use projects;
```
> output: Database changed

- Create table
```SQL
CREATE TABLE projects(
    project_id INT(11) NOT NULL AUTO_INCREMENT,
    title VARCHAR(30),
    description VARCHAR(255),
    PRIMARY KEY(project_id)
);
```
- tests that the table is created
```
show tables;
```
> output: `"table results"`
  
---
Create another table:
```SQL
CREATE TABLE tasks(
    task_id INT(11) NOT NULL AUTO_INCREMENT,
    project_id INT(11) NOT NULL,
    description VARCHAR(255),
    PRIMARY KEY(task_id),
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
    );
```

```
show tables;
```

- Adding items to database
```SQL
INSERT INTO projects(title, description) VALUES ('Organize Photos', 'Organize old iPhone photos by year');
```

```SQL
INSERT INTO tasks(description, project_id) VALUES ('Organize 2020 Photos', 1);
```
> output: Query OK, 1 row affected (0.00 sec)
```
INSERT INTO tasks(description, project_id) VALUES ('Organize 2019 Photos', 1);
```

```SQL
INSERT INTO projects(title, description) VALUES ('Read more', 'Read a book a month this year');
```

```SQL
INSERT INTO tasks(description, project_id) VALUES ('Read the Huntress', 2);
```

```SQL
SELECT * FROM projects;
```
```
+-------------+------------------+--------------------------------------+
| project_id  | title            | description                          |
+-------------+------------------+--------------------------------------+
|           1 | Organize Photos  | Organize old iPhone photos by year   |
|           2 | Read more        | Read a book a month this year        |
+-------------+------------------+--------------------------------------+
```
