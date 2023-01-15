-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojos_and_ninjas_schema` ;

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_and_ninjas_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojos_and_ninjas_schema` ;

-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`dojos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas_schema`.`dojos` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`ninjas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas_schema`.`ninjas` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `age` INT NULL,
  `dojo_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_and_ninjas_schema`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




USE dojos_and_ninjas_schema;
SELECT * FROM dojos;
SELECT * FROM ninjas;

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Los Angeles', '2017-01-01 12:00:00', now()),
('Chicago', '2018-01-01 12:00:00', now()),
('Virginia', '2019-01-01 12:00:00', now());
SELECT * FROM dojos;

DELETE FROM dojos WHERE id =1 OR id=2 OR id=3;
DELETE FROM dojos WHERE id IN (1,2,3);
SELECT * FROM dojos;

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Raleigh', '2020-02-01 12:00:00', now()),
('Austin', '2021-02-01 12:00:00', now()),
('Las Vegas', '2022-02-01 12:00:00', now());
SELECT * FROM dojos;

SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Anshul','Dantre',30,4,now(), now()), ('Shradha','Dantre',26,4,now(), now()), ('Rahul','Jain',45,4,now(), now());
SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Komal','Jain',42,5,now(), now()), ('Avinash','Singh',55,5,now(), now()), ('Astha','Jain',51,5,now(), now());
SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES ('Ashish','Goenka',15,6,now(), now()), ('Nikita','Goenka',13,6,now(), now()), ('Chaitanya','Souhty',35,6,now(), now());
SELECT * FROM ninjas;

SELECT * FROM ninjas WHERE dojo_id=4;
SELECT ninjas.* FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.name='Raleigh';

SELECT * FROM ninjas WHERE dojo_id=5;
SELECT ninjas.* FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id=5;

SELECT ninjas.dojo_id, dojos.name FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE first_name='Chaitanya';