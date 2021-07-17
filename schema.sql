

CREATE TABLE IF NOT EXISTS `Final_table` 
(
    `Customer_ID` INT NOT NULL,
    `engagement_score` TEXT DEFAULT NULL,
    `experience_score` VARCHAR(200) DEFAULT NULL,
    `satisfaction_score` TEXT DEFAULT NULL,
     
    PRIMARY KEY (`Customer_ID`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
