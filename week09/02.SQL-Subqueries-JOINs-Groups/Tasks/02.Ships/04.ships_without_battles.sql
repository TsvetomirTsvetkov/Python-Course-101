SELECT country, name FROM (SELECT ships.name, result, ships.class FROM ships LEFT JOIN outcomes on ships.name=outcomes.ship GROUP BY
           name) AS ship_out JOIN classes ON ship_out.class=classes.class WHERE result IS NULL ORDER BY country
