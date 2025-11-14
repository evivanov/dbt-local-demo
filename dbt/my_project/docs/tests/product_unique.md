{% docs test_product_unique %}

This test ensures that each product appears only once in the aggregated results. Since this is a summary table with one row per product, duplicates would indicate a problem with the aggregation logic or data pipeline. Uniqueness is essential for accurate reporting and prevents double-counting of sales metrics in downstream analyses.

{% enddocs %}
