-- sts all shows contained that have at least one genre linked
-- lists all cities contained in the database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
FULL JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id