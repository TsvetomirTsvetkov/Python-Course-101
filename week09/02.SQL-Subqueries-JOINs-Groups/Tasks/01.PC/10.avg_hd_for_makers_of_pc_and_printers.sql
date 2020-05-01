SELECT AVG(hd) FROM pc JOIN product ON product.model=pc.model WHERE product.maker IN (SELECT maker FROM product WHERE type="Printer" GROUP BY maker)
