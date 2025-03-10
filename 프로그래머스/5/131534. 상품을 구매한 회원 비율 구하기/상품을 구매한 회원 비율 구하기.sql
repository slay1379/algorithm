SELECT 
    DATE_FORMAT(O.SALES_DATE,'%Y') AS YEAR, 
    DATE_FORMAT(O.SALES_DATE,'%m') AS MONTH, 
    COUNT(DISTINCT O.USER_ID) AS PURCHASED_USERS, 
    ROUND(COUNT(DISTINCT O.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE DATE_FORMAT(JOINED,'%Y') = '2021'),1) AS PUCHASED_RATIO
FROM USER_INFO U
JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
WHERE DATE_FORMAT(U.JOINED,'%Y') = '2021'
GROUP BY YEAR,MONTH
ORDER BY YEAR,MONTH