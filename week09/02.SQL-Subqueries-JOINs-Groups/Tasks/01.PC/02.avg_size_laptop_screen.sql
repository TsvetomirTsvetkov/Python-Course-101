SELECT maker, AVG(screen) FROM LAPTOP JOIN product ON laptop.model=product.model GROUP BY maker  
