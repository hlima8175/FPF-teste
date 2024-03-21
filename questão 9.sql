SELECT 
    name,
    customers_number
FROM 
    lawyers
WHERE 
    customers_number = (
        SELECT MAX(customers_number) FROM lawyers
    )
UNION ALL
SELECT 
    name,
    clientes
FROM 
    lawyers
WHERE 
    customers_number = (
        SELECT MIN(customers_number) FROM lawyers
    )
UNION ALL
SELECT 
    'Average' as name,
    AVG(clientes) as media
FROM 
    lawyers;