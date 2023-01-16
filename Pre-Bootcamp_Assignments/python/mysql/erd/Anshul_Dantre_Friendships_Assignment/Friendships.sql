-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema friendship_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `friendship_schema` ;

-- -----------------------------------------------------
-- Schema friendship_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendship_schema` DEFAULT CHARACTER SET utf8 ;
USE `friendship_schema` ;

-- -----------------------------------------------------
-- Table `friendship_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friendship_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `friendship_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `created_at` DATETIME NULL,
  `udpated_At` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendship_schema`.`friendships`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friendship_schema`.`friendships` ;

CREATE TABLE IF NOT EXISTS `friendship_schema`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL,
  `friend_id` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_users_users1_idx` (`friend_id` ASC) VISIBLE,
  INDEX `fk_users_has_users_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_users_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendship_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `friendship_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


SHOW DATABASES;
USE friendship_schema;
SELECT * FROM users;
SELECT * FROM friendships;

INSERT INTO users (first_name, last_name, created_at, udpated_at)
VALUES ('Amy', 'Giver', '2023-01-01','2023-01-01'), ('Eli', 'Byers', '2023-01-04','2023-01-04'), ('Marky', 'Mark', '2023-01-08','2023-01-08'), 
('Big', 'Bird', '2023-01-12','2023-01-12'), ('Kermit', 'The Frog', '2023-01-16','2023-01-16');
SELECT * FROM users;

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1,2,'2023-01-05','2023-01-05'), (1,4,'2023-01-13','2023-01-13'), (1,5,'2023-01-16','2023-01-16'),(2,5,'2023-01-16','2023-01-16'), (2,3,'2023-01-09','2023-01-09'), 
(3,4,'2023-01-16','2023-01-16');
SELECT * FROM friendships;

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id;

-- Query: Create 6 new users 
INSERT INTO users (first_name, last_name, created_at, udpated_at)
VALUES ('Anshul', 'Dantre', '2023-01-01','2023-01-01'), ('Shradha', 'Tripathi', '2023-01-04','2023-01-04'), ('Rahul', 'Jain', '2023-01-08','2023-01-08'), 
('Komal', 'Nahata', '2023-01-12','2023-01-12'), ('Avinash', 'Singh', '2023-01-16','2023-01-16'), ('Astha', 'J', '2023-01-16','2023-01-16');
SELECT * FROM users;
-- 1	-- 6	Anshul	Dantre
-- 2	-- 7	Shradha	Tripathi
-- 3	-- 8	Rahul	Jain
-- 4	-- 9	Komal	Nahata
-- 5	-- 10	Avinash	Singh
-- 6	-- 11	Astha	J

-- Query: Have user 1 be friends with user 2, 4 and 6
-- Anshul friends with Shradha, Komal & Astha
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (6,7,'2023-01-05','2023-01-05'), (6,9,'2023-01-13','2023-01-13'), (6,11,'2023-01-16','2023-01-16');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=6;

-- Query: Have user 2 be friends with user 1, 3 and 5
-- Shradha friends with Anshul, Rahul and Avinash
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (7,6,'2023-01-05','2023-01-05'), (7,8,'2023-01-13','2023-01-13'), (7,10,'2023-01-16','2023-01-16');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=7;

-- Query: Have user 3 be friends with user 2 and 5
-- Rahul friends with Shradha and Avinash
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (8,7,'2023-01-05','2023-01-05'), (8,10,'2023-01-13','2023-01-13');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=8;

-- Query: Have user 4 be friends with user 3
-- Komal friends with Rahul
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (9,8,'2023-01-05','2023-01-05');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=9;

-- Query: Have user 5 be friends with user 1 and 6
-- Avinash Friends with Anshul and Astha
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (10,6,'2023-01-05','2023-01-05'), (10,11,'2023-01-13','2023-01-13');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=10;

-- Query: Have user 6 be friends with user 2 and 3
-- Astha friends with Shradha and Rahul
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (11,7,'2023-01-05','2023-01-05'), (11,8,'2023-01-13','2023-01-13');
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=11;

-- Query: Display the relationships created as shown in the table in the above image
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id > 5;

-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON (users.id = friendships.user_id OR users.id = friendships.friend_id)
LEFT JOIN users as user2
ON (friendships.friend_id = user2.id OR friendships.user_id=user2.id)
WHERE users.id=6
AND users.id <> user2.id;

-- NINJA Query: Return the count of all friendships
-- Additional data in my table and hece additional filter to eliminate the unwatned records
SELECT count(*) FROM friendships WHERE user_id > 5;
SELECT COUNT(user_id) AS total_friends, user_id 
FROM friendships
WHERE user_id > 5
GROUP BY user_id;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT users.id, users.first_name, users.last_name, COUNT(friendships.user_id) AS total_friends
FROM friendships
JOIN users
ON friendships.user_id = users.id
WHERE user_id > 5
GROUP BY friendships.user_id
ORDER BY COUNT(friendships.user_id) DESC
LIMIT 2;

-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as user2
ON friendships.friend_id = user2.id
WHERE users.id=8
ORDER BY user2.first_name;