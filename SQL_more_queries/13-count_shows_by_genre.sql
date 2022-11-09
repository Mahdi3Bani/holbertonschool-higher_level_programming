-- lists all genres
SELECT tv_genres.name AS genre,
    COUNT(TS.genre_id) AS number_of_shows
FROM tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genres_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows;