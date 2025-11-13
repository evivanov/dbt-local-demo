SELECT product, AVG(price) AS avg_price
FROM {{ source('raw', 'raw_sales') }}
GROUP BY product
ORDER BY avg_price DESC