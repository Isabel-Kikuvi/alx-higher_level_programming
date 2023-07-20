-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT	shows.title,
	s_gen.genre_id
FROM	tv_shows AS shows
LEFT JOIN tv_show_genres AS s_gen
ON shows.id = s_gen.show_id
WHERE s_gen.genre_id IS NULL
ORDER BY shows.title, s_gen.genre_id;
