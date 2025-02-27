DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id              INTEGER PRIMARY KEY,
    first_name      VARCHAR(50) NOT NULL,
    last_name       VARCHAR(50) NOT NULL,
    age             INTEGER,
    grade           CHAR(1)
);

\COPY students FROM '/home/max/assignments/week_04/flask-postgresql/flaskr/students.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM students;