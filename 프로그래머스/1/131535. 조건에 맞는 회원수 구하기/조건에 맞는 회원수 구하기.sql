SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE >= 20 AND AGE <= 29 AND DATE_FORMAT(JOINED,'%Y') = 2021