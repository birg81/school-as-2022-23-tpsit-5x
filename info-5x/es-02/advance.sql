SELECT
	p0.lastname AS cognome,
	p0.firstname AS nome,
	IF(p0.gender < 2 , "♂️", "♀") AS `⚥`,
	p0.birthday AS bDay,
	cb.name AS cityBorn,
	cl.name AS cityLive,
	cj.name AS cityJob
FROM
	(people AS p0)
		JOIN
	(cities AS cb)
		ON
	bornplace = cb.id,

	(people AS p1)
		JOIN
	(place2live AS l)
	ON
		l.people = p1.id
	JOIN
		(cities AS cl)
	ON
		l.place = cl.id,

	(people AS p2)
		JOIN
	(place2job AS j)
	ON
		j.people = p2.id
	JOIN
		(cities AS cj)
	ON
		j.place = cj.id
WHERE
	p1.id = p0.id AND
	p2.id = p0.id
ORDER BY
	cognome ASC;
