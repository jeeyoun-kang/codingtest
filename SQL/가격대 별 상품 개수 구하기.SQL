SELECT
    CASE
        WHEN PRICE<10000 THEN 0
        ELSE TRUNCATE(PRICE,-4) --숫자를 버릴 자릿수 아래로 버림
        END PRICE_GROUP
    ,COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;