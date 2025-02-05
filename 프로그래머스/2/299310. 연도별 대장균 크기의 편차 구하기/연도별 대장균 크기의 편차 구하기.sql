WITH max_colony AS (
    SELECT YEAR(DIFFERENTIATION_DATE) AS year,
        MAX(SIZE_OF_COLONY) AS max_size
    FROM ECOLI_DATA
    GROUP BY year
)

SELECT YEAR(E.DIFFERENTIATION_DATE) AS YEAR,
    (M.max_size - E.SIZE_OF_COLONY) AS YEAR_DEV,
    E.ID
FROM ECOLI_DATA E
JOIN max_colony M ON YEAR(E.DIFFERENTIATION_DATE) = M.year
ORDER BY YEAR, YEAR_DEV;

