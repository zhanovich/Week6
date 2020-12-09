CREATE SCHEMA `AddressBook` ;

/* Create people_master table*/
CREATE TABLE `AddressBook`.`people_master` (
  `person_id` INT NOT NULL AUTO_INCREMENT,
  `person_name` VARCHAR(100) NOT NULL,
  `person_DOB` DATE NULL,
  `active_phone_number` VARCHAR(20) NULL,
  PRIMARY KEY (`person_id`),
  UNIQUE INDEX `person_id_UNIQUE` (`person_id` ASC) VISIBLE);

/* Create addresses table*/
CREATE TABLE `AddressBook`.`addresses` (
  `address_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `street_address` VARCHAR(200) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`address_id`));

/* Create people_address*/
CREATE TABLE `AddressBook`.`people_address` (
  `person_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NULL
);

/* Populate DB */
INSERT INTO `AddressBook`.`addresses`
  (`street_address`, `city`, `state`, `zip_code`)
VALUES
  ('4th Avenue', 'Georgetown', 'Alabama', '28301'),
  ('270 Townstreet', 'Tampa', 'Florida', '33610'),
  ('2 Markway', 'New-York', 'New-York', '12001');

INSERT INTO `AddressBook`.`people_master`
  (`person_name`, `person_DOB`, `active_phone_number`)
VALUES
  ('George', '1996-6-01', '8134441122'),
  ('Thomas', '1969-12-4', '9921237744'),
  ('Erik', '1921-11-09', '7771234567'),
  ('Jack', '2000-11-25', '9002316455');

INSERT INTO `AddressBook`.`people_address`
  (`person_id`, `address_id`, `start_date`, `end_date`)
VALUES
  ('1', '1', STR_TO_DATE('2008-03-10', '%Y-%m-%d'), STR_TO_DATE('2010-06-12', '%Y-%m-%d')),
  ('1', '2', STR_TO_DATE('2011-05-30', '%Y-%m-%d'), NULL),
  ('2', '3', STR_TO_DATE('2008-09-10', '%Y-%m-%d'), NULL),
  ('3', '3', STR_TO_DATE('2000-07-21', '%Y-%m-%d'), NULL),
  ('4', '4', STR_TO_DATE('2019-12-28', '%Y-%m-%d'), NULL);
