USE world;
SELECT * FROM countries;
SELECT * FROM cities;
SELECT * FROM languages;

-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. 
-- Your query should arrange the result by language percentage in descending order. (1)
SELECT c.name, l.language, l.percentage
FROM languages l
JOIN countries c
ON l.country_id = c.id
WHERE l.language = 'Slovene'
ORDER BY l.percentage DESC;

-- 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. (3)
SELECT co.name, count(ci.name)
FROM cities ci
JOIN countries co
ON ci.country_id = co.id 
GROUP BY co.name
ORDER BY count(cc.name) DESC;

-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
-- Your query should arrange the result by population in descending order. (1)
SELECT co.name, ci.population, ci.name
FROM cities ci
JOIN countries co
ON ci.country_id = co.id 
WHERE co.name='Mexico'
AND ci.population > 500000
ORDER BY ci.population DESC;

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? 
-- Your query should arrange the result by percentage in descending order. (1)
SELECT c.name, l.language, l.percentage
FROM countries c
JOIN  languages l
ON c.id = l.country_id
WHERE l.percentage > 89
ORDER BY l.percentage DESC;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501
AND population > 100000;

-- 6. What query would you run to get countries with only Constitutional Monarchy governments, with a capital greater than 200 and a life expectancy greater than 75 years? (1)
SELECT name, government_form,  capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy'
AND capital > 200
AND life_expectancy > 75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? 
-- The query should return the Country Name, City Name, District and Population. (2)
SELECT co.name, ci.name, ci.district, ci.population
FROM cities ci
JOIN countries co
ON ci.country_id = co.id 
WHERE co.name='Argentina'
AND ci.district='Buenos Aires'
AND ci.population > 500000;

-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries.
-- Also, the query should arrange the result by the number of countries in descending order. (2)
SELECT region, COUNT(name) 
FROM countries
GROUP BY region
ORDER BY COUNT(name) DESC;