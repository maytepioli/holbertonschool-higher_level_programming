--  enumera la cantidad de registros con la misma puntuación en la tabla

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
