SELECT * FROM (SELECT AVG(price) FROM pc JOIN product ON pc.model=product.model WHERE maker="B"), (SELECT AVG(price) FROM laptop JOIN product ON laptop.model=product.model WHERE maker="B") 
