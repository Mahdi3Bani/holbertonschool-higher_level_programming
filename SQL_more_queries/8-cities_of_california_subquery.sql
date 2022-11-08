-- lists all cities 
SELECT id,
    name
FROM cities
WHERE state_id = (
        SELECT id
        from states
        where name = 'california'
    )
ORDER BY id ASC