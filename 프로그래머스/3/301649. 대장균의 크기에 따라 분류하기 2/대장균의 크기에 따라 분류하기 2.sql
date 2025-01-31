WITH Ranked AS (
    SELECT ID, SIZE_OF_COLONY,
        RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS rnk,
        COUNT(*) OVER () AS total_count
    FROM ECOLI_DATA
)

SELECT ID,
    CASE
        WHEN rnk <= total_count * 0.25 THEN 'CRITICAL'
        WHEN rnk <= total_count * 0.5 THEN 'HIGH'
        WHEN rnk <= total_count * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM Ranked
ORDER BY ID ASC