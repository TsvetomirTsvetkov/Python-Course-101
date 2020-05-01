SELECT * FROM (SELECT maker, COUNT() AS pcs FROM pc LEFT OUTER JOIN product ON pc.model=product.model GROUP BY maker) WHERE pcs >= 3  
