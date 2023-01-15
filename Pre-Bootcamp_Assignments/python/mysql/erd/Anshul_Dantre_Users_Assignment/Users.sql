-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema user_schema
-- -----------------------------------------------------
-- New user schemas created for application
DROP SCHEMA IF EXISTS `user_schema` ;

-- -----------------------------------------------------
-- Schema user_schema
--
-- New user schemas created for application
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user_schema` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `user_schema` ;

-- -----------------------------------------------------
-- Table `user_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `user_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



SHOW DATABASES;
USE user_schema;
SELECT * FROM users;

INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
VALUES ('Anshul', 'Dantre', 'anshul.dantre@gmail.com', NOW(), NOW()),
('Robert', 'Buckley', 'robert.buckley@email.com', NOW(), NOW()),
('Michael', 'Choi', 'michael.choi@email.com', NOW(), NOW());

SELECT * FROM users;
SELECT * FROM users WHERE email='anshul.dantre@gmail.com';

SELECT * FROM users WHERE id=3;

UPDATE users 
set last_name = 'Pancakes'
WHERE id = 3;

SELECT * FROM users WHERE id=3;

DELETE FROM users WHERE id=2;
SELECT * FROM users;

SELECT * FROM users ORDER BY first_name;

SELECT * FROM users ORDER BY first_name desc;