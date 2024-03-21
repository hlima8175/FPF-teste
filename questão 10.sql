SELECT 
    name,
    ROUND(salary * 0.1, 2) AS taxa
FROM 
    people
WHERE 
    salary > 3000;