-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cookieorders
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cookieorders` ;

-- -----------------------------------------------------
-- Schema cookieorders
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cookieorders` DEFAULT CHARACTER SET utf8 ;
USE `cookieorders` ;

-- -----------------------------------------------------
-- Table `cookieorders`.`cookie_orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cookieorders`.`cookie_orders` ;

CREATE TABLE IF NOT EXISTS `cookieorders`.`cookie_orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(100) NULL,
  `cookie_type` VARCHAR(100) NULL,
  `num_of_boxes` INT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
