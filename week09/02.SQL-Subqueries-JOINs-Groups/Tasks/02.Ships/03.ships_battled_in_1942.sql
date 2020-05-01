SELECT ships.name FROM outcomes JOIN ships ON outcomes.ship=ships.name JOIN battles on outcomes.battle=battles.name WHERE date LIKE "%1942%" 
