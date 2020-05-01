SELECT maker FROM (SELECT maker, MAX(price) FROM pc LEFT OUTER JOIN product ON pc.model=product.model)
