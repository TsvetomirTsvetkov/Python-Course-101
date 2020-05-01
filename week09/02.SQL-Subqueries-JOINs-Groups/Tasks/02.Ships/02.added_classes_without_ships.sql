SELECT name, country, numguns, launched FROM classes LEFT JOIN ships ON ships.class=classes.class WHERE classes.class LIKE (SELECT name FROM ships) OR ships.name IS NOT NULL
