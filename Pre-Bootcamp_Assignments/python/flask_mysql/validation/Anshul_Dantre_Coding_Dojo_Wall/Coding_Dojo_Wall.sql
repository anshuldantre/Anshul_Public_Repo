-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema coding_dojo_wall
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `coding_dojo_wall` ;

-- -----------------------------------------------------
-- Schema coding_dojo_wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `coding_dojo_wall` DEFAULT CHARACTER SET utf8 ;
USE `coding_dojo_wall` ;

-- -----------------------------------------------------
-- Table `coding_dojo_wall`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `coding_dojo_wall`.`users` ;

CREATE TABLE IF NOT EXISTS `coding_dojo_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(200) NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `coding_dojo_wall`.`posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `coding_dojo_wall`.`posts` ;

CREATE TABLE IF NOT EXISTS `coding_dojo_wall`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT(1000) NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `coding_dojo_wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
