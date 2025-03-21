SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
WHERE EXISTS (
    SELECT 1 FROM SKILLCODES S
    WHERE (D.SKILL_CODE & S.CODE) <> 0
      AND S.NAME IN ('Python', 'C#')
)
ORDER BY D.ID ASC;
