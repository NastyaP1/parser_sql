CREATE TABLE marks(
    id INT,
    mark INT,
);

SELECT * FROM dogs WHERE name = pes;

DELETE FROM cats WHERE name = Tom;

INSERT INTO cats(id, name) VALUES(1, Tom);

DELETE FROM cats;

UPDATE cats SET id = 12, name = Barsik WHERE name = Tom;
UPDATE cats SET id = 12, name = Barsik;