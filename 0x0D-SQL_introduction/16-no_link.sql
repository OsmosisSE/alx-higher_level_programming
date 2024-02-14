-- Lists the number of records with the same score in the table second_table.
-- Records are ordered by descending count.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
