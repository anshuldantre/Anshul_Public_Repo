-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_authors_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books_authors_schema` ;

-- -----------------------------------------------------
-- Schema books_authors_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_authors_schema` DEFAULT CHARACTER SET utf8 ;
USE `books_authors_schema` ;

-- -----------------------------------------------------
-- Table `books_authors_schema`.`authors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_authors_schema`.`authors` ;

CREATE TABLE IF NOT EXISTS `books_authors_schema`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_authors_schema`.`books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_authors_schema`.`books` ;

CREATE TABLE IF NOT EXISTS `books_authors_schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_authors_schema`.`favourites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_authors_schema`.`favourites` ;

CREATE TABLE IF NOT EXISTS `books_authors_schema`.`favourites` (
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`author_id`, `book_id`),
  INDEX `fk_authors_has_books_books1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_authors_has_books_authors_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `fk_authors_has_books_authors`
    FOREIGN KEY (`author_id`)
    REFERENCES `books_authors_schema`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_authors_has_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_authors_schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
