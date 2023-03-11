-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cookies_and_orders
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cookies_and_orders` ;

-- -----------------------------------------------------
-- Schema cookies_and_orders
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cookies_and_orders` DEFAULT CHARACTER SET utf8 ;
USE `cookies_and_orders` ;

-- -----------------------------------------------------
-- Table `cookies_and_orders`.`cookies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cookies_and_orders`.`cookies` ;

CREATE TABLE IF NOT EXISTS `cookies_and_orders`.`cookies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cookie_type` VARCHAR(100) NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cookies_and_orders`.`customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cookies_and_orders`.`customers` ;

CREATE TABLE IF NOT EXISTS `cookies_and_orders`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NULL,
  `cerated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cookies_and_orders`.`orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cookies_and_orders`.`orders` ;

CREATE TABLE IF NOT EXISTS `cookies_and_orders`.`orders` (
  `cookie_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `num_of_boxes` INT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cookie_id`, `customer_id`),
  INDEX `fk_cookies_has_customers_customers1_idx` (`customer_id` ASC) VISIBLE,
  INDEX `fk_cookies_has_customers_cookies_idx` (`cookie_id` ASC) VISIBLE,
  CONSTRAINT `fk_cookies_has_customers_cookies`
    FOREIGN KEY (`cookie_id`)
    REFERENCES `cookies_and_orders`.`cookies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cookies_has_customers_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `cookies_and_orders`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
