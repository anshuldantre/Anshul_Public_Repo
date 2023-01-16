USE sakila;
SELECT * FROM actor;
SELECT * FROM address;
SELECT * FROM category;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM customer;
SELECT * FROM film;
SELECT * FROM film_actor;
SELECT * FROM film_category;
SELECT * FROM film_list;
SELECT * FROM film_text;
SELECT * FROM inventory;
SELECT * FROM language;
SELECT * FROM payment;
SELECT * FROM rental;
SELECT * FROM staff;
SELECT * FROM store;

-- Views
SELECT * FROM actor_info;
SELECT * FROM customer_list;
SELECT * FROM film_list;
SELECT * FROM nicer_but_slower_film_list;
SELECT * FROM sales_by_film_category;
SELECT * FROM sales_by_store;
SELECT * FROM staff_list;


-- 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
SELECT adr.city_id, cus.first_name, cus.last_name, cus.email, adr.address, c.city, con.country
FROM customer cus
JOIN address adr
ON cus.address_id = adr.address_id
JOIN city c
ON adr.city_id = c.city_id
JOIN country con
ON c.country_id = con.country_id
WHERE adr.city_id=312;

-- 2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE c.name='Comedy';

-- 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
SELECT a.actor_id, a.first_name, a.last_name, f.title, f.description, f.release_year
FROM film_actor fa
JOIN film f
ON fa.film_id = f.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
WHERE fa.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.
SELECT cus.first_name, cus.last_name, cus.email, a.address, a.address2, a.district, ct.city, co.country, a.postal_code
FROM customer cus
JOIN address a 
ON cus.address_id = a.address_id
JOIN city ct
ON a.city_id = ct.city_id
JOIN country co
ON ct.country_id = co.country_id
WHERE cus.store_id = 1
AND ct.city_id IN (1, 42, 312, 459);

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
WHERE f.rating ='G'
AND f.special_features like '%behind the scenes%'
AND fa.actor_id = 15;

-- 6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.
SELECT f.film_id, f.title, a.actor_id, a.first_name, a.last_name
FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
WHERE f.film_id=369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE f.rental_rate ='2.99'
AND c.name='Drama';

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre, a.first_name, a.last_name
FROM film f
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE a.first_name='SANDRA'
AND a.last_name = 'KILMER'
AND c.name='Action';