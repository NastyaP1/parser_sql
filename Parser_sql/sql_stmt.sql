CREATE TABLE marks(
    id INT,
    mark INT,
);

INSERT INTO marks(id, mark) VALUES(1, 5);

SELECT id, name FROM dogs WHERE name = pes;

SELECT id FROM users WHERE age = 45;

SELECT id, age FROM users WHERE age >= 23;

DELETE FROM cats WHERE name = Tom;

DELETE FROM users;

UPDATE cats SET id = 12, name = Barsik WHERE name = Tom2;

UPDATE cats SET name = Barsik;