-- enumerar las ciudades de california 
SELECT cities.name, cities.id
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;