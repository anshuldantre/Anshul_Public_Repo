-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `names` ;

-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `names` DEFAULT CHARACTER SET utf8 ;
USE `names` ;

-- -----------------------------------------------------
-- Table `names`.`names`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `names`.`names` ;

CREATE TABLE IF NOT EXISTS `names`.`names` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updatde_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



show databases;
use names;
SELECT 
    *
FROM
    names;
INSERT INTO names (name, created_at, updated_at) values ('Anshul Dantre',now(), now());
SELECT 
    *
FROM
    names;
INSERT INTO names (name, created_at, updated_at) values ('Robert Buckley',now(), now()), ('Michael Choi',now(), now()), ('Stuart Yee',now(), now());
SELECT 
    *
FROM
    names;
UPDATE names 
SET 
    name = 'Mel Brooks'
WHERE
    id = 2;
SELECT 
    *
FROM
    names;
DELETE FROM names 
WHERE
    id = 4;
SELECT 
    *
FROM
    names;