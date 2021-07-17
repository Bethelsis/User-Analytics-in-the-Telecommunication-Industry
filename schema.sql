

CREATE TABLE IF NOT EXISTS `Final_table` 
(
    `Customer_ID` FLOAT NOT NULL,
    `engagement_score` FLOAT DEFAULT NULL,
    `experience_score` FLOAT DEFAULT NULL,
    `satisfaction_score` FLOAT DEFAULT NULL,
   
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
