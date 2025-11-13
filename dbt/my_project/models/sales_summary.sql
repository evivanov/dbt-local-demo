SELECT
    product,
    SUM(price * quantity) AS total_sales,
    COUNT(*) AS transactions
FROM {{ source('raw', 'raw_sales') }}
GROUP BY product
ORDER BY total_sales DESC