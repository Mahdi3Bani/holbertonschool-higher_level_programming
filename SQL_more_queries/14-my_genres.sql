-- lists all genres
SELECT tv_genres.name AS 'name'
FROM tv_shows
    INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;