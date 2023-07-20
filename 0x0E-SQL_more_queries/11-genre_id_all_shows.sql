-- Script that lists all shows contained in the database hbtn_0d_tvshows
SELECT	shows.title,
	s_gen.genre_id
FROM	tv_shows AS shows
LEFT JOIN tv_show_genres AS s_gen
ON shows.id = s_gen.show_id
ORDER BY shows.title, s_gen.genre_id;
