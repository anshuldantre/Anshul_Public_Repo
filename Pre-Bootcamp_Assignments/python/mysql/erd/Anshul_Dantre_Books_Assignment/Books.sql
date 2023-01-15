-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema book_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `book_schema` ;

-- -----------------------------------------------------
-- Schema book_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_schema` DEFAULT CHARACTER SET utf8 ;
USE `book_schema` ;

-- -----------------------------------------------------
-- Table `book_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `book_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `book_schema`.`books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_schema`.`books` ;

CREATE TABLE IF NOT EXISTS `book_schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `book_schema`.`favourites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_schema`.`favourites` ;

CREATE TABLE IF NOT EXISTS `book_schema`.`favourites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_favourites_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_favourites_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_favourites_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `book_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favourites_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `book_schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


SHOW DATABASES;
USE book_schema;
SELECT * FROM books;
SELECT * FROM favourites;
SELECT * FROM users;

INSERT INTO users (first_name, last_name) 
VALUES ('Jane','Amsden'), ('Emily','Dixon'), ('Theodore','Dostoevsky'), ('William','Shapiro'), ('Lao','Xiu');
SELECT * FROM users;

INSERT INTO books (title)
VALUES ('C Sharp'), ('Java'), ('Python'), ('PHP'), ('Ruby');
SELECT * FROM books;

UPDATE books
SET title = 'C#'
WHERE title = 'C Sharp' AND id=1;
SELECT * FROM books;

UPDATE users
SET first_name = 'Bill'
WHERE id = 4;
SELECT * FROM users;

INSERT INTO favourites (user_id, book_id)
VALUES (1,1), (1,2);
SELECT * FROM favourites;

INSERT INTO favourites (user_id, book_id)
VALUES (2,1), (2,2), (2,3);
SELECT * FROM favourites;

INSERT INTO favourites (user_id, book_id)
VALUES (3,1), (3,2), (3,3), (3,4);
SELECT * FROM favourites;

INSERT INTO favourites (user_id, book_id)
VALUES (4,1), (4,2), (4,3), (4,4), (4,5);
SELECT * FROM favourites;

SELECT u.id, concat_ws(' ', u.first_name, u.last_name) username, b.title
FROM users u
JOIN favourites f
ON u.id = f.user_id
JOIN books b
ON f.book_id = b.id
WHERE b.id=3;

DELETE FROM favourites WHERE user_id=2 AND book_id=3;
SELECT u.id, concat_ws(' ', u.first_name, u.last_name) username, b.title
FROM users u
JOIN favourites f
ON u.id = f.user_id
JOIN books b
ON f.book_id = b.id
WHERE b.id=3;

INSERT INTO favourites (user_id, book_id)
VALUES (5,2);
SELECT * FROM favourites;

SELECT u.id, concat_ws(' ', u.first_name, u.last_name) username, b.title
FROM users u
JOIN favourites f
ON u.id = f.user_id
JOIN books b
ON f.book_id = b.id
WHERE u.id=3;

SELECT u.id, concat_ws(' ', u.first_name, u.last_name) username, b.title
FROM users u
JOIN favourites f
ON u.id = f.user_id
JOIN books b
ON f.book_id = b.id
WHERE b.id=5;